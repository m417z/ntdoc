Determines if a token can pass access checks against the specified SID.

# Parameters
 - `TokenHandle` - an optional handle to the token or one of the supported pseudo-handles (see below). The handle must grant `TOKEN_QUERY` access. The function uses (opens) the current thread's effective token if the caller passes `NULL` in this parameter.
 - `SidToCheck` - a SID to test for membership.
 - `IsMember` - a pointer to a variable that receives a boolean indicating whether the token has the SID.

# Pseudo-handles
This function supports the following pseudo-handle values:
 - `NtCurrentProcessToken` - performs the query on the primary token of the calling process.
 - `NtCurrentThreadToken` - performs the query on the impersonation token of the calling thread. The function fails if the thread is not impersonating.
 - `NtCurrentThreadEffectiveToken` - performs the query on the impersonation token of the calling thread, if present. Otherwise, the function uses the primary token of the calling process.

# Implementation details
This function calls `RtlCheckTokenMembershipEx` with flags set to 0.

# Required OS version
This function was introduced in Windows 8.

# Related Win32 API
 - [`CheckTokenMembership`](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-checktokenmembership)

# See also
 - `RtlCheckTokenMembershipEx`
 - `RtlCheckTokenCapability`
