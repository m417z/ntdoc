Impersonates a copy of the current process's token on the current thread.

# Parameters
 - `ImpersonationLevel` - the impersonation level to use.
 - `AdditionalAccess` - an optional additional token access mask to grant on the returned handle.
 - `ThreadToken` - an optional pointer to a variable that receives a handle to the new token.

# Implementation details
The function opens the current process token via `NtOpenProcessTokenEx`, duplicates it via `NtDuplicateToken`, and then impersonates it via `NtSetInformationThread` with `ThreadImpersonationToken`.

# Remarks
To reset impersonation, use `NtSetInformationThread` with `ThreadImpersonationToken` info class and a `NULL` token handle.

To avoid retaining unused resources, call `NtClose` to close the returned handle when it is no longer required.

# Related Win32 API
 - [`ImpersonateSelf`](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-impersonateself)

# See also
 - `RtlImpersonateSelf`
 - `NtImpersonateThread`
 - `NtOpenThreadToken`
