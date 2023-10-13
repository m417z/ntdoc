Queries package identity information for a token. This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-rtlquerypackageidentity).

# Parameters
 - `TokenHandle` - a handle to a token or one of the supported pseudo-handles (see below). The handle must grant `TOKEN_QUERY` access.
 - `PackageFullName` - an optional pointer to user-allocated buffer that receives the full name of the package.
 - `PackageSize` - an optional pointer to a variable that specifies the size of the `PackageFullName` buffer in bytes and receives the number of bytes written.
 - `AppId` - an optional pointer to user-allocated buffer that receives the relative application user model ID of the package.
 - `AppIdSize` - an optional pointer to a variable that specifies the size of the `AppId` buffer in bytes and receives the number of bytes written.
 - `Packaged` - an optional pointer to a variable that receives whether the token has any package claim flags.

# Pseudo-handles
This function supports the following pseudo-handle values:
 - `NtCurrentProcessToken` - performs the query on the primary token of the calling process.
 - `NtCurrentThreadToken` - performs the query on the impersonation token of the calling thread. The function fails if the thread is not impersonating.
 - `NtCurrentThreadEffectiveToken` - performs the query on the impersonation token of the calling thread, if present. Otherwise, the function uses the primary token of the calling process.

# Notable return values
 - `STATUS_NOT_FOUND` - the token doesn't have package identity attributes.

# Implementation details
This function calls `NtQuerySecurityAttributesToken` and reads the values of the `WIN://SYSAPPID` and `WIN://PKG` attributes.

# Remarks
Alternatively to using `NtQuerySecurityAttributesToken`, you can also enumerate all security attributes via `NtQueryInformationToken` with `TokenSecurityAttributes` and retrieve the values from there.

# Required OS version
This function was introduced in Windows 8.

# See also
 - `RtlQueryPackageClaims`
 - `RtlQueryPackageIdentityEx`
 - `NtQuerySecurityAttributesToken`
 - `NtQueryInformationToken`
