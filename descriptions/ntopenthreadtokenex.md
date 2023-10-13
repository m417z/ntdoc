Opens a handle to an impersonation token of a thread. This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntopenthreadtokenex) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwopenthreadtokenex).

# Parameters
 - `ThreadHandle` - a handle to the thread or the `NtCurrentThread` pseudo-handle. The handle must grant `THREAD_QUERY_LIMITED_INFORMATION` access.
 - `DesiredAccess` - the requested access mask.
 - `OpenAsSelf` - a boolean determining whether the system should perform the access check on the target token using the effective security context of the calling thread (`FALSE`) or ignore impersonation and use the security context of the calling process (`TRUE`).
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

# Notable return values
 - `STATUS_NO_TOKEN` - the thread is not impersonating at the moment.
 - `STATUS_CANT_OPEN_ANONYMOUS` - the caller attempted to open a token that has anonymous level of impersonation.

# Remarks
To avoid retaining unused resources, call `NtClose` to close the returned handle when it is no longer required.

Instead of opening the current thread token for query, consider using the `NtCurrentThreadToken` pseudo-handle on Windows 8 and above.

If you don't want to specify custom handle attributes, you can use `NtOpenThreadToken`.

To set a thread token, use `NtSetInformationThread` with `ThreadImpersonationToken`. See `THREADINFOCLASS` for more details.

# Related Win32 API
 - [`OpenThreadToken`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openthreadtoken)

# See also
 - `NtCurrentThreadToken`
 - `NtCurrentThreadEffectiveToken`
 - `NtOpenThreadToken`
 - `NtOpenProcessTokenEx`
 - `NtQueryInformationToken`
 - `NtSetInformationToken`
 - `NtDuplicateToken`
 - `NtOpenThread`
