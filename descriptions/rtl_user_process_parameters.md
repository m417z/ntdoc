This structure is [documented in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-rtl_user_process_parameters).

---

### MaximumLength

Should be set before call `RtlCreateProcessParameters`.

### Length

Length of valid structure.

### Flags

Currently these flags are known:

```cpp
// Means that the structure is normalized by RtlNormalizeProcessParams.
#define RTL_USER_PROCESS_PARAMETERS_NORMALIZED              0x01

// Source:
// https://github.com/arizvisa/ndk/blob/6851da4ab49ca07ddae29b6d4d255726ad04ef86/ndk/rtltypes.h#L39
#define RTL_USER_PROCESS_PARAMETERS_PROFILE_USER            0x02
#define RTL_USER_PROCESS_PARAMETERS_PROFILE_KERNEL          0x04
#define RTL_USER_PROCESS_PARAMETERS_PROFILE_SERVER          0x08
#define RTL_USER_PROCESS_PARAMETERS_UNKNOWN                 0x10
#define RTL_USER_PROCESS_PARAMETERS_RESERVE_1MB             0x20
#define RTL_USER_PROCESS_PARAMETERS_RESERVE_16MB            0x40
#define RTL_USER_PROCESS_PARAMETERS_CASE_SENSITIVE          0x80
#define RTL_USER_PROCESS_PARAMETERS_DISABLE_HEAP_CHECKS     0x100
#define RTL_USER_PROCESS_PARAMETERS_PROCESS_OR_1            0x200
#define RTL_USER_PROCESS_PARAMETERS_PROCESS_OR_2            0x400
#define RTL_USER_PROCESS_PARAMETERS_PRIVATE_DLL_PATH        0x1000
#define RTL_USER_PROCESS_PARAMETERS_LOCAL_DLL_PATH          0x2000
#define RTL_USER_PROCESS_PARAMETERS_IMAGE_KEY_MISSING       0x4000

// Documented by sixtyvividtails, source:
// https://x.com/sixtyvividtails/status/1719785195086266581
// This flag is needed on certain codepath for DotLocal to work. Set in
// PspSetupUserProcessAddressSpace from PspGlobalFlags.DevOverrideEnabled
// (bit0). And that comes off system-global (not per image) IFEO
// "DevOverrideEnable" (def absent). Old flag, but was mostly ignored.
#define RTL_USER_PROCESS_PARAMETERS_DEVOVERRIDE_ENABLED     0x8000

#define RTL_USER_PROCESS_PARAMETERS_NX                      0x20000
```

### DebugFlags

### ConsoleHandle

`HWND` to console window associated with process (if any).

### ConsoleFlags

### StdInputHandle

### StdOutputHandle

### StdErrorHandle

### CurrentDirectoryPath

Specified in DOS-like symbolic link path, ex: **"C:\\WinNT\\SYSTEM32"**

### CurrentDirectoryHandle

Handle to `FILE` object.

### DllPath

DOS-like paths separated by **';'** where system should search for DLL files.

### ImagePathName

Full path in DOS-like format to process'es file image.

### CommandLine

Command line.

### Environment

Pointer to environment block (see `RtlCreateEnvironment`).

### StartingPositionLeft

### StartingPositionTop

### Width

### Height

### CharWidth

### CharHeight

### ConsoleTextAttributes

### WindowFlags

### ShowWindowFlags

### WindowTitle

### DesktopName

Name of *WindowStation* and *Desktop* objects, where process is assigned.

### ShellInfo

### RuntimeData

### DLCurrentDirectory[0x20]

???

---

`RTL_USER_PROCESS_PARAMETERS` is located at address *0x20000* (for all processes created by call *WIN32 API* `CreateProcess`).

# Documented by

* ReactOS
* Tomasz Nowak

# See also

* `PEB`
* `RTL_DRIVE_LETTER_CURDIR`
* `RtlCreateEnvironment`
* `RtlCreateProcessParameters`
* `RtlCreateUserProcess`
* `RtlDeNormalizeProcessParams`
* `RtlDestroyProcessParameters`
* `RtlNormalizeProcessParams`
