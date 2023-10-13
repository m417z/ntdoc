Queries package identity and claim information for a token.

# Parameters
 - `TokenHandle` - a handle to a token or one of the supported pseudo-handles (see below). The handle must grant `TOKEN_QUERY` access.
 - `PackageFullName` - an optional pointer to user-allocated buffer that receives the full name of the package.
 - `PackageSize` - an optional pointer to a variable that specifies the size of the `PackageFullName` buffer in bytes and receives the number of bytes written.
 - `AppId` - an optional pointer to user-allocated buffer that receives the relative application user model ID of the package.
 - `AppIdSize` - an optional pointer to a variable that specifies the size of the `AppId` buffer in bytes and receives the number of bytes written.
 - `DynamicId` - an optional pointer to a variable that receives the dynamic ID of the application.
 - `PkgClaim` - an optional pointer to a variable that receives package claim flags.
 - `AttributesPresent` - an optional pointer to a variable that receives a bit mask of package-related security attributes present in the token.

# Pseudo-handles
This function supports the following pseudo-handle values:
 - `NtCurrentProcessToken` - performs the query on the primary token of the calling process.
 - `NtCurrentThreadToken` - performs the query on the impersonation token of the calling thread. The function fails if the thread is not impersonating.
 - `NtCurrentThreadEffectiveToken` - performs the query on the impersonation token of the calling thread, if present. Otherwise, the function uses the primary token of the calling process.

# Notable return values
 - `STATUS_NOT_FOUND` - the token doesn't have package identity attributes.

# Implementation details
This function calls `NtQuerySecurityAttributesToken` and reads the values of the `WIN://SYSAPPID` and `WIN://PKG` attributes. When the caller request the list of present attributes, it also checks for the presence of `WP://SKUID` and `XBOX://LI`.

# Remarks
Alternatively to using `NtQuerySecurityAttributesToken`, you can also enumerate all security attributes via `NtQueryInformationToken` with `TokenSecurityAttributes` and retrieve the values from there.

# Required OS version
This function was introduced in Windows 10 TH1 (1507).

# See also
 - `RtlQueryPackageIdentity`
 - `RtlQueryPackageIdentityEx`
 - `NtQuerySecurityAttributesToken`
 - `NtQueryInformationToken`
