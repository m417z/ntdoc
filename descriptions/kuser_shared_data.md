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



## `TickCountLowDeprecated`

| Offset | Sigils |
|--------|--------|
| 0x000 | 𝍌 ♻ |

```cpp
ULONG TickCountLowDeprecated;
```

Unused, deprecated for more than 20 years. Always zero.


## `TickCountMultiplier`

| Offset | Sigils |
|--------|--------|
| 0x004 | 𝍌 |

```cpp
ULONG TickCountMultiplier;
```

Number of milliseconds per ostick, left-shifted by 0x18. Mirrors `nt!ExpTickCountMultiplier`, derived directly from `nt!KeMaximumIncrement`. Across all archs, value is clamped to a max of 0x0FA00000 (1/64 s, or 15.625 ms). And in fact, you'll almost never see anything else there, except maybe 0x0F99A027 on some old systems (~15.600 ms, or 15.600099980831146 ms exactly). `GetTickCount()` => `(🡗TickCountMultiplier × 🡓TickCountQuad) >> 0x18`. Duration of an ostick is fixed at boot time, stored in `nt!KeMaximumIncrement`. Not to be confused with the clock tick duration, `nt!KeTimeIncrement`, which can change at runtime (in 🡓InterruptTime description right below).


## `InterruptTime`

| Offset | Sigils |
|--------|--------|
| 0x008 | ❕ |

```cpp
volatile KSYSTEM_TIME InterruptTime;
```

*changes each clock interrupt*

Number of centums (100 ns units) since system start. Value monotonically increases. Includes sleep/hibernation time and the like (the "bias"); i.e. value jumps forward on wakeup. For raw uptime, subtract 🡓InterruptTimeBias. Updated on each clock interrupt on the clock owner processor. Current update period is `nt!KeTimeIncrement`, adjustable via `NtSetTimerResolution` (aka `timeBeginPeriod`), in the hardcoded range [0.5 ms, 15.625 ms]. Actual adjustable range can be smaller; set at boot as [`nt!KeMinimumIncrement`, `nt!KeMaximumIncrement`]. See 🡓TickCountQuad description on how to change this field initial value from 0 to up to 49.71 days. Coherence of this field vs 🡓SystemTime, 🡓TickCountQuad, and certain others is ensured via 🡓TimeUpdateLock.


## `SystemTime`

| Offset | Sigils |
|--------|--------|
| 0x014 | ❕ 👋 |

```cpp
volatile KSYSTEM_TIME SystemTime;
```

*changes each clock interrupt + adjustable*

UTC System Time. Number of centums since 1601-01-01, exactly. It's a perfectly raw value; any conversions or adjustments (like leap days or leap seconds) ought to be done on the higher level. Coherence of this field vs 🡑InterruptTime, 🡓TickCountQuad, and certain others is ensured via 🡓TimeUpdateLock. Clients not in the server silo with SeSystemtime privilege can set it via `NtSetSystemTime` to any value in range [0, 2⁶¹+2³²), which is [1601-01-01, 8907-12-05 18:49:10].

Note regular users don't have SeSystemtime by default.


## `TimeZoneBias`

| Offset | Sigils |
|--------|--------|
| 0x020 | ◷ 👋 |

```cpp
volatile KSYSTEM_TIME TimeZoneBias;
```

*changes at runtime (~twice a year), manually adjustable*

Current 64-bit time zone bias.

Silo-aware: `SILO_USER_SHARED_DATA.TimeZoneBias`.

It's the value you *subtract* from 🡑SystemTime to get Local Time. It's already pre-adjusted for daylight saving. E.g. for Pacific Time (-08:00) value will be 7:00 in Summer (0x3AAC5ED800 == 7×3600×10⁷). See 🡓TimeZoneBiasEffectiveStart description for when this field is considered valid. Coherence of this field vs the 🡓TimeZoneBiasEffective\* values ensured via 🡓TimeZoneBiasStamp. Clients with SeTimeZone privilege can set bias using `SystemTimeZoneInformation`/`SystemDynamicTimeZoneInformation` infoclasses. Range is ±2³¹ seconds (±68 years), granularity 1 minute. Regular users on client OS versions DO have SeTimeZone privilege by default; on server OS versions they don't.

Note timezone info is stored under `CCS\Control\TimeZoneInformation` key; using timezone infoclasses grants users limited writeability to that key.


## `ImageNumberLow`

| Offset | Sigils |
|--------|--------|
| 0x02C | 𝍌 |

```cpp
USHORT ImageNumberLow;
```

Fixed values, set at boot (in `nt!InitBootProcessor`). Both fields are the same: 0x8664 for x64, 0xAA64 for ARM64. Settable in kernel mode via `RtlSetSystemGlobalData(GlobalDataIdImageNumberLow/GlobalDataIdImageNumberHigh[=4/5])`.


## `ImageNumberHigh`

| Offset | Sigils |
|--------|--------|
| 0x02E | 𝍌 |

```cpp
USHORT ImageNumberHigh;
```

See `ImageNumberLow` above.


## `NtSystemRoot`

| Offset | Sigils |
|--------|--------|
| 0x030 | 𝍌 ♻ |

```cpp
WCHAR NtSystemRoot[0x104];
```

*used now, but really shouldn't be in kuser*

Win32 system root path, e.g. "C:\Windows" – without quotes, without trailing slash. First wchar is adjustable in kernel mode via `RtlSetSystemGlobalData(GlobalDataIdNtSystemRootDrive[=15])`. OS receives path from the osloader (`winload.efi`), in `LoaderBlock.NtBootPathName`. But `LoaderBlock` path has no drive letter, so it's retrieved from the `MountPointManager` via `IOCTL_MOUNTMGR_BOOT_DL_ASSIGNMENT`.

Silo-aware: `RtlGetNtSystemRoot`, `SILO_USER_SHARED_DATA.NtSystemRoot`.


## `MaxStackTraceDepth`

| Offset | Sigils |
|--------|--------|
| 0x238 | 𝍌 ♻ |

```cpp
ULONG MaxStackTraceDepth;
```

"Maximum stack trace depth if tracing is enabled". Appears to be deprecated, unused, always zero.


## `CryptoExponent`

| Offset | Sigils |
|--------|--------|
| 0x23C | 𝍌 ♻ |

```cpp
ULONG CryptoExponent;
```

Crypto exponent for yolocrypto. Unused, always zero. In the past could be non-zero only for "internal" OS builds.


## `TimeZoneId`

| Offset | Sigils |
|--------|--------|
| 0x240 | ◷ 👋 |

```cpp
ULONG TimeZoneId;
```

*changes at runtime ~twice a year, manually adjustable*

Time zone ID, `TIME_ZONE_ID_*`.

Silo-aware: `SILO_USER_SHARED_DATA.TimeZoneId`.

Values:
- 0: \*_UNKNOWN (aka neither, DST not used)
- 1: \*_STANDARD (winter)
- 2: \*_DAYLIGHT (summer)

Settable in kernel mode via `RtlSetSystemGlobalData(GlobalDataIdTimeZoneId[=6])`.

⚠️ Unlike 🡑TimeZoneBias and 🡓TimeZoneBiasEffective\*, this field is NOT protected via 🡓TimeZoneBiasStamp; it is set before starting the 🡓TimeZoneBiasStamp update sequence. For coherence between this and other timezone fields: read this first, then others, then read this field again and ensure it hasn't changed. Indirectly adjustable by clients with SeTimeZone privilege, together with 🡑TimeZoneBias.


## `LargePageMinimum`

| Offset | Sigils |
|--------|--------|
| 0x244 | 𝍌 ♻ |

```cpp
ULONG LargePageMinimum;
```

*used now, but really shouldn't be in kuser*

Minimum size of a large page, in bytes. Determined by the CPU. On boot `nt!MiInitSystem` sets it to hardcoded 2 MB. It seems the only purpose of this field is to simplify implementation of exported `kernelbase!GetLargePageMinimum`.


## `AitSamplingValue`

