Opens a handle to a primary token of a process. This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntopenprocesstokenex) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwopenprocesstokenex).

# Parameters
 - `ProcessHandle` - a handle to the process or the `NtCurrentProcess` pseudo-handle. The handle must grant `PROCESS_QUERY_LIMITED_INFORMATION` access.
 - `DesiredAccess` - the requested access mask.
 - `HandleAttributes` - a set of flags from `OBJECT_ATTRIBUTES`.
 - `TokenHandle` - a pointer to a variable that receives a handle to the token.

# Access masks

Access mask               | Use
------------------------- | -----
`TOKEN_ASSIGN_PRIMARY`    | Allows creating processes with this token and assigning the token as primary via `NtSetInformationProcess` with `ProcessAccessToken`.
`TOKEN_DUPLICATE`         | Allows duplicating the token via `NtDuplicateToken`.
`TOKEN_IMPERSONATE`       | Allows impersonating the token via `NtSetInformationThread` with `ThreadImpersonationToken`.
`TOKEN_QUERY`             | Allows querying most information classes via `NtQueryInformationToken`.
`TOKEN_QUERY_SOURCE`      | Allows querying `TokenSource` via `NtQueryInformationToken`.
`TOKEN_ADJUST_PRIVILEGES` | Allows adjusting token privileges via `NtAdjustPrivilegesToken`
`TOKEN_ADJUST_GROUPS`     | Allows adjusting token privileges via `NtAdjustGroupsToken`
`TOKEN_ADJUST_DEFAULT`    | Allows setting most information classes via `NtSetInformationToken`.
`TOKEN_ADJUST_SESSIONID`  | Allows setting `TokenSessionId` via `NtSetInformationToken`.
`TOKEN_ALL_ACCESS_P`      | All of the above except for the `TOKEN_ADJUST_SESSIONID` right, plus standard rights.
`TOKEN_ALL_ACCESS`        | All of the above plus standard rights.

# Remarks
To avoid retaining unused resources, call `NtClose` to close the returned handle when it is no longer required.

Instead of opening the current process token for query, consider using the `NtCurrentProcessToken` pseudo-handle on Windows 8 and above.

If you don't want to specify custom handle attributes, you can use `NtOpenProcessToken`.

# Related Win32 API
 - [`OpenProcessToken`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocesstoken)

# See also
 - `NtCurrentProcessToken`
 - `NtOpenProcessToken`
 - `NtOpenThreadTokenEx`
 - `NtQueryInformationToken`
 - `NtSetInformationToken`
 - `NtDuplicateToken`
 - `NtOpenProcess`
