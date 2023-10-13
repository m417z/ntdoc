Creates a new token from scratch. Calling this function requires `SeCreateTokenPrivilege`.

# Parameters
 - `TokenHandle` - a pointer to a variable that receives a handle to the new token.
 - `DesiredAccess` - the access mask to provide on the returned handle. This value is usually `TOKEN_ALL_ACCESS`.
 - `ObjectAttributes` - an optional pointer to an `OBJECT_ATTRIBUTES` structure that specifies attributes of the handle/object. The `SecurityQualityOfService->ImpersonationLevel` field is especially meaningful for this function because it controls the impersonation level of the new token.
 - `Type` - the type of the new token, either primary or impersonation.
 - `AuthenticationId` - the LUID of the logon session to associate with the token.
 - `ExpirationTime` - the expiration time in the 100-nanosecond format to associate with the token.
 - `User` - a pointer to the user SID for the token.
 - `Groups` - a pointer to a collection of group SIDs to add into the token.
 - `Privileges` - a pointer to a collection of privilege LUIDs to add into the token.
 - `Owner` - an optional pointer to the default owner SID for newly created objects. The owner must be the user or a group with `SE_GROUP_OWNER` attribute.
 - `PrimaryGroup` - a pointer to the default primary group SID for newly created objects. The primary group must be the user or a group from the `Groups` parameter.
 - `DefaultDacl` - an optional pointer to the default discretionary ACL (DACL) for newly created objects.
 - `Source` - a pointer to a buffer that identifies the creator of the token. You can use `NtAllocateLocallyUniqueId` to reserve a unique ID for this parameter.

# Notable return values
 - `STATUS_NO_SUCH_LOGON_SESSION` - the provided logon session LUID does not exist.
 - `STATUS_INVALID_OWNER` - the provided owner is not the user or a group with a `SE_GROUP_OWNER` flag.
 - `STATUS_INVALID_PRIMARY_GROUP` - the provided primary group is not the user and is not in the list of groups.
 - `STATUS_INVALID_LABEL` - the SID marked as `SE_GROUP_INTEGRITY_ENABLED` exceeds the range of integrity levels.

# Remarks
You might want to enable the no-write-up policy on the new token after creation since the function does not do it.

To avoid retaining unused resources, call `NtClose` to close the returned handle when it is no longer required.

# See also
 - `NtCreateTokenEx`
 - `NtFilterToken`
 - `NtDuplicateToken`
