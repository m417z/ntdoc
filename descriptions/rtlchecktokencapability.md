Determines if a token can pass access checks that require the specified capability SID.

# Parameters
 - `TokenHandle` - an optional handle to the token or one of the supported pseudo-handles (see below). The handle must grant `TOKEN_QUERY` access. The function uses (opens) the current thread's effective token if the caller passes `NULL` in this parameter.
 - `CapabilitySidToCheck` - a capability SID to check. The SID must satisfy the `RtlIsCapabilitySid` check.
 - `HasCapability` - a pointer to a variable that receives a boolean indicating whether the token has the capability.

# Pseudo-handles
This function supports the following pseudo-handle values:
 - `NtCurrentProcessToken` - performs the query on the primary token of the calling process.
 - `NtCurrentThreadToken` - performs the query on the impersonation token of the calling thread. The function fails if the thread is not impersonating.
 - `NtCurrentThreadEffectiveToken` - performs the query on the impersonation token of the calling thread, if present. Otherwise, the function uses the primary token of the calling process.

# Implementation details
This function creates a security descriptor with a DACL that grants access to the user SID and the capability SID and performs an access checks against it via `NtAccessCheck`. Therefore, unsandboxed tokens are considered to have any capability.

# Required OS version
This function was introduced in Windows 8.

# Related Win32 API
 - [`CheckTokenCapability`](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-checktokencapability)

# See also
 - `RtlCheckTokenMembership`
 - `RtlCheckTokenMembershipEx`
 - `RtlDeriveCapabilitySidsFromName`
