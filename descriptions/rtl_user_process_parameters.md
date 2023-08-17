### MaximumLength

Should be set before call `RtlCreateProcessParameters`.

### Length

Length of valid structure.

### Flags

Currently only one flag is known:

```
PPF_NORMALIZED  (1)     // Means that structure is normalized by call RtlNormalizeProcessParams
```

### DebugFlags

### ConsoleHandle

`HWND` to console window associated with process (if any).

### ConsoleFlags

### StdInputHandle

### StdOutputHandle

### StdErrorHandle

### CurrentDirectoryPath

Specified in DOS-like symbolic link path, ex: **"C:/WinNT/SYSTEM32"**

### CurrentDirectoryHandle

Handle to `FILE` object.

### DllPath

DOS-like paths separated by **';'** where system shoult search for DLL files.

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
