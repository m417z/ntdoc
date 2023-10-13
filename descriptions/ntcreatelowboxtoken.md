Creates an AppContainer/LowBox token based on an existing token. This function is [documented in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/secauthz/ntcreatelowboxtoken).

# Parameters
 - `TokenHandle` - a pointer to a variable that receives a handle to the new token.
 - `ExistingTokenHandle` - a handle to an existing token to use as a template. The handle must grant `TOKEN_DUPLICATE` access.
 - `DesiredAccess` - the access mask to provide on the returned handle. This value is usually `TOKEN_ALL_ACCESS`.
 - `ObjectAttributes` - an optional pointer to an `OBJECT_ATTRIBUTES` structure that specifies attributes of the handle/object.
 - `PackageSid` - the AppContainer package SID to associate with the token. The SID must satisfy the `RtlIsPackageSid` check.
 - `CapabilityCount` - the number of capabilities passed in the `Capabilities` parameter.
 - `Capabilities` - an optional pointer to a collection of capability SIDs to add to the token. Each SID must satisfy the `RtlIsCapabilitySid` check.
 - `HandleCount` - the number of handles passed in the `Handles` parameter.
 - `Handles` - an optional pointer to a collection of handles to reference in the token to extend their lifetime. Currently, the only supported kernel types are `Directory`, `SymbolicLink`, and `File`.

# Notable return values
 - `STATUS_BAD_IMPERSONATION_LEVEL` - the provided token is an impersonation token of either anonymous or identification level.
 - `STATUS_INVALID_PACKAGE_SID_LENGTH` - the package SID does not have the correct length.

# Remarks
The function always returns a primary token.

Note that this function does not support token pseudo-handles such as `NtCurrentProcessToken`. If you want to filter the current process/thread token, you need to open it first.

AppContainer tokens perform an additional access check against the corresponding AppContainer/Package SID, `ALL APPLICATION PACKAGES` SID (`S-1-15-2-1`), and the list of provided capabilities. It is also possible to convert such tokens into Less Privileged AppContainer (LPAC) via a dedicated security attribute. See `TOKEN_INFORMATION_CLASS` value `TokenIsLessPrivilegedAppContainer` for more details on LPAC.

# Required OS version
This function was introduced in Windows 8.

# See also
 - `NtFilterToken`
 - `NtDuplicateToken`
 - `NtCreateToken`
 - `RtlDeriveCapabilitySidsFromName`
 - `RtlCheckTokenCapability`
