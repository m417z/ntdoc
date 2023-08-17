Function `NtAdjustPrivilegesToken` is used to modify state of avaiable token's privileges, and it's descripted also in *Microsoft SDK* help as `AdjustTokenPrivileges`.

### TokenHandle

`HANDLE` to Token Object opened with `TOKEN_ADJUST_PRIVILEGES` access. If `PreviousPrivileges` parameter is non-NULL, also `TOKEN_QUERY` access is required.

### DisableAllPrivileges

If set, all accessable privileges are disabled, and rest of parameters below are ignored.

### TokenPrivileges

Pointer to `TOKEN_PRIVILEGES` structure containing array of privileges to adjust.

### PreviousPrivilegesLength

Length of `PreviousPrivileges` buffer, in bytes.

### PreviousPrivileges

Optionally pointer to `TOKEN_PRIVILEGES` structure filled by function with previous state of privileges specified by `TokenPrivileges` array.

### RequiredLength

If `PreviousPrivileges` buffer was to small, this parameter point to required size.

# Documented by

* Tomasz Nowak

# See also

* `NtAdjustGroupsToken`
* `NtCreateToken`
* `NtOpenProcessToken`
* `NtOpenThreadToken`
* `NtPrivilegeCheck`
* `NtQueryInformationToken`
* `TOKEN_PRIVILEGES`
