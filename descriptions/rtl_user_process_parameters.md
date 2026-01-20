### MaximumLength

Specifies the total size, in bytes, of memory allocated for the structure. Up to `MaximumLength` bytes may be written into the buffer without trampling memory.

### Length

Total allocated size of the process parameter block, including the fixed structure and the following variable-length string data stored contiguously after the structure:

* `CurrentDirectory.DosPath`
* `DllPath`
* `ImagePathName`
* `CommandLine`
* `WindowTitle`
* `DesktopInfo`
* `ShellInfo`
* `RuntimeData`
* `RedirectionDllName`

Note that this does not include data allocated separately and referenced via pointers that are always absolute, such as the `Environment` pointer.

### Flags

Process parameter flags. These flags control various behaviors during process creation and initialization.

| Flag | Value | Description |
|------|-------|-------------|
| `RTL_USER_PROC_PARAMS_NORMALIZED` | `0x00000001` | Structure is normalized by `RtlNormalizeProcessParams`. Pointers that are specified above (in the `Length` field description) are absolute addresses rather than offsets. |
| `RTL_USER_PROC_PROFILE_USER` | `0x00000002` | |
| `RTL_USER_PROC_PROFILE_KERNEL` | `0x00000004` | |
| `RTL_USER_PROC_PROFILE_SERVER` | `0x00000008` | |
| `RTL_USER_PROC_UNKNOWN` | `0x00000010` | |
| `RTL_USER_PROC_RESERVE_1MB` | `0x00000020` | The system should reserve a region at the lower addresses (the NULL page) at process creation. See also `PS_MEMORY_RESERVE` and `PS_ATTRIBUTE_MEMORY_RESERVE`. |
| `RTL_USER_PROC_RESERVE_16MB` | `0x00000040` | The system should reserve a region at the lower addresses (the NULL page) at process creation. See also `PS_MEMORY_RESERVE` and `PS_ATTRIBUTE_MEMORY_RESERVE`. |
| `RTL_USER_PROC_CASE_SENSITIVE` | `0x00000080` | |
| `RTL_USER_PROC_DISABLE_HEAP_DECOMMIT` | `0x00000100` | |
| `RTL_USER_PROC_PROCESS_OR_1` | `0x00000200` | |
| `RTL_USER_PROC_PROCESS_OR_2` | `0x00000400` | |
| `RTL_USER_PROC_DLL_REDIRECTION_LOCAL` | `0x00001000` | |
| `RTL_USER_PROC_APP_MANIFEST_PRESENT` | `0x00002000` | The system has detected an application manifest upon process creation. |
| `RTL_USER_PROC_IMAGE_KEY_MISSING` | `0x00004000` | The corresponding Image File Execution Options (IFEO) key was not found at process creation. |
| `RTL_USER_PROC_DEV_OVERRIDE_ENABLED` | `0x00008000` | Required for DotLocal to work on certain codepaths. Set in `PspSetupUserProcessAddressSpace` from `PspGlobalFlags.DevOverrideEnabled`. Controlled by system-global IFEO `DevOverrideEnable`. [Documented by sixtyvividtails](https://x.com/sixtyvividtails/status/1719785195086266581). |
| `RTL_USER_PROC_OPTIN_PROCESS` | `0x00020000` | |
| `RTL_USER_PROC_SESSION_OWNER` | `0x00040000` | |
| `RTL_USER_PROC_HANDLE_USER_CALLBACK_EXCEPTIONS` | `0x00080000` | |
| `RTL_USER_PROC_PROTECTED_PROCESS` | `0x00400000` | |
| `RTL_USER_PROC_NO_IMAGE_EXPANSION_MITIGATION` | `0x02000000` | |
| `RTL_USER_PROC_APPX_LOADER_ALTERNATE_FORWARDER` | `0x04000000` | |
| `RTL_USER_PROC_APPX_GLOBAL_OVERRIDE` | `0x08000000` | |
| `RTL_USER_PROC_ONECORE_FORWARDERS_ENABLED` | `0x20000000` | Enables the loader to use OneCore API set forwarders when resolving DLL imports. Set in `PspSetupUserProcessAddressSpace` from `_ESERVERSILO_GLOBALS.OneCoreForwardersEnabled`. [Documented by sixtyvividtails](https://x.com/sixtyvividtails/status/1832175457229255082). |
| `RTL_USER_PROC_EXIT_PROCESS_NORMAL` | `0x40000000` | Allows processes with `AppModelPolicy_ProcessEnd_TerminateProcess` to opt back in to the normal `ExitProcess` path that detaches from DLLs on exit. |
| `RTL_USER_PROC_SECURE_PROCESS` | `0x80000000` | |

### DebugFlags

### ConsoleHandle

Handle identifying the console session associated with the process. Inherited from parent process by default, or set to a special value during process creation:

| Value | Description |
|-------|-------------|
| `RTL_USER_PROC_DETACHED_PROCESS` | Process created with `DETACHED_PROCESS` flag. |
| `RTL_USER_PROC_CREATE_NEW_CONSOLE` | Process created with `CREATE_NEW_CONSOLE` flag. |
| `RTL_USER_PROC_CREATE_NO_WINDOW` | Process created with `CREATE_NO_WINDOW` flag. |

For running console processes, this field usually stores the console connection handle (`\Device\ConDrv\Connect`).

### ConsoleFlags

| Flag | Value | Description |
|------|-------|-------------|
| `CONSOLE_IGNORE_CTRL_C` | `0x01` | Set when process is created with `CREATE_NEW_PROCESS_GROUP` without `CREATE_NEW_CONSOLE`. Allows the process to temporarily block Ctrl+C requests. You can set/remove this flag via `SetConsoleCtrlHandler(NULL, TRUE/FALSE)`. |

### StandardInput

Handle to the standard input stream. Corresponds to `STARTUPINFO.hStdInput`.

For console processes, this field usually stores a `\Device\ConDrv\Input` handle.

### StandardOutput

Handle to the standard output stream. Corresponds to `STARTUPINFO.hStdOutput`.

For console processes, this field usually stores a `\Device\ConDrv\Output` handle.

### StandardError

Handle to the standard error stream. Corresponds to `STARTUPINFO.hStdError`.

For console processes, this field usually stores a `\Device\ConDrv\Output` handle (same as the standard output).

### CurrentDirectory

A `CURDIR` structure containing the current directory path and handle.

The `DosPath` member is specified as a DOS-like path, e.g., `C:\Windows\System32`.

The `Handle` member is an open handle to the current directory file object.

Note that the caller should always check the normalization flag before attempting to use `DosPath` as-is.

### DllPath

DOS-like paths separated by `;` where the system should search for DLL files.

Note that the caller should always check the normalization flag before attempting to use the value as is.

### ImagePathName

Full path in DOS-like format to the process executable image, e.g., `C:\Windows\System32\notepad.exe`.

Note that the caller should always check the normalization flag before attempting to use the value as is.

### CommandLine

The command line string passed to the process.

Note that the caller should always check the normalization flag before attempting to use the value as is.

### Environment

Pointer to the environment block. See `RtlCreateEnvironment` for creating environment blocks.

### StartingX

Initial X position of the window in pixels. Corresponds to `STARTUPINFO.dwX`. Only used if `WindowFlags` includes `STARTF_USEPOSITION`.

### StartingY

Initial Y position of the window in pixels. Corresponds to `STARTUPINFO.dwY`. Only used if `WindowFlags` includes `STARTF_USEPOSITION`.

### CountX

Initial width of the window in pixels. Corresponds to `STARTUPINFO.dwXSize`. Only used if `WindowFlags` includes `STARTF_USESIZE`.

### CountY

Initial height of the window in pixels. Corresponds to `STARTUPINFO.dwYSize`. Only used if `WindowFlags` includes `STARTF_USESIZE`.

### CountCharsX

Screen buffer width in character columns. Corresponds to `STARTUPINFO.dwXCountChars`. Only used if `WindowFlags` includes `STARTF_USECOUNTCHARS`.

### CountCharsY

Screen buffer height in character rows. Corresponds to `STARTUPINFO.dwYCountChars`. Only used if `WindowFlags` includes `STARTF_USECOUNTCHARS`.

### FillAttribute

Initial text and background colors for console windows. Corresponds to `STARTUPINFO.dwFillAttribute`. Only used if `WindowFlags` includes `STARTF_USEFILLATTRIBUTE`. Uses console color attributes (e.g., `FOREGROUND_RED | BACKGROUND_BLUE`).

### WindowFlags

Flags indicating which `STARTUPINFO` fields contain valid data. Corresponds to `STARTUPINFO.dwFlags`. Common values:

| Flag | Value | Description |
|------|-------|-------------|
| `STARTF_USESHOWWINDOW` | `0x0001` | Use `ShowWindowFlags` value |
| `STARTF_USESIZE` | `0x0002` | Use `CountX` and `CountY` |
| `STARTF_USEPOSITION` | `0x0004` | Use `StartingX` and `StartingY` |
| `STARTF_USECOUNTCHARS` | `0x0008` | Use `CountCharsX` and `CountCharsY` |
| `STARTF_USEFILLATTRIBUTE` | `0x0010` | Use `FillAttribute` |
| `STARTF_RUNFULLSCREEN` | `0x0020` | Run full screen (x86 console only) |
| `STARTF_FORCEONFEEDBACK` | `0x0040` | Force feedback cursor on |
| `STARTF_FORCEOFFFEEDBACK` | `0x0080` | Force feedback cursor off |
| `STARTF_USESTDHANDLES` | `0x0100` | Use Standard* handle fields |
| `STARTF_USEHOTKEY` | `0x0200` | `StandardInput` contains a hotkey value instead of a handle. |
| `STARTF_HASSHELLDATA` | `0x0400` | `StandardOutput` contains either a monitor handle (to specify the monitor on which to start the process) or an icon handle (legacy, NT 3.x only). When set, `STARTF_USESTDHANDLES` is ignored. |
| `STARTF_TITLEISLINKNAME` | `0x0800` | `WindowTitle` is a shortcut file path (`.lnk`). |
| `STARTF_TITLEISAPPID` | `0x1000` | `WindowTitle` is an AppUserModelID |
| `STARTF_PREVENTPINNING` | `0x2000` | Prevent taskbar pinning |
| `STARTF_UNTRUSTEDSOURCE` | `0x8000` | Process started from untrusted source |
| `STARTF_INHERITDESKTOP` | `0x40000000` | Inherit desktop from parent process. |
| `STARTF_SCREENSAVER` | `0x80000000` | Process starts at `NORMAL_PRIORITY`, then drops to `IDLE_PRIORITY` on first `GetMessage` call. Only WinLogon is permitted to use this flag. |

### ShowWindowFlags

Specifies how the window should be shown. Corresponds to `STARTUPINFO.wShowWindow`. Uses the `SW_*` values from `ShowWindow()`, e.g., `SW_SHOW`, `SW_HIDE`, `SW_MAXIMIZE`. Only used if `WindowFlags` includes `STARTF_USESHOWWINDOW`.

### WindowTitle

For console processes, the title displayed in the title bar if a new console window is created. If `NULL`, the executable file name is used. When `STARTF_TITLEISAPPID` is set, contains an AppUserModelID instead. Corresponds to `STARTUPINFO.lpTitle`.

Note that the caller should always check the normalization flag before attempting to use the value as is.

### DesktopInfo

Name of the WindowStation and Desktop objects where the process is assigned, in the format `WindowStation\Desktop`, e.g., `WinSta0\Default`. Corresponds to `STARTUPINFO.lpDesktop`.

Note that the caller should always check the normalization flag before attempting to use the value as is.

### ShellInfo

Corresponds to `STARTUPINFO.lpReserved`. Historically used by Program Manager to pass startup information as a comma-separated string in format `dde.#,hotkey.#,ntvdm.#`.

Source: [Undocumented CreateProcess](https://www.catch22.net/tuts/system/undocumented-createprocess/) by Catch22.

Note that the caller should always check the normalization flag before attempting to use the value as is.

### RuntimeData

Corresponds to `STARTUPINFO.lpReserved2`/`cbReserved2`. Used by the C runtime to pass open file handles to child processes.

Source: [Undocumented CreateProcess](https://www.catch22.net/tuts/system/undocumented-createprocess/) by Catch22.

Note that the caller should always check the normalization flag before attempting to use the value as is.

### CurrentDirectories[RTL_MAX_DRIVE_LETTERS]

Array of 32 `RTL_DRIVE_LETTER_CURDIR` structures. The intended purpose was keeping a current directory for each drive letter, but no code is known that uses this array.

Source: [Geoff Chappell](https://www.geoffchappell.com/studies/windows/km/ntoskrnl/inc/api/pebteb/rtl_drive_letter_curdir.htm).

### EnvironmentSize

Specifies the total size, in bytes, of memory allocated for the `Environment` structure.

Added in Windows Vista.

### EnvironmentVersion

The number of times the environment block has changed. Incremented every time by `RtlSetEnvironmentStrings` and `RtlSetEnvironmentVar`.

Added in Windows 7.

### PackageDependencyData

Added in Windows 8.

### ProcessGroupId

The console group identifier to narrow down control signal delivery.

Added in Windows 8.

### LoaderThreads

Number of worker threads for parallel DLL loading during process initialization. If 0, defaults to 4; if greater than 16, capped at 16. The thread pool is created with one less than this value since the main thread also participates in loading. Can be overridden via IFEO `MaxLoaderThreads` registry value.

Source: [Windows 10 Parallel Loading Breakdown](https://blogs.blackberry.com/en/2017/10/windows-10-parallel-loading-breakdown) by BlackBerry.

Added in Windows 10.

### RedirectionDllName

Path to a DLL that provides import redirection for packaged applications (Desktop Bridge). If set, the loader calls `LdrpLoadDll` to load it during process initialization. For non-packaged apps, the DLL must be Microsoft-signed. Configured via `ImportRedirectionTable` in the app manifest.

Source: [DLL Import Redirection in Windows 10 1909](https://www.tiraniddo.dev/2020/02/dll-import-redirection-in-windows-10_8.html) by James Forshaw.

Note that the caller should always check the normalization flag before attempting to use the value as is.

Added in Windows 10 version 1809.

### HeapPartitionName

Added in Windows 10 version 1903.

### DefaultThreadpoolCpuSetMasks

Added in Windows 10 version 1903.

### DefaultThreadpoolCpuSetMaskCount

Added in Windows 10 version 1903.

### DefaultThreadpoolThreadMaximum

Added in Windows 10 version 2004.

### HeapMemoryTypeMask

Added in Windows 11 version 22H2.

# Related Win32 structs
- [`STARTUPINFOA`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfoa)
- [`STARTUPINFOW`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfow)

# See also

* `RtlCreateProcessParameters`
* `RtlDestroyProcessParameters`
* `RtlNormalizeProcessParams`
* `RtlDeNormalizeProcessParams`
* `RtlCreateUserProcess`
* `PEB`
