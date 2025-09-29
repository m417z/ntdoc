This structure is partially [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/ns-ntddk-kuser_shared_data). However, as verified on 2025-09, almost all Microsoft documentation for this structure is either outdated, useless, or downright incorrect.  


# Introduction
KUSER_SHARED_DATA structure defines layout of the memory region, shared between kernelmode and usermode. It occupies a single physical page, mapped in oskernel at fixed address `0xFFFF'F780'0000'0000` (0xFFFFF78000000000), and in all but the _Minimal_ processes at `0x7FFE'0000` (0x7FFE0000). Since win11 23H2, the fixed virtual address in kernel is read-only; `nt!MmWriteableSharedUserData` holds a randomized virtual address of the writeable kernelmode mapping.


# Definition
Here is the full definition, with all fields properly documented.  
It has been enriched with field offsets and five special sigils to help you quickly assess each item.  

Legend:  
𝍌 - field fixed at boot and won't change at runtime  
❕ - changes often (e.g. secondwise)  
◷ - changes rarely (e.g. hourly)  
👋 – can be changed by usermode applications at runtime  
♻ – field is either reserved, or deprecated, or it has no real reason to be in kuser and should be moved elsewhere

```cpp
struct _KUSER_SHARED_DATA
{
    // Unused, deprecated for more than 20 years. Always zero.
    ULONG TickCountLowDeprecated;                   // 000 𝍌♻

    // Number of milliseconds per ostick, left-shifted by 0x18.
    // Mirrors nt!ExpTickCountMultiplier, derived directly from nt!KeMaximumIncrement. Across all archs, value is
    // clamped to a max of 0x0FA00000 (1/64 s, or 15.625 ms). And in fact, you'll almost never see anything else there,
    // except maybe 0x0F99A027 on some old systems (~15.600 ms, or 15.600099980831146 ms exactly).
    // GetTickCount() => (🡗TickCountMultiplier × 🡓TickCountQuad) >> 0x18.
    // Duration of an ostick is fixed at boot time, stored in nt!KeMaximumIncrement. Not to be confused with the clock
    // tick duration, nt!KeTimeIncrement, which can change at runtime (in 🡓InterruptTime description right below).
    ULONG TickCountMultiplier;                      // 004 𝍌

    // Number of centums (100 ns units) since system start. Value monotonically increases. Includes sleep/hibernation
    // time and the like (the "bias"); i.e. value jumps forward on wakeup. For raw uptime, subtract 🡓InterruptTimeBias.
    // Updated on each clock interrupt on the clock owner processor. Current update period is nt!KeTimeIncrement,
    // adjustable via NtSetTimerResolution (aka timeBeginPeriod), in the hardcoded range [0.5 ms, 15.625 ms].
    // Actual adjustable range can be smaller; set at boot as [nt!KeMinimumIncrement, nt!KeMaximumIncrement].
    // See 🡓TickCountQuad description on how to change this field initial value from 0 to up to 49.71 days.
    // Coherence of this field vs 🡓SystemTime, 🡓TickCountQuad, and certain others is ensured via 🡓TimeUpdateLock.
    volatile KSYSTEM_TIME InterruptTime;            // 008 ❕ changes each clock interrupt

    // UTC System Time. Number of centums since 1601-01-01, exactly. It's a perfectly raw value; any conversions or
    // adjustments (like leap days or leap seconds) ought to be done on the higher level.
    // Coherence of this field vs 🡑InterruptTime, 🡓TickCountQuad, and certain others is ensured via 🡓TimeUpdateLock.
    // Asilous clients with SeSystemtime privilege can set it via NtSetSystemTime to any value in range [0, 2⁶¹+2³²),
    // which is [1601-01-01, 8907-12-05 18:49:10]. Note regular users don't have SeSystemtime privilege by default.
    volatile KSYSTEM_TIME SystemTime;               // 014 ❕👋 changes each clock interrupt + adjustable

    // Current 64-bit time zone bias. Silo-aware: SILO_USER_SHARED_DATA.TimeZoneBias.
    // It's the value you *subtract* from 🡑SystemTime to get Local Time. It's already pre-adjusted for daylight saving.
    // E.g. for Pacific Time (-08:00) value will be 7:00 in Summer (0x3AAC5ED800 == 7×3600×10⁷).
    // See 🡓TimeZoneBiasEffectiveStart description for when this field is considered valid.
    // Coherence of this field vs the 🡓TimeZoneBiasEffective* values ensured via 🡓TimeZoneBiasStamp.
    // Clients with SeTimeZone privilege can set bias using SystemTimeZoneInformation/SystemDynamicTimeZoneInformation
    // infoclasses. Range is ±2³¹ seconds (±68 years), granularity 1 minute. Regular users on client OS versions
    // DO have SeTimeZone privilege by default; on server OS versions they don't. Note timezone info is stored under
    // CCS\Control\TimeZoneInformation key; using timezone infoclasses grants users limited writeability to that key.
    volatile KSYSTEM_TIME TimeZoneBias;             // 020 ◷👋 changes at runtime (~twice a year), manually adjustable

    // Fixed values, set at boot (in nt!InitBootProcessor). Both fields are the same: 0x8664 for x64, 0xAA64 for ARM64.
    // Settable in kernel mode via RtlSetSystemGlobalData(GlobalDataIdImageNumberLow/GlobalDataIdImageNumberHigh[=4/5]).
    USHORT ImageNumberLow;                          // 02C 𝍌
    USHORT ImageNumberHigh;                         // 02E 𝍌

    // Win32 system root path, e.g. "C:\Windows" – without quotes, without trailing slash.
    // First wchar is adjustable in kernel mode via RtlSetSystemGlobalData(GlobalDataIdNtSystemRootDrive[=15]).
    // OS receives path from the osloader (winload.efi), in LoaderBlock.NtBootPathName. But LoaderBlock path has
    // no drive letter, so it's retrieved from the MountPointManager via IOCTL_MOUNTMGR_BOOT_DL_ASSIGNMENT.
    // Silo-aware: RtlGetNtSystemRoot, SILO_USER_SHARED_DATA.NtSystemRoot.
    WCHAR NtSystemRoot[0x104];                      // 030 𝍌♻ used now, but really shouldn't be in kuser

    // "Maximum stack trace depth if tracing is enabled".
    // Appears to be deprecated, unused, always zero.
    ULONG MaxStackTraceDepth;                       // 238 𝍌♻

    // Crypto exponent for yolocrypto. Unused, always zero. In the past could be non-zero only for "internal" OS builds.
    ULONG CryptoExponent;                           // 23C 𝍌♻

    // Time zone ID, TIME_ZONE_ID_*. Silo-aware: SILO_USER_SHARED_DATA.TimeZoneId.
    // 0: *_UNKNOWN (aka neither, DST not used), 1: *_STANDARD (winter), 2: *_DAYLIGHT (summer).
    // Settable in kernel mode via RtlSetSystemGlobalData(GlobalDataIdTimeZoneId[=6]).
    // ⚠️ Unlike 🡑TimeZoneBias and 🡓TimeZoneBiasEffective*, this field is NOT protected via 🡓TimeZoneBiasStamp; it is
    // set before starting the 🡓TimeZoneBiasStamp update sequence. For coherence between this and other timezone
    // fields: read this first, then others, then read this field again and ensure it hasn't changed.
    // Indirectly adjustable by clients with SeTimeZone privilege, together with 🡑TimeZoneBias.
    ULONG TimeZoneId;                               // 240 ◷👋 changes at runtime ~twice a year, manually adjustable

    // Minimum size of a large page, in bytes. Determined by the CPU. On boot nt!MiInitSystem sets it to hardcoded 2 MB.
    // It seems the only purpose of this field is to simplify implementation of exported kernelbase!GetLargePageMinimum.
    ULONG LargePageMinimum;                         // 244 𝍌♻ used now, but really shouldn't be in kuser

    // AIT sampling rate. TL note: AIT means App Impact Telemetry. Related to KIT, Kernel Impact Telemetry.
    // Related to ETW provider MS_Windows_AIT_Provider and exported api nt!KitLogFeatureUsage. Most likely deprecated.
    // Set during boot in nt!KitpInitAitSampleRate from CCS\Control\Session Manager\AppCompatCache₄Rate, unless it's
    // a safeboot. By default there is nothing in registry, so normally this field is 0.
    // Can be adjusted by holders of SeProfileSingleProcess privilege: NtSetSystemInformation(SystemAitSamplingValue).
    ULONG AitSamplingValue;                         // 248 👋♻

    // "This value controls switchback processing".
    // Seemingly deprecated, unused, and always 0. But there's an active PEB field of similar name: PEB.AppCompatFlags.
    ULONG AppCompatFlag;                            // 24C 𝍌♻

    // Number of times since boot CNG.sys has reseeded its entropy pool.
    // Reseed can be triggered via exported cng!EntropyPoolTriggerReseedForIum, but it mostly auto-reseeds at these
    // intervals after the previous auto-reseed, in seconds: 1, 3, 9, 27, 81, 243, 729, 2187, 3600, 3600, 3600,..
    // I.e. interval triples till it hits one hour (but there's about 5 extra reseeds at system start).
    // On boot you'll often see 8 here; +27s: 9; +81s more: 10; after 6/18/55/115 minutes of uptime: 11/12/13/14; etc.
    // Settable in kernel mode via RtlSetSystemGlobalData(GlobalDataIdRngSeedVersion[=1]).
    ULONGLONG RNGSeedVersion;                       // 250 ◷ incremened periodically (every hour on average)

    // Set of flags to control assert failures handling. Read on boot from CCS\Control\ValidationRunLevels₄Global. See
    // VRL_* flags in sdk; from oskernel view the only bit is VRL_ENABLE_KERNEL_BREAKS, it only affects debug OS builds.
    ULONG GlobalValidationRunlevel;                 // 258 𝍌♻

    // Sequence number/lock for timezone data: 🡑TimeZoneBias, 🡓TimeZoneBiasEffectiveStart, 🡓TimeZoneBiasEffectiveEnd.
    // When value is odd, the set of fields is being updated. See "Cross-fields coherence via sequence numbers" below
    // for details. Clients without any privileges can increment it by two via NtSetSystemTime(null, null).
    // Silo-aware: SILO_USER_SHARED_DATA.TimeZoneBiasStamp.
    volatile LONG TimeZoneBiasStamp;                // 25C ◷👋 changes at runtime rarely (e.g. daily), +manual adjust

    // Mirrors exported nt!NtBuildNumber, but with its higher nibble zeroed.
    // For nt!NtBuildNumber, higher nibble is 0xC in Checked (debug) builds, or 0xF in Free (release) builds.
    // Initially set to a hardcoded value for current ntoskrnl, equal to the "real" value in FixedFileVersionInfo (e.g.
    // 19041); during boot re-set to a dword from registry (e.g. 19045). This field (or rather the nt!NtBuildNumber it's
    // derived from) has modest usage throughout the system, but it does affect codepaths. Goes into PEB.NtBuildNumber.
    // Reg path for win10: HKLM\Software\Microsoft\Windows NT\CurrentVersion\EditionVersion₄EditionBuildNumber.
    // For WS2022/win11: HKLM\SYSTEM\Software\Microsoft\BuildLayers\<SubkeyWithValue.IsTopLevel==1>₄BuildNumber.
    // "The shared collective build number undecorated with C or F." – original WDK gem, kept for posterity.
    ULONG NtBuildNumber;                            // 260 𝍌

    // Product type: client (e.g. Windows 10) VS server (e.g. Windows Server 2022) VS domain controller server.
    // 1/NtProductWinNt: client OS; 2/NtProductLanManNt: Windows Server in DC role; 3/NtProductServer: Windows Server.
    // Set on boot in nt!MiMemoryLicense, from nt!MmRegistryState.ProductType: CCS\Control\ProductOptions₄ProductType.
    // Silo-aware: RtlGetNtProductType, SILO_USER_SHARED_DATA.NtProductType.
    NT_PRODUCT_TYPE NtProductType;                  // 264 𝍌

    // Tells APIs they can use 🡑NtProductType field instead of querying that info from registry.
    // Normally it's 1, except during system install ("SystemSetupInProgress").
    BOOLEAN ProductTypeIsValid;                     // 268 𝍌♻

    // Zero.
    BOOLEAN Reserved0[1];                           // 269 𝍌♻

    // PROCESSOR_ARCHITECTURE_* constant, e.g. 9 for PROCESSOR_ARCHITECTURE_AMD64, 12 for _ARM64.
    USHORT NativeProcessorArchitecture;             // 26A 𝍌♻; shouldn't be in kuser; wow/sxs should use regular api

    // OS Version, set at boot to fixed values (in nt!InitBootProcessor). E.g. win7: 6 major, 1 minor.
    // Usual values: 5.1, 5.2, 6.0, 6.1, 6.2, 6.3; hardcoded to 10.0 since win10, stays as such in win11.
    // Unlike 🡑NtBuildNumber, adjusting MajorVersion & MinorVersion in registry does NOT affect these fields.
    ULONG NtMajorVersion;                           // 26C 𝍌
    ULONG NtMinorVersion;                           // 270 𝍌

    // Processor and/or OS features. See PF_* flags. Unfortunately, one whole byte used per flag.
    // Used by kernelbase!IsProcessorFeaturePresent (via ntdll!RtlIsProcessorFeaturePresent).
    // ⚠️ Older OS versions may not set all expected flags, even if feature is actually supported by CPU and OS.
    BOOLEAN ProcessorFeatures[0x40];                // 274 𝍌; 0x40 is PROCESSOR_FEATURE_MAX

    // Obsolete, dnu: always 0x7FFEFFFF on 64-bit OS. On 32-bit OS mirrors MM_HIGHEST_USER_ADDRESS (sensible with /3GB).
    ULONG Reserved1;                                // 2B4 𝍌♻; aka MaximumUserModeAddressDeprecated

    // Obsolete, dnu: always 0x80000000 on 64-bit OS. On 32-bit OS mirrors MmSystemRangeStart.
    ULONG Reserved3;                                // 2B8 𝍌♻; aka SystemRangeStartDeprecated

    // "Time slippage while in debugger".
    // So, supposedly "time wasted debugging", but there's strong indication this field is obsolete and always zero.
    volatile ULONG TimeSlip;                        // 2BC 𝍌♻; *most likely* fixed at boot to 0 and doesn't change

    // Always zero. Previously: "alternative system architecture, e.g., NEC PC98xx on x86".
    ULONG AlternativeArchitecture;                  // 2C0 𝍌♻; type is 2-const enum ALTERNATIVE_ARCHITECTURE_TYPE

    // Number of boots since OS install (really, boot attempts). Osloader (winload.efi) reads \Windows\bootstat.dat
    // (BSD_BOOT_STATUS_DATA.LastBootId`0x34), increments and resaves it; passes value through LoaderBlock for
    // nt!InitBootProcessor, which stores it here. Filepath is changeable via BsdLogPath; ntoskrnl reduplicates it
    // from the loader block into CCS\ControlₛOsBootstatPath.
    // Hyper-V docker containers run with BootId == 1; at least some Windows Sandbox instances run with BootId == 2.
    ULONG BootId;                                   // 2C4 𝍌

    // Value of 🡑SystemTime when system expires. Normally 0, which means no expiration. Not related to activation.
    // Evaluation OS versions have real value here. Used by winver.exe directly, and by win32k*.sys to paint watermark.
    // Set during boot from data returned by nt!ExGetExpirationDate() [ZwQueryLicenseValue("Kernel-ExpirationDate")].
    LARGE_INTEGER SystemExpirationDate;             // 2C8 𝍌

    // VER_SUITE_* mask, i.e. (1 << SUITE_TYPE::*). E.g. if bit16 set, it's Windows Phone (SUITE_TYPE::PhoneNT == 16).
    // Over time got sidelined; mostly you'll see just the minimum: 0x110 == VER_SUITE_TERMINAL|VER_SUITE_SINGLEUSERTS.
    // Silo-aware: RtlGetSuiteMask, SILO_USER_SHARED_DATA.SuiteMask.
    ULONG SuiteMask;                                // 2D0 𝍌

    // Kernel Debugger status bitmask. Value can change dynamically into any state (e.g. 1 -> 3 -> 0 -> 3 -> 1 -> ...).
    // Bit0 mirrors exported boolean nt!KdDebuggerEnabled (debugger enabled, but not necessarily connected).
    // Bit1 is negation of the exported bool nt!KdDebuggerNotPresent (that is: when bit1 is 1, KD is connected/active).
    // 🔎 Example: booted with "bcdedit /debug on", but w/o KD running: field=1 (enabled, not connected);
    // then launched KD on host: guest OS connects to KD, field changes 1->3 (active); run "kdbgctrl -d" on guest, aka
    // NtSystemDebugControl(SysDbgDisableKernelDebugger): field changes 3->0 (forcing KD disconnect until dbg events).
    // Can also change 0->1/3 with kdbgctrl as long as nt!KdPitchDebugger is false (i.e. "/debug on" is true).
    // Settable in kernel mode via RtlSetSystemGlobalData(GlobalDataIdKdDebuggerEnabled[=10]), done by kdxxx/kdnet.dll.
    UCHAR KdDebuggerEnabled;                        // 2D4 ◷👋 may change if debugger connected; manually adjustable

    union
    {
        // Minor subset of system mitigations.
        UCHAR MitigationPolicies;                   // 2D5 𝍌
        struct
        {
            // NX_SUPPORT_POLICY_* values. Only meaningful for 32-bit x86 processes. From "bcdedit /set nx VALUE".
            // Applied at process startup via NtSetInformationProcess(ProcessExecuteFlags).
            UCHAR NXSupportPolicy: 2;

            // SEH_VALIDATION_POLICY_* values. Only meaningful for 32-bit x86 processes. Set on boot from
            // CCS\Control\Session Manager₄DisableExceptionChainValidation. App IFEO value with the same name trumps it.
            UCHAR SEHValidationPolicy: 2;

            // Determines what kinds of devices are illegal to have Current Working Directory searched for dlls. From
            // CCS\Control\Session Manager₄CWDIllegalInDLLSearch. App-specific IFEO value with the same name trumps it.
            // 0: any allowed; 1: WebDav; 2: any Remote device; 3: all devices illegal, never use CWD (-1 in registry).
            UCHAR CurDirDevicesSkippedForDlls: 2;

            // Zero.
            UCHAR Reserved: 2;
        };
    };

    // Measured duration of "pause" (x86) or "yield" (ARM) instructions, in TSC (rdtsc) cycles. Determines how many
    // times to spin, e.g. in RtlBackoff (both rings). Early at boot set to 10, then – at later boot stages – updated
    // with data from nt!ExpComputeCyclesPerYield. Example: 0x0D, 0x18, 0x84. Measured values can vary boot to boot! OS
    // clamps value in range [1, 0xFFFF]. So if value is 0, the OS is simply too old to use it: older than win10 1903.
    USHORT CyclesPerYield;                          // 2D6 𝍌

    // Current physical console Session Id. RDP sessions ignored. During boot it's 0. Right after the boot it may stay
    // 0 (Hyper-V docker container), change to 1 (normal box, Logon Screen), or to -1 (Windows Sandbox, kind of RDP).
    // Note Hyper-V Manager *basic* sessions are "physical", but *enhanced* sessions are RDP; thus in enhanced sessions
    // you'll observe some "leftover" here, but really it'll be the "physical" basic session LogonUI.exe is running in.
    // When the physical box (or its equivalent) is locked, value *may* change; happens when LogonUI.exe is created in
    // a new session, which is the case if there are already several user sessions (physical or RDP).
    // Field set by win32kbase.sys and win32kfull.sys; they use dedicated exported api, nt!RtlSetActiveConsoleId.
    // Silo-aware: RtlGetActiveConsoleId, SILO_USER_SHARED_DATA.ActiveConsoleId.
    volatile ULONG ActiveConsoleId;                 // 2D8 ◷👋 sort of changeable by physically present users

    // Force-dismounting volumes makes affected handles refer to "invalid" files/volumes/directories; if app wants to
    // ensure handles "validity" for some reason (race condition notwithstanding), but doesn't want to always issue
    // FSCTL_IS_VOLUME_MOUNTED ioctl (0x090028), it can simply check sameness of this field.
    // OS changes this value – interlocked-increments it – on two occasions:
    // 1) well-behaved filesystem driver invoked exported nt!FsRtlDismountComplete;
    // 2) OS received FSCTL_DISMOUNT_VOLUME (0x090020) via NtFsControlFile/NtDeviceIoControl (+=1 or +=2 per call).
    volatile ULONG DismountCount;                   // 2DC ◷👋 changes at runtime on dismounts (rare), +manually

    // Lazy-mirrors HKLM\SOFTWARE\Microsoft\.NETFramework₄Enable64Bit. Value is a bitfield with only bit0 defined:
    // COMPLUS_ENABLE_64BIT. When set, it makes system run suitable 32-bit MSIL images as native 64-bit processes (so
    // one can observe 32-bit PE images run as 64-bit processes). Registry value is normally 1, but this field initially
    // set to UINT_MAX, making engaged code use NtQuerySystemInformation(SystemComPlusPackage) to query reg value and
    // update this field. NtSet(SystemComPlusPackage) updates registry and this field, but needs registry write access.
    ULONG ComPlusPackage;                           // 2E0 ◷👋♻ normally changes once at runtime; manually adjustable

    // Snapshot of GetTickCount() ms at the moment of the last user input, across all terminal sessions (including RDP).
    // Used for e.g. idle detection. Updated by win32kbase!CitpLastInputUpdate at most *once per second*.
    // Settable in kernel mode via RtlSetSystemGlobalData(GlobalDataIdLastSystemRITEventTickCount[=13]).
    ULONG LastSystemRITEventTickCount;              // 2E4 ❕👋 updates every second as long as some users provide input

    // OS-visible total RAM size, in pages, clamped to UINT_MAX (16 TB RAM). Since win11 24H2, extended 64-bit field is
    // also available: 🡓FullNumberOfPhysicalPages. Both fields can change if RAM is added or removed.
    // Be aware: often 1-24 MB less than the actual RAM (sum of smbios memory devices), likely due to uefi hiding some.
    ULONG NumberOfPhysicalPages;                    // 2E8 ◷ fixed at boot, but might [rarely] change at runtime

    // True if booted in safe boot mode ("SAFEBOOT:" present in the OS load options).
    BOOLEAN SafeBootMode;                           // 2EC 𝍌

    union
    {
        // Copy of nt!KiVirtFlags, made in KiInitializeKernel based on MSR_IA32_FEATURE_CONTROL and/or VM_CR MSR.
        // bit0: vmx/svm enableable, bit1: enableablement locked (MSR_IA32_FEATURE_CONTROL.lock is true). Bits are 0
        // when: Hyper-V is running (regardless of partition); or VMX is off (in bios, or VM VBS-compatibility off).
        // Bits form mask 3 or 1 when: Hyper-V is NOT running, and VMX is on (in bios, or VM VBS-compatibility ON).
        UCHAR VirtualizationFlags;                  // 2ED 𝍌
#if defined(_M_ARM64)
        // Set during boot to exact copy of byte LoaderBlock.Extension.VirtualizationFlags.
        struct
        {
            UCHAR ArchStartedInEl2: 1;
            UCHAR QcSlIsSupported: 1;
            UCHAR: 6;
        };
#endif
    };

    // Zero. "Available for reuse".
    UCHAR Reserved12[2];                            // 2EE 𝍌♻

    // Various system state flags, SHARED_GLOBAL_FLAGS_*. System adjusts them using interlocked operations.
    // Settable in kernel mode via RtlSetSystemGlobalData(GlobalDataIdSharedDataFlags[=14]) in a special way:
    // bit *index* is bits [0..29] of the input dword; bit 30 to *set* the bit, and/or bit31 to *clear* the bit.
    union
    {
        ULONG SharedDataFlags;                      // 2F0 ◷👋 certain flags may change at runtime
        struct
        {
            // Process with SetTcb privilege can (re-)register one global alpc error port via SystemErrorPortInformation
            // system infoclass (-> nt!DbgkRegisterErrorPort). When that happens, system sets this bit. When registrar
            // process exits, or if port somehow disconnects, system unregisters port and clears this bit. In practice,
            // this bit indicates whether WerSvc is currently running (it registers \WindowsErrorReportingServicePort).
            // Note processes in silo can register error port too, but it'll be silo-specific; this bit won't be set.
            ULONG DbgErrorPortPresent       : 1;    //  0/0001 ◷👋

            // Following 3 flags, together with new 🡓DbgShadowAdminEnabled, form basis for RTL_ELEVATION_FLAGS struct,
            // returned by RtlQueryElevationFlags api (in both usermode and kernelmode). Fields set on boot from reg
            // data at HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System, they won't update until reboot
            // even if registry values change. Bad type or size of reg data, or a missing value, yields 1 (not 0).
            // However, if CCS\Control\LsaInformatiion₄UACInstalled is 0, all 4 flags will be set to 0.
            // 
            // policy: "UAC: Turn on Admin Approval Mode", aka "UAC: Run all administrators in Admin Approval Mode".
            ULONG DbgElevationEnabled       : 1;    //  1/0002 𝍌, reg value₄: "EnableLUA"
            // policy: "UAC: Virtualize file and registry write failures to per-user locations".
            ULONG DbgVirtEnabled            : 1;    //  2/0004 𝍌, reg value₄: "EnableVirtualization"
            // policy: "UAC: Detect application installations and prompt for elevation".
            ULONG DbgInstallerDetectEnabled : 1;    //  3/0008 𝍌, reg value₄: "EnableInstallerDetection"

            // Indicates if Last Known Good is enabled. This bit mirrors nt!CmpLKGEnabled, initialized at boot to
            // CCS\Control\Session Manager\Configuration Manager\LastKnownGood₄Enabled. Most often it's 0.
            // This bit is NOT directly related to "DisableLKG" reg value₄ set by NtDisableLastKnownGood.
            ULONG DbgLkgEnabled             : 1;    //  4/0010 𝍌

            // Indicates if new processors can be added at runtime. This bit mirrors exported "almost read-only" value
            // nt!KeDynamicPartitioningSupported, initialized at boot; value depends on sku and licensing. Normally
            // it's 0 for client systems, and can be 1 for servers. However: it's always zero in Hyper-V root partition.
            ULONG DbgDynProcessorEnabled    : 1;    //  5/0020 𝍌

            // Dynamic value, managed by ConDrv.sys (the console driver). When true, console attach/allocation routines
            // in usermode take different road. Normally value is 0. But if any process with SeTcb privilege asks for
            // brokerage via request to \Device\ConDrv\Broker, this bit becomes 1 (until all broker objects are gone).
            ULONG DbgConsoleBrokerEnabled   : 1;    //  6/0040 👋

            // True when SecureBoot is enabled. Initialized during boot. Matches simultaneously set value in the
            // volatile "State" subkey: CCS\Control\SecureBoot\State₄UEFISecureBootEnabled.
            ULONG DbgSecureBootEnabled      : 1;    //  7/0080 𝍌

            // Indicates that OS supports multiple sessions. For regular OS it's always 1, even for "single-user sku".
            // It's 0 only for Hyper-V docker containers; even then, OS still uses separate session for user processes.
            // Cleared bit entails serious security lax across OS (user ⥵ admin) due to "WIN://ISMULTISESSIONSKU"
            // conditional ACEs (mainly for registry keys), and regular checks in both modes via RtlIsMultiSessionSku.
            // Bit is zeroed only if: CCS\Control\Session Manager₄NumberOfInitialSessions < 2 (default 2), AND
            // "ext-ms-win-session-wtsapi32-l1-1-0" apiset fails to resolve to proper dll.
            // Silo-aware: ntdll!RtlIsMultiSessionSku, SILO_USER_SHARED_DATA.IsMultiSessionSku.
            ULONG DbgMultiSessionSku        : 1;    //  8/0100 𝍌

            // Probably indicates that multiple users can share a session (lightweight user separation?). Often gets
            // checked when 🡑DbgMultiSessionSku is 0. Set at boot to mirror nt!RtlpMultiUsersInSessionSupported,
            // from CCS\Control\Session Manager₄MultiUsersInSessionSupported. Default is 0.
            // Accessible via exported ntdll!RtlIsMultiUsersInSessionSku.
            ULONG DbgMultiUsersInSessionSku : 1;    //  9/0200 𝍌

            // Indicates if state separation is enabled. It's hard to enable it for a regular OS, so normally it's 0.
            // State separation is a facility to use different, configurable paths to some registry hives, some
            // registry keys, and some files. This bit set at boot time to mirror nt!CmStateSeparationEnabled, from
            // CCS\Control\StateSeparation\Policy₄Enabled.
            ULONG DbgStateSeparationEnabled : 1;    // 10/0400 𝍌

            // Relatively new flag, even though concept of split token itself is old.
            // Likely requires at least win11 25H2. Not set in win11 24H2 and before.
            ULONG DbgSplitTokenEnabled      : 1;    // 11/0800 𝍌

            // Part of RTL_ELEVATION_FLAGS.
            // Likely requires at least win11 25H2. Not set in win11 24H2 and before.
            ULONG DbgShadowAdminEnabled     : 1;    // 12/1000 𝍌, reg value: "TypeOfAdminApprovalMode"

            ULONG SpareBits                 : 19;   // 13/~1FFF 𝍌♻
        } DUMMYSTRUCTNAME2;
    } DUMMYUNIONNAME2;

    // Zero.
    ULONG DataFlagsPad[1];                          // 2F4 𝍌♻

    // On x64 contains 0xC3 ("ret"), 0 on ARM64. 32-bit x86 code can jump here to check if DEP is enabled: this page is
    // not executable, but if DEP is effectively off, OS will remove its NX bit for the process on exec attempt, sparing
    // the app STATUS_ACCESS_VIOLATION. That won't affect 64-bit processes: they implicitly have DEP enabled, always.
    ULONGLONG TestRetInstruction;                   // 2F8 𝍌♻

    // Frequency of the high-resolution counter, ntdll!RtlQueryPerformanceCounter() and nt!KeQueryPerformanceCounter().
    // Value from such counter is known simply as "Qpc". 🡗QpcFrequency = (Qpc₁ - Qpc₀), where (t₁ - t₀) == 1 s.
    // 
    // What counter is actually used determined by the _REGISTERED_TIMER struct pointed to by nt!HalpPerformanceCounter.
    // Timer type is normally TimerProcessor (rdtsc/TSC_DEADLINE_MSR) [or TimerHypervisor, or TimerGit, ⩯ rdtsc].
    // For TimerProcessor OS scales tsc values used for Qpc to 10 MHz == 10⁷ Hz == 0x989680 (since win10 1809).
    // For TimerHypervisor the frequency simply set to 10 MHz in the first place. Thus 0x989680 is what you'd normally
    // see there. Duration of each Qpc tick in such case is, naturally, 10⁻⁷ seconds – exactly one centum (100 ns).
    // This field gets set once at boot time together with various other 🡓Qpc* fields, in nt!KiSetupTimeIncrement.
    LONGLONG QpcFrequency;                          // 300 𝍌

    // Normally 0. Contains 1 if int2E is preferable to syscall (x64 only). Set to 1 when: nt!KiSystemCallSelector
    // AND  NtQuery(SystemIsolatedUserModeInformation).HvciEnabled  AND  cpuid(0x40000004).eax.UseIntForMbecSystemCalls.
    // Note int2E IDT entry is special: its DPL is 0 (disallowed for usermode) when nt!KiSystemCallSelector == 0. And
    // the latter mirrors the LoaderBlock.Extension.VsmConfigured bit (hypercall code page for VSM mapped by winload).
    ULONG SystemCall;                               // 308 𝍌

    // Zero. "Reserved field – do not use. Used to be UserCetAvailableEnvironments".
    ULONG Reserved2;                                // 30C 𝍌♻

    // OS-visible total RAM size, in pages. For comparison, 🡑NumberOfPhysicalPages holds 32-bit value of such, clamped
    // to UINT_MAX (16 TB RAM). Both values can change if RAM is added or removed; this larger field is updated first.
    // Be aware: often 1-24 MB less than the actual RAM (sum of smbios memory devices), likely due to uefi hiding some.
    // ⚠️ WARNING ⚠️: field available since win11 24H2. On previous systems this location contains 0.
    ULONGLONG FullNumberOfPhysicalPages;            // 310 ◷ fixed at boot, but might [rarely] change at runtime

    // Zero. "Available for reuse".
    ULONGLONG SystemCallPad[1];                     // 318 𝍌♻

    // Number of osticks since boot, incremented with fixed-at-boot frequency. This value is NOT ms, it's "osticks",
    // which can be translated into ms (most often single ostick is 15.625 ms); see 🡑TickCountMultiplier.
    // Value updated by the clock owner processor, together with 🡑InterruptTime (just usually not as often). And just
    // like 🡑InterruptTime, this value includes sleep/hibernation time and the like (i.e. it jumps forward on wakeup).
    // Coherence of this field with 🡑SystemTime, 🡑InterruptTime, and certain others ensured via 🡓TimeUpdateLock.
    // 
    // ⚠️ To change initial value of this field, set CCS\Control\Session Manager\Executive₄TickcountRolloverDelay to
    // the NEGATIVE desired time, in ms. E.g. to start from ≈8 osticks, set reg data to -125 ms (0xFFFF'FF83); that'll
    // also set 🡑InterruptTime and 🡓InterruptTimeBias initial values to 1250000. Adjustable range: up to 49.71 days.
    union
    {
        volatile KSYSTEM_TIME TickCount;
        volatile ULONG64 TickCountQuad;             // 320 ❕ incremented by one every 15.625 ms (virtually all systems)
        struct
        {
            ULONG ReservedTickCountOverlay[3];
            ULONG TickCountPad[1];                  // 32C 𝍌♻
        } DUMMYSTRUCTNAME;
    } DUMMYUNIONNAME3;

    // Cookie for encoding usermode pointers system-wide. Not related to the stack GS cookie, nor to the ProcessCookie
    // infoclass. Exported ntdll!RtlEncodeSystemPointer uses this field: encoded_ptr = rotr(orig_ptr ^ Cookie, Cookie).
    // Set once per boot to a good random value, on the first usermode thread creation, in nt!PspNotifyThreadCreation.
    ULONG Cookie;                                   // 330 𝍌

    // Zero. Could have been higher part of the cookie to encode more bits, but unfortunately this field is unused.
    ULONG CookiePad[1];                             // 334 𝍌♻

    // Process ID (pid) of the process with focus in the current physical console. RDP sessions ignored. Edge cases when
    // value is zero: Windows Sandbox (as it's RDP), and Hyper-V docker containers (as they are gui-less, so no focus).
    // Hyper-V Manager *enhanced* sessions are RDP too, in such sessions you'll observe some "leftover" value, normally
    // the pid of the LogonUI.exe running in the "physical" *basic* session. Similar to 🡑ActiveConsoleId.
    // When the physical box (or its equivalent) is locked, focused app is normally LogonUI.exe; pid here reflects that.
    // ⚠️ Process death is not tracked – there might be brief periods when this field contains id of an already
    // terminated process, or even id of some new, unrelated process due to pid reuse (very brief and rare).
    // To set this field win32kfull.sys uses dedicated exported api: nt!RtlSetConsoleSessionForegroundProcessId.
    // Silo-aware: RtlGetConsoleSessionForegroundProcessId, SILO_USER_SHARED_DATA.ConsoleSessionForegroundProcessId.
    volatile LONGLONG ConsoleSessionForegroundProcessId;    // 338 ❕👋 physical user controls it; 🐞 added "volatile"

    // Sequence number/lock for time-related fields.
    // When value is odd, set of fields is being updated. See "Cross-fields coherence via sequence numbers" below for
    // details. List of protected fields, in currently utilized update order (not everything listed is always updated):
    // 🡑SystemTime, 🡑InterruptTime, 🡓BaselineSystemTimeQpc, 🡓BaselineInterruptTimeQpc , [🡑TickCountQuad].
    // And on the rare "time-only" codepath we have slightly different update order and 2 more fields:
    // 🡓BaselineSystemTimeQpc, 🡑SystemTime, 🡓QpcSystemTimeIncrement, 🡓QpcSystemTimeIncrementShift.
    volatile ULONGLONG TimeUpdateLock;              // 340 ❕ changes twice each clock interrupt; 🐞 added "volatile"

    // Value retrieved via nt!KeQueryPerformanceCounter() right before the 🡑SystemTime field update, and used to
    // compute new value of 🡑SystemTime. Associated subfractional parts accumulator: nt!KiSystemTimeErrorAccumulator.
    volatile ULONGLONG BaselineSystemTimeQpc;       // 348 ❕ updates together with 🡑SystemTime; 🐞 added "volatile"

    // Value retrieved via nt!KeQueryPerformanceCounter() right before the 🡑InterruptTime field update, and used to
    // compute new value of 🡑InterruptTime. Since on the "system tick" codepath 🡑InterruptTime and 🡑SystemTime are
    // updated together, this field most often holds very same Qpc value as 🡑BaselineSystemTimeQpc.
    // Associated subfractional parts accumulator: nt!KiInterruptTimeErrorAccumulator.
    volatile ULONGLONG BaselineInterruptTimeQpc;    // 350 ❕ updates together with 🡑InterruptTime; 🐞 added "volatile"
    
    // Fractional part of the Multiplier for computing new 🡑SystemTime: SystemTime += QpcDelta × Multiplier.
    // This field might change at runtime to speedup/slowdown the clock; that avoids sudden time jumps during timesync.
    // Such clockrate change does NOT affect performance: rate of 🡑InterruptTime and osticks/GetTickCount is constant.
    // It's common to see value 0x8000'0000'0000'0000 here; with fixed scaler of -0x40 that's effectively 0.5.
    // See "Time updates via Qpc deltas and increments" below for details on the System Time computation.
    ULONGLONG QpcSystemTimeIncrement;               // 358 ◷ might change at runtime for a bit (supposedly rare)

    // Fractional part of the Multiplier for computing new 🡑InterruptTime: InterruptTime += QpcDelta × Multiplier.
    // Set once during boot, in nt!KiSetupTimeIncrement. Remains constant afterwards.
    // It's common to see value 0x8000'0000'0000'0000 here; with fixed scaler of -0x40 that's effectively 0.5.
    // See "Time updates via Qpc deltas and increments" below for details on the Interrupt Time computation.
    ULONGLONG QpcInterruptTimeIncrement;            // 360 𝍌

    // Extra scaling bits for computing new 🡑SystemTime; scaler = -0x40 + 🡗QpcSystemTimeIncrementShift.
    // Just like with 🡑QpcSystemTimeIncrement, this field *might change* at runtime to speedup or slowdown the clock.
    // It's common to see value 1 here; when const-scaled 🡑QpcSystemTimeIncrement is effectively 0.5, these two
    // fields basically cancel each other out. See "Time updates via Qpc deltas and increments" below for details.
    UCHAR QpcSystemTimeIncrementShift;              // 368 ◷ might change at runtime for a bit (supposedly rare)

    // Extra scaling bits for computing new 🡑InterruptTime; scaler = -0x40 + 🡗QpcInterruptTimeIncrementShift.
    // Just like with 🡑QpcInterruptTimeIncrement, this field *set once* during boot, in nt!KiSetupTimeIncrement.
    // It's common to see value 1 here; when const-scaled 🡑QpcInterruptTimeIncrement is effectively 0.5, these two
    // fields basically cancel each other out. See "Time updates via Qpc deltas and increments" below for details.
    UCHAR QpcInterruptTimeIncrementShift;           // 369 𝍌

    // Number of "powered on" [logical] processors. Each SMT core counts as a separate processor.
    // This value can swing a lot at runtime as OS parks CPUs to save power. Always ≤ 🡓ActiveProcessorCount.
    // Most often used to avoid spins in locks when there's only one running processor (by user and kernel mode alike).
    volatile USHORT UnparkedProcessorCount;         // 36A ❕ may change a lot at runtime; 🐞 added "volatile"

    // Bitmask of enclave features supported on this system. Used by ntdll!RtlIsEnclaveFeaturePresent.
    // Out of the whole 128-bit value, only 3 bits seem to be currently defined.
    // bit1/bit2: SGX1/SGX2 leaf funcs enabled (and locked in that state).
    // bit8: 1 if LoaderBlock->Extension.IumEnabled (can be 1 in root and non-root partitions; 0 if Hyper-V is off).
    ULONG EnclaveFeatureMask[4];                    // 36C 𝍌♻

    // Current coverage round for telemetry based coverage (sequence number).
    // Set to 1 at boot in nt!EtwpInitializeCoverage – and most of the time stays like that. One way to increment this
    // value: end the coverage round via NtSetInformationProcess(ProcessTelemetryCoverage, {.LastCoveredRound=-4});
    // however, that needs enabled Administrators group in client's token.
    ULONG TelemetryCoverageRound;                   // 37C 👋

    // Used for ETW UMGL (user-mode global logging). Indices are ETW_UMGL_INDEX_* constants (see nt!EtwpUmglProviders):
    // ETW_UMGL_INDEX_HEAP = 0 (nt!HeapGuid), ETW_UMGL_INDEX_CRITSEC = 1 (nt!CritSecGuid), etc.
    // Each USHORT is actually a 2-byte ETW_UMGL_KEY structure: byte0 is LoggerId, byte1 is "MatchAnyKeyword" Flags.
    // NtTraceControl(EtwSendDataBlock) -> ... -> nt!EtwpEnableDisableSpecialGuids() -> nt!EtwpEnableDisableUMGL().
    // Silo-aware: SILO_USER_SHARED_DATA.UserModeGlobalLogger. See ETW_UMGL_* macro and defines for more.
    USHORT UserModeGlobalLogger[0x10];              // 380 👋 limited adjustability, specific conditions required

    // When bit0 is set, "GlobalFlag" bits FLG_APPLICATION_VERIFIER|FLG_HEAP_PAGE_ALLOCS (0x0200'0100) will be read
    // from HKCU IFEO (as long as both flags🡕 absent in HKLM IFEO, and it's not a secure process). These two verifier
    // bits are read by ntdll during process init, saved in PEB.GlobalFlags.
    // This field does NOT affect other IFEO values or GlobalFlag bits; they're still read from HKLM and PE LoadConfig.
    // Bit0 initialized during boot in nt!VerifierInitSystem, from bit0 of nt!ViImageExecutionOptions (in turn, from
    // CCS\Control\Session Manager₄ImageExecutionOptions). This entire field can be adjusted at runtime by clients with
    // SeTcb privilege, via NtSetSystemInformation(SystemImageFileExecutionOptionsInformation).
    ULONG ImageFileExecutionOptions;                // 3A0 👋♻ changeable at runtime (but normally static)

    // Sequence number of the nt!MUIRegistryInfo structure, which holds UI languages info. Starts at 0 during boot.
    // Only changes when usermode calls NtGetMUIRegistryInfo(Flags |= 8); that increments this field, and also assigns
    // updated value to nt!MUIRegistryInfo.Generation (when nt!MUIRegistryInfo exists). Normally the first and only
    // increment is done by the first Winlogon.exe. No rights nor privileges required to perform such increment.
    ULONG LangGenerationCount;                      // 3A4 👋 changeable at runtime (but mostly static)

    // Zero. "Available for reuse".
    ULONGLONG Reserved4;                            // 3A8 𝍌♻

    // Under certain conditions (e.g. after hibernation), OS makes 🡑InterruptTime to jump forward (OS "biases" it).
    // This field accumulates all such adjustments, enabling clients to get unadulterated Interrupt Time.
    // To get such unadultered Unbiased Interrupt Time, take 🡑InterruptTime, and subtract 🡗InterruptTimeBias from it.
    // 
    // ⚠️ Field is NOT protected via 🡑TimeUpdateLock. To ensure coherence between this field and 🡑InterruptTime,
    // read this value first, then 🡑InterruptTime, then this value again – and check it hasn't changed.
    // Note ntdll!RtlQueryUnbiasedInterruptTime does a bit more: it wraps that sequence into a pair of reads of exported
    // ntdll!RtlpFreezeTimeBias [where OS accumulates Deep Freeze time for current process], and subtracts that too.
    //
    // Updated on these paths:
    // 1) nt!KeAdjustInterruptTime. Mostly on exit from sleep/hibernate; also if "TickcountRolloverDelay" 🡑 used.
    // 2) nt!KiAdjustTimersAfterDripsExit. DRIPS is Deepest Runtime Idle Platform State. Tricky: only increments
    // if OS spent more than nt!KeTimerRebaseThresholdOnDripsExit consecutive seconds in the current DRIPS state.
    // That var is from CCS\Control\Power₄TimerRebaseThresholdOnDripsExit; by default it's 45 seconds.
    volatile ULONGLONG InterruptTimeBias;           // 3B0 ◷👋 rare updates on power events; "manual" via timed sleep

    // Somewhat similar to 🡑InterruptTimeBias. Accumulates bias for the Qpc value. But there's important difference:
    // 🡑InterruptTime already incorporates bias, so client-oriented api RtlQueryUnbiasedInterruptTime has to *subtract*
    // 🡑InterruptTimeBias; but raw Qpc value does NOT incorporate bias, so RtlQueryPerformanceCounter has to *add*
    // 🡗QpcBias! Yes, it's almost like OS devs mixed up bias inclusion cases to do some extra math on hot codepaths.
    //
    // Unit is 🡑QpcFrequency⁻¹ seconds. When nt!HalpPerformanceCounter type is Processor or Hypervisor,
    // frequency is 10 MHz; making the unit exactly one centum (100 ns), same as 🡑InterruptTimeBias.
    // Updated in nt!HalpTimerPropagateQpcBiasUpdate, on rare power-related events, like sleep/hibernation.
    // For TimerHypervisor and TimerGit, bias value comes directly from REGISTERED_TIMER.TimeBias. For TimerProcessor
    // that same TimeBias field is scaled to 10 MHz first.
    // Settable in kernel mode via RtlSetSystemGlobalData(GlobalDataIdQpcBias[=18]).
    volatile ULONGLONG QpcBias;                     // 3B8 ◷👋 rare updates on power events; "manual" via timed sleep

    // Number of [logical] processors in the system. Each SMT core counts as a separate processor. Field name is mildly
    // confusing (and digging deeper only makes it worse). Value mirrors unexported nt!KeNumberProcessors; don't mistake
    // it for the *exported* "KeNumberProcessors", which is actually nt!KeNumberProcessorsGroup0 variable (¿⸮?).
    // Also don't mix it up with nt!KeMaximumProcessors🡖, nor with nt!KeActiveProcessors (set of KAFFINITY_EX masks).
    // ⮞ TLDR: just drop "Active" from the name. Use 🡑UnparkedProcessorCount for count of CPUs actually running atm.
    // Field set during boot. On some server SKUs you can add CPUs dynamically: on such systems this value may increase
    // at runtime. But it will never decrease, and will never exceed nt!KeMaximumProcessors during current boot session.
    // Absolute max # of processors: ws2022/win11: 0x800 (2048) [confirmed 24H2]; win10 22H2: 0x500 (1280).
    volatile ULONG ActiveProcessorCount;            // 3C0 ◷ rare increments at runtime possible; 🐞 added "volatile"

    // Number of processor groups in the system. Mirrors nt!KiActiveGroups.
    // On some server SKUs you can add CPUs dynamically: on such systems this value may increase at runtime.
    // Note you can force-split CPUs into multiple groups on boot: "bcdedit /set GroupSize 2" to get N groups with 2
    // CPUs each. Absolute max # of CPU groups for any OS is 0x20 (32) [confirmed 24H2].
    volatile UCHAR ActiveGroupCount;                // 3C4 ◷ rare increments possible

    // Zero. "Available for reuse".
    UCHAR Reserved9;                                // 3C5 𝍌♻

    // Modern OS treats this union as bitmask/flags governing ntdll!RtlQueryPerformanceCounter() behavior.
    // See SHARED_GLOBAL_FLAGS_QPC_BYPASS_* flags. Only 7 bits are in use, all overlaid with 🡗QpcBypassEnabled byte.
    //   0/0001: _ENABLED: usermode code can bypass NtQueryPerformanceCounter syscall, retrieve Qpc perfcounter by
    //     transforming rdtsc/rdtscp value or ARM64_CNTVCT_EL0 register. When this bit is 0, all others are zeroed too.
    //     On x86 you can force bit to 0 with "bcdedit /set UsePlatformClock yes" (don't mixup with "UsePlatformTick").
    //   1/0002: _USE_HV_PAGE: use bias and multiplier from HV_REFERENCE_TSC_PAGE struct (aka "huser", the page you get
    //     via SystemHypervisorSharedPageInformation infoclass). It's the most common case; hypervisor is NOT required.
    //   2/0004: _DISABLE_32BIT: 32-bit code (wow64) should not attempt to bypass the syscall.
    //   3/0008: – unused.
    //   4/0010: _USE_MFENCE: "mfence" instruction before rdtsc. For AMD CPUs where rdtscp can't be used.
    //           Kernel mode may use (KPRCB.CpuVendor == CPU_AMD) instead. But rdtscp (bit7 🡓) always outweighs it.
    //   5/0020: _USE_LFENCE: "lfence" instruction before rdtsc. For Intel CPUs where rdtscp can't be used.
    //           Kernel mode may use (KPRCB.CpuVendor == CPU_INTEL) instead. But rdtscp (bit7 🡓) always outweighs it.
    //   6/0040: _A73_ERRATA: read ARM64_CNTVCT_EL0 twice (barrier'd); if bit32 changed, use the first reading.
    //   7/0080: _USE_RDTSCP: instead of rdtsc, use [partially serializing] "rdtscp". For CPUs since Nehalem.
    //           Kernel mode may disregard it and use 🡑ProcessorFeatures[PF_RDTSCP_INSTRUCTION_AVAILABLE] instead.
    // 
    // Severely simplified pseudocode for qpc retrieval in RtlQueryPerformanceCounter (assuming syscall bypass enabled):
    //   tsc = rdtsc()   [or rdtscp(), or ReadStatusReg(ARM64_CNTVCT_EL0)]
    //   qpc = kuser.QpcBias + (kuser.QpcData & _USE_HV_PAGE)? tsc × huser.TscScale × 2⁻⁶⁴ + huser.TscOffset: tsc
    union
    {
        // Entire field settable in kernel mode via RtlSetSystemGlobalData(GlobalDataIdQpcData[=17]).
        USHORT QpcData;                             // 3C6 ◷
        struct
        {
            // Bitflags governing ntdll!RtlQueryPerformanceCounter() behavior, described above.
            // On old OS [before win10 1709, RS3] it was a bool, that role is now taken by bit0.
            // This byte settable in kernel mode via RtlSetSystemGlobalData(QpcBypassEnabled[=16]).
            volatile UCHAR QpcBypassEnabled;        // 3C6 ◷ won't change; except miiight on OS live migration

            // Zero. Unused on modern OS. On old OS [before win10 1709, RS3] it was used as a bitshift value for the
            // raw perfcounter: ntdll!RltQueryPerformanceCounter() => (rdtsc() + 🡑QpcBias) >> 🡗QpcShift [before 1709].
            // But that made Qpc rate very different across systems; nowadays OS uses much more precise scaling.
            UCHAR QpcShift;                         // 3C7 𝍌♻
        };
    };

    // Pair (🡗TimeZoneBiasEffectiveStart, 🡗TimeZoneBiasEffectiveEnd) form a range for 🡑SystemTime when
    // 🡑TimeZoneBias is valid. That is, if 🡑SystemTime is in that range, LocalTime = (🡑SystemTime - 🡑TimeZoneBias).
    // That's true regardless of DST (it's already included in 🡑TimeZoneBias). If both range ends are 0, the range
    // spans *all* time. For time outside the range, local time has to be computed manually.
    // Fields can be updated at runtime (e.g. when range end is reached, or timezone changed).
    // Coherence in relation to 🡑TimeZoneBias during fields update ensured via 🡑TimeZoneBiasStamp.
    // Silo-aware: SILO_USER_SHARED_DATA.TimeZoneBiasEffectiveStart, SILO_USER_SHARED_DATA.TimeZoneBiasEffectiveEnd.
    // 
    // Normally, 🡗TimeZoneBiasEffectiveStart is equal to the snapshot of 🡑SystemTime at one of these moments:
    // a) system boot + 5..15 seconds; b) system date/time change; c) timezone change; d) crossing the DST line (i.e.
    // 🡑SystemTime reached 🡗TimeZoneBiasEffectiveEnd, so the new range has to be established).
    // 🡗TimeZoneBiasEffectiveEnd updated together with 🡗TimeZoneBiasEffectiveStart. It's set to either the next DST
    // line or to (end of year + 🡑TimeZoneBias), whichever is earlier.
    // Adjustable – within a certain amount – by clients with SeTimeZone privilege, together with 🡑TimeZoneBias.
    LARGE_INTEGER TimeZoneBiasEffectiveStart;       // 3C8 ◷👋
    LARGE_INTEGER TimeZoneBiasEffectiveEnd;         // 3D0 ◷👋

    // Extended processor state configuration.
    // Initialized once at boot in nt!KiInitializeXSaveConfiguration, based on features actually supported by cpu,
    // and features disabled via LoaderBlock ("bcdedit /set xsaveDisable|xsavePolicy|xsaveRemoveFeature"). Since
    // win11 24H2, ARM64 oskernel tries to ignore this field, uses its own 🡓XStateArm64 instead. But even though ARM64
    // doesn't init it, XState.EnabledFeatures still used sometimes (e.g. nt!PopHandleNextState) due to bugs/leftovers.
    XSTATE_CONFIGURATION XState;                    // 3D8 𝍌♻ used now, but really should not be in kuser

    // Mirrors global value read via exported nt!RtlQueryFeatureConfigurationChangeStamp (part of nt!CmFcSystemManager).
    // Starts at 1 at boot, increments each time feature config changes. However, there is so called
    // "SwapReferenceIndex" (RtlGetSwapReferenceIndex), changing which might bring in parallel global value.
    // This field is what's referred to as RTL_FEATURE_CHANGE_STAMP/ChangeStamp in structures for
    // NtSetSystemInformation(SystemFeatureConfigurationInformation). Note these are NOT "Optional Windows Features";
    // rather these are A/B features (and ongoing security fix "features"), adjustable via e.g. opensource ViveTool.
    // ⚠️ Size of 🡑XState increased by 0x10 in WS2022, changing this field offset from 0x710 to 0x720.
    KSYSTEM_TIME FeatureConfigurationChangeStamp;   // 720; offset is 0x710 on win10 22H2 and earlier OS

    // Zero.
    ULONG Spare;                                    // 72C 𝍌♻

    // Mirrors nt!KePointerAuthMask. Only used for ARM64, zero on x64. Initialized once at boot.
    // Contains a mask to apply to a pointer value to extract authentication "PAC" bits together with a sign
    // bit (highest bit preceding the PAC). If PAC is not used, or PAC size is not exactly 8 bits, value is simply
    // zero (confirmed win11 24H2 and earlier). So the only values possible are 0 and 0xFF80'0000'0000'0000 [2025-08].
    UINT64 UserPointerAuthMask;                     // 730 𝍌 available since win11 22H2

    // Following fields are there since win11 24H2.
#ifdef _M_ARM64
    // Extended processor state configuration specifically for ARM64.
    // ARM64 OS kernels before win11 24H2 were less greedy and simply used 🡑XState.
    XSTATE_CONFIGURATION XStateArm64;               // 738 𝍌♻ used now, but really should not be in kuser
#else
    // "The reserved space for other architectures is not available for reuse".
    UINT Reserved10[0xD2];                          // 738 𝍌♻
#endif
};  // struct _KUSER_SHARED_DATA, size: 0xA80
```