| Offset | Sigils |
|--------|--------|
| 0x248 | 👋 ♻ |

```cpp
ULONG AitSamplingValue;
```

AIT sampling rate. TL note: AIT means App Impact Telemetry. Related to KIT, Kernel Impact Telemetry. Related to ETW provider `MS_Windows_AIT_Provider` and exported api `nt!KitLogFeatureUsage`. Most likely deprecated. Set during boot in `nt!KitpInitAitSampleRate` from `CCS\Control\Session Manager\AppCompatCache₄Rate`, unless it's a safeboot. By default there is nothing in registry, so normally this field is 0. Can be adjusted by holders of SeProfileSingleProcess privilege: `NtSetSystemInformation(SystemAitSamplingValue)`.


## `AppCompatFlag`

| Offset | Sigils |
|--------|--------|
| 0x24C | 𝍌 ♻ |

```cpp
ULONG AppCompatFlag;
```

"This value controls switchback processing". Seemingly deprecated, unused, and always 0. But there's an active PEB field of similar name: `PEB.AppCompatFlags`.


## `RNGSeedVersion`

| Offset | Sigils |
|--------|--------|
| 0x250 | ◷ |

```cpp
ULONGLONG RNGSeedVersion;
```

*incremented periodically (every hour on average)*

Number of times since boot `CNG.sys` has reseeded its entropy pool. Reseed can be triggered via exported `cng!EntropyPoolTriggerReseedForIum`, but it mostly auto-reseeds at these intervals after the previous auto-reseed, in seconds: 1, 3, 9, 27, 81, 243, 729, 2187, 3600, 3600, 3600,.. I.e. interval triples till it hits one hour (but there's about 5 extra reseeds at system start). On boot you'll often see 8 here; +27s: 9; +81s more: 10; after 6/18/55/115 minutes of uptime: 11/12/13/14; etc. Settable in kernel mode via `RtlSetSystemGlobalData(GlobalDataIdRngSeedVersion[=1])`.


## `GlobalValidationRunlevel`

| Offset | Sigils |
|--------|--------|
| 0x258 | 𝍌 ♻ |

```cpp
ULONG GlobalValidationRunlevel;
```

Set of flags to control assert failures handling. Read on boot from `CCS\Control\ValidationRunLevels₄Global`. See `VRL_*` flags in sdk; from oskernel view the only bit is `VRL_ENABLE_KERNEL_BREAKS`, it only affects debug OS builds.


## `TimeZoneBiasStamp`

| Offset | Sigils |
|--------|--------|
| 0x25C | ◷ 👋 |

```cpp
volatile LONG TimeZoneBiasStamp;
```

*changes at runtime rarely (e.g. daily), +manual adjust*

Sequence number/lock for timezone data: 🡑TimeZoneBias, 🡓TimeZoneBiasEffectiveStart, 🡓TimeZoneBiasEffectiveEnd. When value is odd, the set of fields is being updated. See "Cross-fields coherence via sequence numbers" below for details. Clients without any privileges can increment it by two via `NtSetSystemTime(null, null)`.

Silo-aware: `SILO_USER_SHARED_DATA.TimeZoneBiasStamp`.


## `NtBuildNumber`

| Offset | Sigils |
|--------|--------|
| 0x260 | 𝍌 |

```cpp
ULONG NtBuildNumber;
```

Mirrors exported `nt!NtBuildNumber`, but with its higher nibble zeroed. For `nt!NtBuildNumber`, higher nibble is 0xC in Checked (debug) builds, or 0xF in Free (release) builds. Initially set to a hardcoded value for current `ntoskrnl`, equal to the "real" value in `FixedFileVersionInfo` (e.g. 19041); during boot re-set to a dword from registry (e.g. 19045). This field (or rather the `nt!NtBuildNumber` it's derived from) has modest usage throughout the system, but it does affect codepaths. Goes into `PEB.NtBuildNumber`. Reg path for win10: `HKLM\Software\Microsoft\Windows NT\CurrentVersion\EditionVersion₄EditionBuildNumber`. For WS2022/win11: `HKLM\SYSTEM\Software\Microsoft\BuildLayers\<SubkeyWithValue.IsTopLevel==1>₄BuildNumber`. "The shared collective build number undecorated with C or F." – original WDK gem, kept for posterity.


## `NtProductType`

| Offset | Sigils |
|--------|--------|
| 0x264 | 𝍌 |

```cpp
NT_PRODUCT_TYPE NtProductType;
```

Product type: client (e.g. Windows 10) VS server (e.g. Windows Server 2022) VS domain controller server.

- 1/NtProductWinNt: client OS
- 2/NtProductLanManNt: Windows Server in DC role
- 3/NtProductServer: Windows Server

Set on boot in `nt!MiMemoryLicense`, from `nt!MmRegistryState`.ProductType: `CCS\Control\ProductOptions₄ProductType`.

Silo-aware: `RtlGetNtProductType`, `SILO_USER_SHARED_DATA.NtProductType`.


## `ProductTypeIsValid`

| Offset | Sigils |
|--------|--------|
| 0x268 | 𝍌 ♻ |

```cpp
BOOLEAN ProductTypeIsValid;
```

Tells APIs they can use 🡑NtProductType field instead of querying that info from registry. Normally it's 1, except during system install ("SystemSetupInProgress").


## `Reserved0`

| Offset | Sigils |
|--------|--------|
| 0x269 | 𝍌 ♻ |

```cpp
BOOLEAN Reserved0[1];
```

Zero.


## `NativeProcessorArchitecture`

| Offset | Sigils |
|--------|--------|
| 0x26A | 𝍌 ♻ |

```cpp
USHORT NativeProcessorArchitecture;
```

*shouldn't be in kuser; wow/sxs should use regular api*

`PROCESSOR_ARCHITECTURE_*` constant, e.g. 9 for `PROCESSOR_ARCHITECTURE_AMD64`, 12 for _ARM64.


## `NtMajorVersion`

| Offset | Sigils |
|--------|--------|
| 0x26C | 𝍌 |

```cpp
ULONG NtMajorVersion;
```

OS Version, set at boot to fixed values (in `nt!InitBootProcessor`). E.g. win7: 6 major, 1 minor. Usual values: 5.1, 5.2, 6.0, 6.1, 6.2, 6.3; hardcoded to 10.0 since win10, stays as such in win11. Unlike 🡑NtBuildNumber, adjusting MajorVersion & MinorVersion in registry does NOT affect these fields.


## `NtMinorVersion`

| Offset | Sigils |
|--------|--------|
| 0x270 | 𝍌 |

```cpp
ULONG NtMinorVersion;
```

See `NtMajorVersion` above.


## `ProcessorFeatures`

| Offset | Sigils |
|--------|--------|
| 0x274 | 𝍌 |

```cpp
BOOLEAN ProcessorFeatures[0x40];
```

*0x40 is PROCESSOR_FEATURE_MAX*

Processor and/or OS features. See `PF_*` flags. Unfortunately, one whole byte used per flag. Used by `kernelbase!IsProcessorFeaturePresent` (via `ntdll!RtlIsProcessorFeaturePresent`).

⚠️ Older OS versions may not set all expected flags, even if feature is actually supported by CPU and OS.


## `Reserved1`

| Offset | Sigils |
|--------|--------|
| 0x2B4 | 𝍌 ♻ |

```cpp
ULONG Reserved1;
```

*aka MaximumUserModeAddressDeprecated*

Obsolete, dnu: always 0x7FFEFFFF on 64-bit OS. On 32-bit OS mirrors `MM_HIGHEST_USER_ADDRESS` (sensible with /3GB).


## `Reserved3`

| Offset | Sigils |
|--------|--------|
| 0x2B8 | 𝍌 ♻ |

```cpp
ULONG Reserved3;
```

*aka SystemRangeStartDeprecated*

Obsolete, dnu: always 0x80000000 on 64-bit OS. On 32-bit OS mirrors MmSystemRangeStart.


## `TimeSlip`

| Offset | Sigils |
|--------|--------|
| 0x2BC | 𝍌 ♻ |

```cpp
volatile ULONG TimeSlip;
```

***most likely** fixed at boot to 0 and doesn't change*

"Time slippage while in debugger". So, supposedly "time wasted debugging", but there's strong indication this field is obsolete and always zero.


## `AlternativeArchitecture`

| Offset | Sigils |
|--------|--------|
| 0x2C0 | 𝍌 ♻ |

```cpp
ULONG AlternativeArchitecture;
```

*type is 2-const enum ALTERNATIVE_ARCHITECTURE_TYPE*

Always zero. Previously: "alternative system architecture, e.g., NEC PC98xx on x86".


## `BootId`

| Offset | Sigils |
|--------|--------|
| 0x2C4 | 𝍌 |

```cpp
ULONG BootId;
```

Number of boots since OS install (really, boot attempts). Osloader (`winload.efi`) reads `\Windows\bootstat.dat` (``BSD_BOOT_STATUS_DATA.LastBootId`0x34``), increments and resaves it; passes value through LoaderBlock for `nt!InitBootProcessor`, which stores it here. Filepath is changeable via `BsdLogPath`; `ntoskrnl` reduplicates it from the loader block into `CCS\ControlₛOsBootstatPath`. Hyper-V docker containers run with BootId == 1; at least some Windows Sandbox instances run with BootId == 2.


## `SystemExpirationDate`

| Offset | Sigils |
|--------|--------|
| 0x2C8 | 𝍌 |

```cpp
LARGE_INTEGER SystemExpirationDate;
```

Value of 🡑SystemTime when system expires. Normally 0, which means no expiration. Not related to activation. Evaluation OS versions have real value here. Used by `winver.exe` directly, and by `win32k*.sys` to paint watermark. Set during boot from data returned by `nt!ExGetExpirationDate()` [ZwQueryLicenseValue("Kernel-ExpirationDate")].


## `SuiteMask`

| Offset | Sigils |
|--------|--------|
| 0x2D0 | 𝍌 |

```cpp
ULONG SuiteMask;
```

`VER_SUITE_*` mask, i.e. (1 << `SUITE_TYPE::*`). E.g. if bit16 set, it's Windows Phone (`SUITE_TYPE::PhoneNT` == 16). Over time got sidelined; mostly you'll see just the minimum: 0x110 == `VER_SUITE_TERMINAL`|`VER_SUITE_SINGLEUSERTS`.

Silo-aware: `RtlGetSuiteMask`, `SILO_USER_SHARED_DATA.SuiteMask`.


## `KdDebuggerEnabled`

| Offset | Sigils |
|--------|--------|
| 0x2D4 | ◷ 👋 |

```cpp
UCHAR KdDebuggerEnabled;
```

*may change if debugger connected; manually adjustable*

Kernel Debugger status bitmask. Value can change dynamically into any state (e.g. 1 -> 3 -> 0 -> 3 -> 1 -> ...). Bit0 mirrors exported boolean `nt!KdDebuggerEnabled` (debugger enabled, but not necessarily connected). Bit1 is negation of the exported bool `nt!KdDebuggerNotPresent` (that is: when bit1 is 1, KD is connected/active). 🔎 Example: booted with `bcdedit /debug on`, but w/o KD running: field=1 (enabled, not connected); then launched KD on host: guest OS connects to KD, field changes 1->3 (active); run `kdbgctrl -d` on guest, aka `NtSystemDebugControl(SysDbgDisableKernelDebugger)`: field changes 3->0 (forcing KD disconnect until dbg events). Can also change 0->1/3 with `kdbgctrl` as long as `nt!KdPitchDebugger` is false (i.e. "/debug on" is true). Settable in kernel mode via `RtlSetSystemGlobalData(GlobalDataIdKdDebuggerEnabled[=10])`, done by `kdxxx`/`kdnet.dll`.


## `MitigationPolicies` (in union)

| Offset | Sigils | Context |
|--------|--------|--------|
| 0x2D5 | 𝍌 | Part of union at 0x2D5 |

```cpp
UCHAR MitigationPolicies;
```

Minor subset of system mitigations.


## `NXSupportPolicy` (in struct)

| Context |
|--------|
| Bitfield in struct at 0x2D5 |

```cpp
UCHAR NXSupportPolicy: 2;
```

`NX_SUPPORT_POLICY_*` values. Only meaningful for 32-bit x86 processes. From `bcdedit /set nx VALUE`. Applied at process startup via `NtSetInformationProcess(ProcessExecuteFlags)`.


## `SEHValidationPolicy` (in struct)

| Context |
|--------|
| Bitfield in struct at 0x2D5 |

```cpp
UCHAR SEHValidationPolicy: 2;
```

`SEH_VALIDATION_POLICY_*` values. Only meaningful for 32-bit x86 processes. Set on boot from `CCS\Control\Session Manager₄DisableExceptionChainValidation`. App IFEO value with the same name trumps it.


## `CurDirDevicesSkippedForDlls` (in struct)

| Context |
|--------|
| Bitfield in struct at 0x2D5 |

```cpp
UCHAR CurDirDevicesSkippedForDlls: 2;
```

Determines what kinds of devices are illegal to have Current Working Directory searched for dlls. From `CCS\Control\Session Manager₄CWDIllegalInDLLSearch`. App-specific IFEO value with the same name trumps it.

Values:
- 0: any allowed
- 1: WebDav
- 2: any Remote device
- 3: all devices illegal, never use CWD (-1 in registry)


## `Reserved` (in struct)

| Context |
|--------|
| Bitfield in struct at 0x2D5 |

```cpp
UCHAR Reserved: 2;
```

Zero.


## `CyclesPerYield`

| Offset | Sigils |
|--------|--------|
| 0x2D6 | 𝍌 |

```cpp
USHORT CyclesPerYield;
```

Measured duration of `pause` (x86) or `yield` (ARM) instructions, in TSC (`rdtsc`) cycles. Determines how many times to spin, e.g. in `RtlBackoff` (both rings). Early at boot set to 10, then – at later boot stages – updated with data from `nt!ExpComputeCyclesPerYield`. Example: 0x0D, 0x18, 0x84. Measured values can vary boot to boot! OS clamps value in range [1, 0xFFFF]. So if value is 0, the OS is simply too old to use it: older than win10 1903.


## `ActiveConsoleId`

| Offset | Sigils |
|--------|--------|
| 0x2D8 | ◷ 👋 |

```cpp
volatile ULONG ActiveConsoleId;
```

*sort of changeable by physically present users*

Current physical console Session Id. RDP sessions ignored. During boot it's 0. Right after the boot it may stay 0 (Hyper-V docker container), change to 1 (normal box, Logon Screen), or to -1 (Windows Sandbox, kind of RDP).

Note Hyper-V Manager *basic* sessions are "physical", but *enhanced* sessions are RDP; thus in enhanced sessions you'll observe some "leftover" here, but really it'll be the "physical" basic session `LogonUI.exe` is running in. When the physical box (or its equivalent) is locked, value *may* change; happens when `LogonUI.exe` is created in a new session, which is the case if there are already several user sessions (physical or RDP). Field set by `win32kbase.sys` and `win32kfull.sys`; they use dedicated exported api, `nt!RtlSetActiveConsoleId`.

Silo-aware: `RtlGetActiveConsoleId`, `SILO_USER_SHARED_DATA.ActiveConsoleId`.


## `DismountCount`

| Offset | Sigils |
|--------|--------|
| 0x2DC | ◷ 👋 |

```cpp
volatile ULONG DismountCount;
```

*changes at runtime on dismounts (rare), +manually*

Force-dismounting volumes makes affected handles refer to "invalid" files/volumes/directories; if app wants to ensure handles "validity" for some reason (race condition notwithstanding), but doesn't want to always issue `FSCTL_IS_VOLUME_MOUNTED` ioctl (0x090028), it can simply check sameness of this field. OS changes this value – interlocked-increments it – on two occasions:

1. Well-behaved filesystem driver invoked exported `nt!FsRtlDismountComplete`.
2. OS received `FSCTL_DISMOUNT_VOLUME` (0x090020) via `NtFsControlFile`/`NtDeviceIoControlFile` (+=1 or +=2 per call).


## `ComPlusPackage`

| Offset | Sigils |
|--------|--------|
| 0x2E0 | ◷ 👋 ♻ |

```cpp
ULONG ComPlusPackage;
```

*normally changes once at runtime; manually adjustable*

Lazy-mirrors `HKLM\SOFTWARE\Microsoft\.NETFramework₄Enable64Bit`. Value is a bitfield with only bit0 defined: `COMPLUS_ENABLE_64BIT`. When set, it makes system run suitable 32-bit MSIL images as native 64-bit processes (so one can observe 32-bit PE images run as 64-bit processes). Registry value is normally 1, but this field initially set to `UINT_MAX`, making engaged code use `NtQuerySystemInformation(SystemComPlusPackage)` to query reg value and update this field. `NtSetSystemInformation(SystemComPlusPackage)` updates registry and this field, but needs registry write access.


## `LastSystemRITEventTickCount`

| Offset | Sigils |
|--------|--------|
| 0x2E4 | ❕ 👋 |

```cpp
ULONG LastSystemRITEventTickCount;
```

*updates every second as long as some users provide input*

Snapshot of `GetTickCount()` ms at the moment of the last user input, across all terminal sessions (including RDP). Used for e.g. idle detection. Updated by `win32kbase!CitpLastInputUpdate` at most *once per second*. Settable in kernel mode via `RtlSetSystemGlobalData(GlobalDataIdLastSystemRITEventTickCount[=13])`.


## `NumberOfPhysicalPages`

| Offset | Sigils |
|--------|--------|
| 0x2E8 | ◷ |

```cpp
ULONG NumberOfPhysicalPages;
```

*fixed at boot, but might [rarely] change at runtime*

OS-visible total RAM size, in pages, clamped to `UINT_MAX` (16 TB RAM). Since win11 24H2, extended 64-bit field is also available: 🡓FullNumberOfPhysicalPages. Both fields can change if RAM is added or removed. Be aware: often 1-24 MB less than the actual RAM (sum of smbios memory devices), likely due to uefi hiding some.


## `SafeBootMode`

| Offset | Sigils |
|--------|--------|
| 0x2EC | 𝍌 |

```cpp
BOOLEAN SafeBootMode;
```

True if booted in safe boot mode ("SAFEBOOT:" present in the OS load options).


## `VirtualizationFlags` (in union)

| Offset | Sigils | Context |
|--------|--------|--------|
| 0x2ED | 𝍌 | Part of union at 0x2ED |

```cpp
UCHAR VirtualizationFlags;
```

Copy of `nt!KiVirtFlags`, made in KiInitializeKernel based on `MSR_IA32_FEATURE_CONTROL` and/or `VM_CR` MSR.

- bit0: vmx/svm enableable
- bit1: enableablement locked (`MSR_IA32_FEATURE_CONTROL.lock` is true)

Bits are 0 when: Hyper-V is running (regardless of partition); or VMX is off (in bios, or VM VBS-compatibility off). Bits form mask 3 or 1 when: Hyper-V is NOT running, and VMX is on (in bios, or VM VBS-compatibility ON).


## `ArchStartedInEl2` (in struct)

| Context | Condition |
|--------|--------|
| Bitfield in struct at 0x2ED | defined(_M_ARM64) |

```cpp
UCHAR ArchStartedInEl2: 1;
```


## `QcSlIsSupported` (in struct)

| Context | Condition |
|--------|--------|
| Bitfield in struct at 0x2ED | defined(_M_ARM64) |

```cpp
UCHAR QcSlIsSupported: 1;
```


## `Reserved12`

| Offset | Sigils |
|--------|--------|
| 0x2EE | 𝍌 ♻ |

```cpp
UCHAR Reserved12[2];
```

Zero. "Available for reuse".


## `SharedDataFlags` (in union)

| Offset | Sigils | Context |
|--------|--------|--------|
| 0x2F0 | ◷ 👋 | Part of union at 0x2F0 |

```cpp
ULONG SharedDataFlags;
```

*certain flags may change at runtime*


## `DbgErrorPortPresent` (in struct)

| Context | Bit | Value | Sigils |
|---------|-----|-------|--------|
| Bitfield in struct at 0x2F0 | 0 | 0001 | ◷👋 |

```cpp
ULONG DbgErrorPortPresent: 1;
```

Process with SeTcb privilege can (re-)register one global alpc error port via `SystemErrorPortInformation` system infoclass (-> `nt!DbgkRegisterErrorPort`). When that happens, system sets this bit. When registrar process exits, or if port somehow disconnects, system unregisters port and clears this bit. In practice, this bit indicates whether `WerSvc` is currently running (it registers `\WindowsErrorReportingServicePort`).

Note processes in silo can register error port too, but it'll be silo-specific; this bit won't be set.


## `DbgElevationEnabled` (in struct)

| Context | Bit | Value | Sigils |
|---------|-----|-------|--------|
| Bitfield in struct at 0x2F0 | 1 | 0002 | 𝍌 |

```cpp
ULONG DbgElevationEnabled: 1;
```

*reg value₄: "EnableLUA"*

Following 3 flags, together with new 🡓DbgShadowAdminEnabled, form basis for `RTL_ELEVATION_FLAGS` struct, returned by `RtlQueryElevationFlags` api (in both usermode and kernelmode). Fields set on boot from reg data at `HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System`, they won't update until reboot even if registry values change. Bad type or size of reg data, or a missing value, yields 1 (not 0). However, if `CCS\Control\LsaInformation₄UACInstalled` is 0, all 4 flags will be set to 0. Policy: "UAC: Turn on Admin Approval Mode", aka "UAC: Run all administrators in Admin Approval Mode".


## `DbgVirtEnabled` (in struct)

| Context | Bit | Value | Sigils |
|---------|-----|-------|--------|
| Bitfield in struct at 0x2F0 | 2 | 0004 | 𝍌 |

```cpp
ULONG DbgVirtEnabled: 1;
```

*reg value₄: "EnableVirtualization"*

policy: "UAC: Virtualize file and registry write failures to per-user locations".


## `DbgInstallerDetectEnabled` (in struct)

| Context | Bit | Value | Sigils |
|---------|-----|-------|--------|
| Bitfield in struct at 0x2F0 | 3 | 0008 | 𝍌 |

```cpp
ULONG DbgInstallerDetectEnabled: 1;
```

*reg value₄: "EnableInstallerDetection"*

policy: "UAC: Detect application installations and prompt for elevation".


## `DbgLkgEnabled` (in struct)

| Context | Bit | Value | Sigils |
|---------|-----|-------|--------|
| Bitfield in struct at 0x2F0 | 4 | 0010 | 𝍌 |

```cpp
ULONG DbgLkgEnabled: 1;
```

Indicates if Last Known Good is enabled. This bit mirrors `nt!CmpLKGEnabled`, initialized at boot to `CCS\Control\Session Manager\Configuration Manager\LastKnownGood₄Enabled`. Most often it's 0. This bit is NOT directly related to "DisableLKG" reg value₄ set by `NtDisableLastKnownGood`.


## `DbgDynProcessorEnabled` (in struct)

| Context | Bit | Value | Sigils |
|---------|-----|-------|--------|
| Bitfield in struct at 0x2F0 | 5 | 0020 | 𝍌 |

```cpp
ULONG DbgDynProcessorEnabled: 1;
```

Indicates if new processors can be added at runtime. This bit mirrors exported "almost read-only" value `nt!KeDynamicPartitioningSupported`, initialized at boot; value depends on sku and licensing. Normally it's 0 for client systems, and can be 1 for servers. However: it's always zero in Hyper-V root partition.


## `DbgConsoleBrokerEnabled` (in struct)

| Context | Bit | Value | Sigils |
|---------|-----|-------|--------|
| Bitfield in struct at 0x2F0 | 6 | 0040 | 👋 |

```cpp
ULONG DbgConsoleBrokerEnabled: 1;
```

Dynamic value, managed by `ConDrv.sys` (the console driver). When true, console attach/allocation routines in usermode take different road. Normally value is 0. But if any process with SeTcb privilege asks for brokerage via request to `\Device\ConDrv\Broker`, this bit becomes 1 (until all broker objects are gone).


## `DbgSecureBootEnabled` (in struct)

| Context | Bit | Value | Sigils |
|---------|-----|-------|--------|
| Bitfield in struct at 0x2F0 | 7 | 0080 | 𝍌 |

```cpp
ULONG DbgSecureBootEnabled: 1;
```

True when SecureBoot is enabled. Initialized during boot. Matches simultaneously set value in the volatile "State" subkey: `CCS\Control\SecureBoot\State₄UEFISecureBootEnabled`.


## `DbgMultiSessionSku` (in struct)

| Context | Bit | Value | Sigils |
|---------|-----|-------|--------|
| Bitfield in struct at 0x2F0 | 8 | 0100 | 𝍌 |

```cpp
ULONG DbgMultiSessionSku: 1;
```

Indicates that OS supports multiple sessions. For regular OS it's always 1, even for "single-user sku". It's 0 only for Hyper-V docker containers; even then, OS still uses separate session for user processes. Cleared bit entails serious security lax across OS (user ⥵ admin) due to "WIN://ISMULTISESSIONSKU" conditional ACEs (mainly for registry keys), and regular checks in both modes via `RtlIsMultiSessionSku`.

Bit is zeroed only if:
- `CCS\Control\Session Manager₄NumberOfInitialSessions` < 2 (default 2), AND
- "ext-ms-win-session-wtsapi32-l1-1-0" apiset fails to resolve to proper dll

Silo-aware: `ntdll!RtlIsMultiSessionSku`, `SILO_USER_SHARED_DATA.IsMultiSessionSku`.


## `DbgMultiUsersInSessionSku` (in struct)

| Context | Bit | Value | Sigils |
|---------|-----|-------|--------|
| Bitfield in struct at 0x2F0 | 9 | 0200 | 𝍌 |

```cpp
ULONG DbgMultiUsersInSessionSku: 1;
```

Probably indicates that multiple users can share a session (lightweight user separation?). Often gets checked when 🡑DbgMultiSessionSku is 0. Set at boot to mirror `nt!RtlpMultiUsersInSessionSupported`, from `CCS\Control\Session Manager₄MultiUsersInSessionSupported`. Default is 0. Accessible via exported `ntdll!RtlIsMultiUsersInSessionSku`.


## `DbgStateSeparationEnabled` (in struct)

| Context | Bit | Value | Sigils |
|---------|-----|-------|--------|
| Bitfield in struct at 0x2F0 | 10 | 0400 | 𝍌 |

```cpp
ULONG DbgStateSeparationEnabled: 1;
```

Indicates if state separation is enabled. It's hard to enable it for a regular OS, so normally it's 0. State separation is a facility to use different, configurable paths to some registry hives, some registry keys, and some files. This bit set at boot time to mirror `nt!CmStateSeparationEnabled`, from `CCS\Control\StateSeparation\Policy₄Enabled`.


## `DbgSplitTokenEnabled` (in struct)

| Context | Bit | Value | Sigils |
|---------|-----|-------|--------|
| Bitfield in struct at 0x2F0 | 11 | 0800 | 𝍌 |

```cpp
ULONG DbgSplitTokenEnabled: 1;
```

Relatively new flag, even though concept of split token itself is old. Likely requires at least win11 25H2. Not set in win11 24H2 and before.


## `DbgShadowAdminEnabled` (in struct)

| Context | Bit | Value | Sigils |
|---------|-----|-------|--------|
| Bitfield in struct at 0x2F0 | 12 | 1000 | 𝍌 |

```cpp
ULONG DbgShadowAdminEnabled: 1;
```

*reg value: "TypeOfAdminApprovalMode"*

Part of `RTL_ELEVATION_FLAGS`. Likely requires at least win11 25H2. Not set in win11 24H2 and before.


## `SpareBits` (in struct)

| Context | Bit | Value | Sigils |
|---------|-----|-------|--------|
| Bitfield in struct at 0x2F0 | 13 | ~1FFF | 𝍌♻ |

```cpp
ULONG SpareBits: 19;
```


## `DataFlagsPad`

| Offset | Sigils |
|--------|--------|
| 0x2F4 | 𝍌 ♻ |

```cpp
ULONG DataFlagsPad[1];
```

Zero.


## `TestRetInstruction`

| Offset | Sigils |
|--------|--------|
| 0x2F8 | 𝍌 ♻ |

```cpp
ULONGLONG TestRetInstruction;
```

On x64 contains 0xC3 ("ret"), 0 on ARM64. 32-bit x86 code can jump here to check if DEP is enabled: this page is not executable, but if DEP is effectively off, OS will remove its NX bit for the process on exec attempt, sparing the app `STATUS_ACCESS_VIOLATION`. That won't affect 64-bit processes: they implicitly have DEP enabled, always.


## `QpcFrequency`

| Offset | Sigils |
|--------|--------|
| 0x300 | 𝍌 |

```cpp
LONGLONG QpcFrequency;
```

Frequency of the high-resolution counter, `ntdll!RtlQueryPerformanceCounter()` and `nt!KeQueryPerformanceCounter()`. Value from such counter is known simply as "Qpc". 🡗QpcFrequency = (Qpc₁ - Qpc₀), where (t₁ - t₀) == 1 s. What counter is actually used determined by the `_REGISTERED_TIMER` struct pointed to by `nt!HalpPerformanceCounter`. Timer type is normally `TimerProcessor` (`rdtsc`/`TSC_DEADLINE_MSR`) [or `TimerHypervisor`, or `TimerGit`, ⩯ `rdtsc`]. For `TimerProcessor` OS scales tsc values used for Qpc to 10 MHz == 10⁷ Hz == 0x989680 (since win10 1809). For `TimerHypervisor` the frequency simply set to 10 MHz in the first place. Thus 0x989680 is what you'd normally see there. Duration of each Qpc tick in such case is, naturally, 10⁻⁷ seconds – exactly one centum (100 ns). This field gets set once at boot time together with various other 🡓Qpc\* fields, in `nt!KiSetupTimeIncrement`.


## `SystemCall`

| Offset | Sigils |
|--------|--------|
| 0x308 | 𝍌 |

```cpp
ULONG SystemCall;
```

Normally 0. Contains 1 if `int2E` is preferable to `syscall` (x64 only). Set to 1 when: `nt!KiSystemCallSelector` AND `NtQuery(SystemIsolatedUserModeInformation).HvciEnabled` AND `cpuid(0x40000004).eax.UseIntForMbecSystemCalls`.

Note `int2E` IDT entry is special: its DPL is 0 (disallowed for usermode) when `nt!KiSystemCallSelector` == 0. And the latter mirrors the `LoaderBlock.Extension.VsmConfigured` bit (hypercall code page for VSM mapped by `winload`).


## `Reserved2`

| Offset | Sigils |
|--------|--------|
| 0x30C | 𝍌 ♻ |

```cpp
ULONG Reserved2;
```

Zero. "Reserved field – do not use. Used to be UserCetAvailableEnvironments".


## `FullNumberOfPhysicalPages`

| Offset | Sigils |
|--------|--------|
| 0x310 | ◷ |

```cpp
ULONGLONG FullNumberOfPhysicalPages;
```

*fixed at boot, but might [rarely] change at runtime*

OS-visible total RAM size, in pages. For comparison, 🡑NumberOfPhysicalPages holds 32-bit value of such, clamped to `UINT_MAX` (16 TB RAM). Both values can change if RAM is added or removed; this larger field is updated first. Be aware: often 1-24 MB less than the actual RAM (sum of smbios memory devices), likely due to uefi hiding some.

⚠️ WARNING ⚠️: field available since win11 24H2. On previous systems this location contains 0.


## `SystemCallPad`

| Offset | Sigils |
|--------|--------|
| 0x318 | 𝍌 ♻ |

```cpp
ULONGLONG SystemCallPad[1];
```

Zero. "Available for reuse".


## `TickCountQuad` (in union)

| Offset | Sigils | Context |
|--------|--------|--------|
| 0x320 | ❕ | Part of union at 0x320 |

```cpp
volatile ULONG64 TickCountQuad;
```

*incremented by one every 15.625 ms (virtually all systems)*


## `TickCountPad` (in struct)

| Offset | Sigils | Context |
|--------|--------|--------|
| 0x32C | 𝍌 ♻ | Part of struct at 0x320 |

```cpp
ULONG TickCountPad[1];
```


## `Cookie`

| Offset | Sigils |
|--------|--------|
| 0x330 | 𝍌 |

```cpp
ULONG Cookie;
```

Cookie for encoding usermode pointers system-wide. Not related to the stack GS cookie, nor to the `ProcessCookie` infoclass. Exported `ntdll!RtlEncodeSystemPointer` uses this field: `encoded_ptr = rotr(orig_ptr ^ Cookie, Cookie)`. Set once per boot to a good random value, on the first usermode thread creation, in `nt!PspNotifyThreadCreation`.


## `CookiePad`

| Offset | Sigils |
|--------|--------|
| 0x334 | 𝍌 ♻ |

```cpp
ULONG CookiePad[1];
```

Zero. Could have been higher part of the cookie to encode more bits, but unfortunately this field is unused.


## `ConsoleSessionForegroundProcessId`

| Offset | Sigils |
|--------|--------|
| 0x338 | ❕ 👋 |

```cpp
volatile LONGLONG ConsoleSessionForegroundProcessId;
```

*physical user controls it; 🐞 added "volatile"*

Process ID (pid) of the process with focus in the current physical console. RDP sessions ignored. Edge cases when value is zero: Windows Sandbox (as it's RDP), and Hyper-V docker containers (as they are gui-less, so no focus). Hyper-V Manager *enhanced* sessions are RDP too, in such sessions you'll observe some "leftover" value, normally the pid of the `LogonUI.exe` running in the "physical" *basic* session. Similar to 🡑ActiveConsoleId. When the physical box (or its equivalent) is locked, focused app is normally `LogonUI.exe`; pid here reflects that.

⚠️ Process death is not tracked – there might be brief periods when this field contains id of an already terminated process, or even id of some new, unrelated process due to pid reuse (very brief and rare). To set this field `win32kfull.sys` uses dedicated exported api: `nt!RtlSetConsoleSessionForegroundProcessId`.

Silo-aware: `RtlGetConsoleSessionForegroundProcessId`, `SILO_USER_SHARED_DATA.ConsoleSessionForegroundProcessId`.


## `TimeUpdateLock`

| Offset | Sigils |
|--------|--------|
| 0x340 | ❕ |

```cpp
volatile ULONGLONG TimeUpdateLock;
```

*changes twice each clock interrupt; 🐞 added "volatile"*

Sequence number/lock for time-related fields. When value is odd, set of fields is being updated. See "Cross-fields coherence via sequence numbers" below for details. List of protected fields, in currently utilized update order (not everything listed is always updated): 🡑SystemTime, 🡑InterruptTime, 🡓BaselineSystemTimeQpc, 🡓BaselineInterruptTimeQpc , [🡑TickCountQuad]. And on the rare "time-only" codepath we have slightly different update order and 2 more fields: 🡓BaselineSystemTimeQpc, 🡑SystemTime, 🡓QpcSystemTimeIncrement, 🡓QpcSystemTimeIncrementShift.


## `BaselineSystemTimeQpc`

| Offset | Sigils |
|--------|--------|
| 0x348 | ❕ |

```cpp
volatile ULONGLONG BaselineSystemTimeQpc;
```

*updates together with 🡑SystemTime; 🐞 added "volatile"*

Value retrieved via `nt!KeQueryPerformanceCounter()` right before the 🡑SystemTime field update, and used to compute new value of 🡑SystemTime. Associated subfractional parts accumulator: `nt!KiSystemTimeErrorAccumulator`.


## `BaselineInterruptTimeQpc`

| Offset | Sigils |
|--------|--------|
| 0x350 | ❕ |

```cpp
volatile ULONGLONG BaselineInterruptTimeQpc;
```

*updates together with 🡑InterruptTime; 🐞 added "volatile"*

Value retrieved via `nt!KeQueryPerformanceCounter()` right before the 🡑InterruptTime field update, and used to compute new value of 🡑InterruptTime. Since on the "system tick" codepath 🡑InterruptTime and 🡑SystemTime are updated together, this field most often holds very same Qpc value as 🡑BaselineSystemTimeQpc. Associated subfractional parts accumulator: `nt!KiInterruptTimeErrorAccumulator`.


## `QpcSystemTimeIncrement`

| Offset | Sigils |
|--------|--------|
| 0x358 | ◷ |

```cpp
ULONGLONG QpcSystemTimeIncrement;
```

*might change at runtime for a bit (supposedly rare)*

Fractional part of the Multiplier for computing new 🡑SystemTime: `SystemTime += QpcDelta × Multiplier`. This field might change at runtime to speedup/slowdown the clock; that avoids sudden time jumps during timesync. Such clockrate change does NOT affect performance: rate of 🡑InterruptTime and osticks/`GetTickCount()` is constant. It's common to see value 0x8000'0000'0000'0000 here; with fixed scaler of -0x40 that's effectively 0.5. See "Time updates via Qpc deltas and increments" below for details on the System Time computation.


## `QpcInterruptTimeIncrement`

| Offset | Sigils |
|--------|--------|
| 0x360 | 𝍌 |

```cpp
ULONGLONG QpcInterruptTimeIncrement;
```

Fractional part of the Multiplier for computing new 🡑InterruptTime: InterruptTime += QpcDelta × Multiplier. Set once during boot, in `nt!KiSetupTimeIncrement`. Remains constant afterwards. It's common to see value 0x8000'0000'0000'0000 here; with fixed scaler of -0x40 that's effectively 0.5. See "Time updates via Qpc deltas and increments" below for details on the Interrupt Time computation.


## `QpcSystemTimeIncrementShift`

| Offset | Sigils |
|--------|--------|
| 0x368 | ◷ |

```cpp
UCHAR QpcSystemTimeIncrementShift;
```

*might change at runtime for a bit (supposedly rare)*

Extra scaling bits for computing new 🡑SystemTime; scaler = -0x40 + 🡗QpcSystemTimeIncrementShift. Just like with 🡑QpcSystemTimeIncrement, this field *might change* at runtime to speedup or slowdown the clock. It's common to see value 1 here; when const-scaled 🡑QpcSystemTimeIncrement is effectively 0.5, these two fields basically cancel each other out. See "Time updates via Qpc deltas and increments" below for details.


## `QpcInterruptTimeIncrementShift`

| Offset | Sigils |
|--------|--------|
| 0x369 | 𝍌 |

```cpp
UCHAR QpcInterruptTimeIncrementShift;
```

Extra scaling bits for computing new 🡑InterruptTime; scaler = -0x40 + 🡗QpcInterruptTimeIncrementShift. Just like with 🡑QpcInterruptTimeIncrement, this field *set once* during boot, in `nt!KiSetupTimeIncrement`. It's common to see value 1 here; when const-scaled 🡑QpcInterruptTimeIncrement is effectively 0.5, these two fields basically cancel each other out. See "Time updates via Qpc deltas and increments" below for details.


## `UnparkedProcessorCount`

| Offset | Sigils |
|--------|--------|
| 0x36A | ❕ |

```cpp
volatile USHORT UnparkedProcessorCount;
```

*may change a lot at runtime; 🐞 added "volatile"*

Number of "powered on" [logical] processors. Each SMT core counts as a separate processor. This value can swing a lot at runtime as OS parks CPUs to save power. Always ≤ 🡓ActiveProcessorCount. Most often used to avoid spins in locks when there's only one running processor (by user and kernel mode alike).


## `EnclaveFeatureMask`

| Offset | Sigils |
|--------|--------|
| 0x36C | 𝍌 ♻ |

```cpp
ULONG EnclaveFeatureMask[4];
```

Bitmask of enclave features supported on this system. Used by `ntdll!RtlIsEnclaveFeaturePresent`. Out of the whole 128-bit value, only 3 bits seem to be currently defined:

- bit1/bit2: SGX1/SGX2 leaf funcs enabled (and locked in that state)
- bit8: 1 if `LoaderBlock->Extension.IumEnabled` (can be 1 in root and non-root partitions; 0 if Hyper-V is off)


## `TelemetryCoverageRound`

| Offset | Sigils |
|--------|--------|
| 0x37C | 👋 |

```cpp
ULONG TelemetryCoverageRound;
```

Current coverage round for telemetry based coverage (sequence number). Set to 1 at boot in `nt!EtwpInitializeCoverage` – and most of the time stays like that. One way to increment this value: end the coverage round via `NtSetInformationProcess(ProcessTelemetryCoverage, {.LastCoveredRound=-4})`; however, that needs enabled Administrators group in client's token.


## `UserModeGlobalLogger`

| Offset | Sigils |
|--------|--------|
| 0x380 | 👋 |

```cpp
USHORT UserModeGlobalLogger[0x10];
```

*limited adjustability, specific conditions required*

Used for ETW UMGL (user-mode global logging). Indices are `ETW_UMGL_INDEX_*` constants (see `nt!EtwpUmglProviders`): `ETW_UMGL_INDEX_HEAP` = 0 (`nt!HeapGuid`), `ETW_UMGL_INDEX_CRITSEC` = 1 (`nt!CritSecGuid`), etc. Each USHORT is actually a 2-byte `ETW_UMGL_KEY` structure: byte0 is LoggerId, byte1 is "MatchAnyKeyword" Flags. `NtTraceControl(EtwSendDataBlock)` -> ... -> `nt!EtwpEnableDisableSpecialGuids()` -> `nt!EtwpEnableDisableUMGL()`.

Silo-aware: `SILO_USER_SHARED_DATA.UserModeGlobalLogger`. See `ETW_UMGL_*` macro and defines for more.


## `ImageFileExecutionOptions`

| Offset | Sigils |
|--------|--------|
| 0x3A0 | 👋 ♻ |

```cpp
ULONG ImageFileExecutionOptions;
```

*changeable at runtime (but normally static)*

When bit0 is set, "GlobalFlag" bits `FLG_APPLICATION_VERIFIER`|`FLG_HEAP_PAGE_ALLOCS` (0x0200'0100) will be read from HKCU IFEO (as long as both flags🡕 absent in HKLM IFEO, and it's not a secure process). These two verifier bits are read by `ntdll` during process init, saved in `PEB.GlobalFlags`. This field does NOT affect other IFEO values or GlobalFlag bits; they're still read from HKLM and PE `LoadConfig`. Bit0 initialized during boot in `nt!VerifierInitSystem`, from bit0 of `nt!ViImageExecutionOptions` (in turn, from `CCS\Control\Session Manager₄ImageExecutionOptions`). This entire field can be adjusted at runtime by clients with SeTcb privilege, via `NtSetSystemInformation(SystemImageFileExecutionOptionsInformation)`.


## `LangGenerationCount`

| Offset | Sigils |
|--------|--------|
| 0x3A4 | 👋 |

```cpp
ULONG LangGenerationCount;
```

*changeable at runtime (but mostly static)*

Sequence number of the `nt!MUIRegistryInfo` structure, which holds UI languages info. Starts at 0 during boot. Only changes when usermode calls `NtGetMUIRegistryInfo(Flags |= 8)`; that increments this field, and also assigns updated value to `nt!MUIRegistryInfo`.Generation (when `nt!MUIRegistryInfo` exists). Normally the first and only increment is done by the first `Winlogon.exe`. No rights nor privileges required to perform such increment.


## `Reserved4`

| Offset | Sigils |
|--------|--------|
| 0x3A8 | 𝍌 ♻ |

```cpp
ULONGLONG Reserved4;
```

Zero. "Available for reuse".


## `InterruptTimeBias`

| Offset | Sigils |
|--------|--------|
| 0x3B0 | ◷ 👋 |

```cpp
volatile ULONGLONG InterruptTimeBias;
```

*rare updates on power events; "manual" via timed sleep*

Under certain conditions (e.g. after hibernation), OS makes 🡑InterruptTime to jump forward (OS "biases" it). This field accumulates all such adjustments, enabling clients to get unadulterated Interrupt Time. To get such unadulterated Unbiased Interrupt Time, take 🡑InterruptTime, and subtract 🡗InterruptTimeBias from it.

⚠️ Field is NOT protected via 🡑TimeUpdateLock. To ensure coherence between this field and 🡑InterruptTime, read this value first, then 🡑InterruptTime, then this value again – and check it hasn't changed.

Note `ntdll!RtlQueryUnbiasedInterruptTime` does a bit more: it wraps that sequence into a pair of reads of exported `ntdll!RtlpFreezeTimeBias` [where OS accumulates Deep Freeze time for current process], and subtracts that too.

Updated on these paths:

1. `nt!KeAdjustInterruptTime`. Mostly on exit from sleep/hibernate; also if `TickcountRolloverDelay` 🡑 used.
2. `nt!KiAdjustTimersAfterDripsExit`. DRIPS is Deepest Runtime Idle Platform State. Tricky: only increments if OS spent more than `nt!KeTimerRebaseThresholdOnDripsExit` consecutive seconds in the current DRIPS state. That var is from `CCS\Control\Power₄TimerRebaseThresholdOnDripsExit`; by default it's 45 seconds.


## `QpcBias`

| Offset | Sigils |
|--------|--------|
| 0x3B8 | ◷ 👋 |

```cpp
volatile ULONGLONG QpcBias;
```

*rare updates on power events; "manual" via timed sleep*

Somewhat similar to 🡑InterruptTimeBias. Accumulates bias for the Qpc value. But there's important difference: 🡑InterruptTime already incorporates bias, so client-oriented api `RtlQueryUnbiasedInterruptTime` has to *subtract* 🡑InterruptTimeBias; but raw Qpc value does NOT incorporate bias, so `RtlQueryPerformanceCounter` has to *add* 🡗QpcBias! Yes, it's almost like OS devs mixed up bias inclusion cases to do some extra math on hot codepaths. Unit is 🡑QpcFrequency⁻¹ seconds. When `nt!HalpPerformanceCounter` type is Processor or Hypervisor, frequency is 10 MHz; making the unit exactly one centum (100 ns), same as 🡑InterruptTimeBias. Updated in `nt!HalpTimerPropagateQpcBiasUpdate`, on rare power-related events, like sleep/hibernation. For `TimerHypervisor` and `TimerGit`, bias value comes directly from `REGISTERED_TIMER.TimeBias`. For `TimerProcessor` that same `TimeBias` field is scaled to 10 MHz first. Settable in kernel mode via `RtlSetSystemGlobalData(GlobalDataIdQpcBias[=18])`.


## `ActiveProcessorCount`

| Offset | Sigils |
|--------|--------|
| 0x3C0 | ◷ |

```cpp
volatile ULONG ActiveProcessorCount;
```

*rare increments at runtime possible; 🐞 added "volatile"*

Number of [logical] processors in the system. Each SMT core counts as a separate processor. Field name is mildly confusing (and digging deeper only makes it worse). Value mirrors unexported `nt!KeNumberProcessors`; don't mistake it for the *exported* "KeNumberProcessors", which is actually `nt!KeNumberProcessorsGroup0` variable (¿⸮?). Also don't mix it up with `nt!KeMaximumProcessors`🡖, nor with `nt!KeActiveProcessors` (set of `KAFFINITY_EX` masks). ⮞ TLDR: just drop "Active" from the name. Use 🡑UnparkedProcessorCount for count of CPUs actually running atm. Field set during boot. On some server SKUs you can add CPUs dynamically: on such systems this value may increase at runtime. But it will never decrease, and will never exceed `nt!KeMaximumProcessors` during current boot session. Absolute max # of processors: ws2022/win11: 0x800 (2048) [confirmed 24H2]; win10 22H2: 0x500 (1280).


## `ActiveGroupCount`

| Offset | Sigils |
|--------|--------|
| 0x3C4 | ◷ |

```cpp
volatile UCHAR ActiveGroupCount;
```

*rare increments possible*

Number of processor groups in the system. Mirrors `nt!KiActiveGroups`. On some server SKUs you can add CPUs dynamically: on such systems this value may increase at runtime.

Note you can force-split CPUs into multiple groups on boot: `bcdedit /set GroupSize 2` to get N groups with 2 CPUs each. Absolute max # of CPU groups for any OS is 0x20 (32) [confirmed 24H2].


## `Reserved9`

| Offset | Sigils |
|--------|--------|
| 0x3C5 | 𝍌 ♻ |

```cpp
UCHAR Reserved9;
```

Zero. "Available for reuse".


## `QpcData` (in union)

| Offset | Sigils | Context |
|--------|--------|--------|
| 0x3C6 | ◷ | Part of union at 0x3C6 |

```cpp
USHORT QpcData;
```

Entire field settable in kernel mode via `RtlSetSystemGlobalData(GlobalDataIdQpcData[=17])`.


## `QpcBypassEnabled` (in struct)

| Offset | Sigils | Context |
|--------|--------|--------|
| 0x3C6 | ◷ | Part of struct at 0x3C6 |

```cpp
volatile UCHAR QpcBypassEnabled;
```

*won't really change, except possibly on OS live migration*

Bitflags governing `ntdll!RtlQueryPerformanceCounter()` behavior, described above. On old OS [before win10 1709, RS3] it was a bool, that role is now taken by bit0. This byte settable in kernel mode via `RtlSetSystemGlobalData(QpcBypassEnabled[=16])`.


## `QpcShift` (in struct)

| Offset | Sigils | Context |
|--------|--------|--------|
| 0x3C7 | 𝍌 ♻ | Part of struct at 0x3C6 |

```cpp
UCHAR QpcShift;
```

Zero. Unused on modern OS. On old OS [before win10 1709, RS3] it was used as a bitshift value for the raw perfcounter: `ntdll!RtlQueryPerformanceCounter()` => `(rdtsc() + 🡑QpcBias) >> 🡗QpcShift` [before 1709]. But that made Qpc rate very different across systems; nowadays OS uses much more precise scaling.


## `TimeZoneBiasEffectiveStart`

| Offset | Sigils |
|--------|--------|
| 0x3C8 | ◷ 👋 |

```cpp
LARGE_INTEGER TimeZoneBiasEffectiveStart;
```

Pair (🡗TimeZoneBiasEffectiveStart, 🡗TimeZoneBiasEffectiveEnd) form a range for 🡑SystemTime when 🡑TimeZoneBias is valid. That is, if 🡑SystemTime is in that range, LocalTime = (🡑SystemTime - 🡑TimeZoneBias). That's true regardless of DST (it's already included in 🡑TimeZoneBias). If both range ends are 0, the range spans *all* time. For time outside the range, local time has to be computed manually. Fields can be updated at runtime (e.g. when range end is reached, or timezone changed). Coherence in relation to 🡑TimeZoneBias during fields update ensured via 🡑TimeZoneBiasStamp.

Silo-aware: `SILO_USER_SHARED_DATA.TimeZoneBiasEffectiveStart`, `SILO_USER_SHARED_DATA.TimeZoneBiasEffectiveEnd`.

Normally, 🡗TimeZoneBiasEffectiveStart is equal to the snapshot of 🡑SystemTime at one of these moments:
- system boot + 5..15 seconds
- system date/time change
- timezone change
- crossing the DST line (i.e. 🡑SystemTime reached 🡗TimeZoneBiasEffectiveEnd, so the new range has to be established)

🡗TimeZoneBiasEffectiveEnd updated together with 🡗TimeZoneBiasEffectiveStart. It's set to either the next DST line or to (end of year + 🡑TimeZoneBias), whichever is earlier. Adjustable – within a certain amount – by clients with SeTimeZone privilege, together with 🡑TimeZoneBias.


## `TimeZoneBiasEffectiveEnd`

| Offset | Sigils |
|--------|--------|
| 0x3D0 | ◷ 👋 |

```cpp
LARGE_INTEGER TimeZoneBiasEffectiveEnd;
```

See `TimeZoneBiasEffectiveStart` above.


## `XState`

| Offset | Sigils |
|--------|--------|
| 0x3D8 | 𝍌 ♻ |

```cpp
XSTATE_CONFIGURATION XState;
```

*used now, but really should not be in kuser*

Extended processor state configuration. Initialized once at boot in `nt!KiInitializeXSaveConfiguration`, based on features actually supported by cpu, and features disabled via `LoaderBlock` (`bcdedit /set xsaveDisable|xsavePolicy|xsaveRemoveFeature`). Since win11 24H2, ARM64 oskernel tries to ignore this field, uses its own 🡓XStateArm64 instead. But even though ARM64 doesn't init it, `XState.EnabledFeatures` still used sometimes (e.g. `nt!PopHandleNextState`) due to bugs/leftovers.


## `FeatureConfigurationChangeStamp`

| Offset |
|--------|
| 0x720 |

```cpp
KSYSTEM_TIME FeatureConfigurationChangeStamp;
```

*offset is 0x710 on win10 22H2 and earlier OS*

Mirrors global value read via exported `nt!RtlQueryFeatureConfigurationChangeStamp` (part of `nt!CmFcSystemManager`). Starts at 1 at boot, increments each time feature config changes. However, there is so called "SwapReferenceIndex" (`RtlGetSwapReferenceIndex`), changing which might bring in parallel global value. This field is what's referred to as `RTL_FEATURE_CHANGE_STAMP`/`ChangeStamp` in structures for `NtSetSystemInformation(SystemFeatureConfigurationInformation)`.

Note these are NOT "Optional Windows Features"; rather these are A/B features (and ongoing security fix "features"), adjustable via e.g. opensource ViveTool.

⚠️ Size of 🡑XState increased by 0x10 in WS2022, changing this field offset from 0x710 to 0x720.


## `Spare`

| Offset | Sigils |
|--------|--------|
| 0x72C | 𝍌 ♻ |

```cpp
ULONG Spare;
```

Zero.


## `UserPointerAuthMask`

| Offset | Sigils |
|--------|--------|
| 0x730 | 𝍌 |

```cpp
UINT64 UserPointerAuthMask;
```

*available since win11 22H2*

Mirrors `nt!KePointerAuthMask`. Only used for ARM64, zero on x64. Initialized once at boot. Contains a mask to apply to a pointer value to extract authentication "PAC" bits together with a sign bit (highest bit preceding the PAC). If PAC is not used, or PAC size is not exactly 8 bits, value is simply zero (confirmed win11 24H2 and earlier). So the only values possible are 0 and 0xFF80'0000'0000'0000 [2025-08].


## `XStateArm64`

| Offset | Sigils | Condition |
|--------|--------|--------|
| 0x738 | 𝍌 ♻ | ARM64 only |

```cpp
XSTATE_CONFIGURATION XStateArm64;
```

*used now, but really should not be in kuser*

Following fields are there since win11 24H2. Extended processor state configuration specifically for ARM64. ARM64 OS kernels before win11 24H2 were less greedy and simply used 🡑XState.


## `Reserved10`

| Offset | Sigils | Condition |
|--------|--------|--------|
| 0x738 | 𝍌 ♻ | Non-ARM64 |

```cpp
UINT Reserved10[0xD2];
```

"The reserved space for other architectures is not available for reuse".


## Structure End

Total size: 0xA80
