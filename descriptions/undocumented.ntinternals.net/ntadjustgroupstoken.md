Function `NtAdjustGroupsToken` modify state of one or more groups available for Token Object. See also description of similar *Win32 API* **AdjustTokenGroups** in *Win32 SDK*.

### TokenHandle

`HANDLE` to Token Object opened with `TOKEN_ADJUST_GROUPS` access.

### ResetToDefault

If set, groups are reset to token's defaults. In this case all other parameters are ignored.

### TokenGroups

Pointer to `TOKEN_GROUPS` structure containing groups to modify.

### PreviousGroupsLength

Specifies length of `PreviousGroups` buffer, in bytes.

### PreviousGroups

Optionally pointer to `TOKEN_GROUPS` buffer receiving information about modified groups before modification begins.

### RequiredLength

If `PreviousGroups` parameter is specified, and `PreviousGroupsLength` is to small, this value receives required length of buffer, in bytes.

# Documented by

* Tomasz Nowak

# See also

* `NtAdjustPrivilegesToken`
* `NtCreateToken`
* `NtOpenProcessToken`
* `NtOpenThreadToken`
* `NtQueryInformationToken`
* `NtSetInformationToken`
* `TOKEN_GROUPS`
