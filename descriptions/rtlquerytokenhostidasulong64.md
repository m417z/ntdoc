Queries package host ID for a token.

# Parameters
 - `TokenHandle` - a handle to a token or one of the supported pseudo-handles (see below). The handle must grant `TOKEN_QUERY` access.
 - `HostId` - a pointer to a variable that receives package host ID.

# Pseudo-handles
This function supports the following pseudo-handle values:
 - `NtCurrentProcessToken` - performs the query on the primary token of the calling process.
 - `NtCurrentThreadToken` - performs the query on the impersonation token of the calling thread. The function fails if the thread is not impersonating.
 - `NtCurrentThreadEffectiveToken` - performs the query on the impersonation token of the calling thread, if present. Otherwise, the function uses the primary token of the calling process.

# Notable return values
 - `STATUS_NOT_FOUND` - the token doesn't have a package host ID attribute.

# Implementation details
This function calls `NtQuerySecurityAttributesToken` and reads the value of the `WIN://PKGHOSTID` security attribute.

# Remarks
Alternatively to using `NtQuerySecurityAttributesToken`, you can also enumerate all security attributes via `NtQueryInformationToken` with `TokenSecurityAttributes` and retrieve the value from there.

# Required OS version
This function was introduced in Windows 10 RS4 (1803).

# See also
 - `RtlQueryPackageClaims`
 - `RtlQueryPackageIdentity`
 - `NtQuerySecurityAttributesToken`
 - `NtQueryInformationToken`
