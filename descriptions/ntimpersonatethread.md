Copies an effective token of one thread onto another.

# Parameters
 - `ServerThreadHandle` - a handle to the server thread on which the system will impersonate a copy of the effective token of the client thread. The handle must grant `THREAD_IMPERSONATE` access. It can also be the `NtCurrentThread` pseudo-handle.
 - `ClientThreadHandle` - a handle to the client thread that provides the token. If this thread doesn't have a token, the system uses the primary token of the process containing this thread. The handle must grant `THREAD_DIRECT_IMPERSONATION` access. It can also be the `NtCurrentThread` pseudo-handle.
 - `SecurityQos` - a pointer to a structure that specifies the impersonation level to use.

# Notable return values
 - `STATUS_BAD_IMPERSONATION_LEVEL` - the requested impersonation level is higher than the impersonation level of the client thread's token.

# Remarks
Note that if the server process does not have `SeImpersonatePrivilege` enabled, the system might silently downgrade the token to the identification level of impersonation.

To reset impersonation, use `NtSetInformationThread` with `ThreadImpersonationToken` info class and a `NULL` token handle.

# See also
 - `NtOpenThread`
 - `NtOpenThreadToken`
 - `NtQueryInformationToken`
 - `NtDuplicateToken`
