### ImagePath

Full path to executable image, in NT format (ex: **"\\??\\C:\\WinNT\\SYSTEM32\\cmd.exe"**).

### ObjectAttributes

Used in File object creation. Valid are `OBJ_INHERIT` and `OBJ_CASE_INSENSITIVE`.

### ProcessParameters

Normalized `RTL_USER_PROCESS_PARAMETERS` structure pointer. See `RtlCreateProcessParameters` for more information.

### ParentProcess

Handle to object Process, opened with `PROCESS_CREATE_PROCESS` access.

### ProcessInformation

Pointer to user-allocated structure `RTL_USER_PROCESS_INFORMATION`.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `RTL_USER_PROCESS_INFORMATION`
* `RTL_USER_PROCESS_PARAMETERS`
* `RtlCreateProcessParameters`
* `RtlCreateUserThread`
* `RtlNormalizeProcessParams`
