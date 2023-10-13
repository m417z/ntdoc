Impersonates the anonymous logon token on the specified thread.

# Parameters
 - `ThreadHandle` - a handle to the thread. The handle must grant `THREAD_IMPERSONATE` access.

# Remarks
Depending on the `EveryoneIncludesAnonymous` LSA setting, the anonymous logon token either has untrusted integrity with no group membership or low integrity with Everyone membership.

To reset impersonation, use `NtSetInformationThread` with `ThreadImpersonationToken` info class and a `NULL` token handle.

# Related Win32 API
 - [`ImpersonateAnonymousToken`](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-impersonateanonymoustoken)

# See also
 - `NtOpenThreadToken`
