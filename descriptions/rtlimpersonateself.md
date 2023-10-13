Impersonates a copy of the current process's token on the current thread.

# Parameters
 - `ImpersonationLevel` - the impersonation level to use.

# Implementation details
The function opens the current process token via `NtOpenProcessTokenEx`, duplicates it via `NtDuplicateToken`, and then impersonates it via `NtSetInformationThread` with `ThreadImpersonationToken`.

# Remarks
To reset impersonation, use `NtSetInformationThread` with `ThreadImpersonationToken` info class and a `NULL` token handle.

# Related Win32 API
 - [`ImpersonateSelf`](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-impersonateself)

# See also
 - `RtlImpersonateSelfEx`
 - `NtImpersonateThread`
 - `NtOpenThreadToken`
