Creates a restricted (filtered) copy of a token.

# Parameters
 - `ExistingTokenHandle` - a handle to an existing token. The handle must grant at least `TOKEN_DUPLICATE` access.
 - `Flags` - a set of flags that control behavior of the function (see description below).
 - `SidsToDisable` - an optional pointer to a collection of SIDs to be disabled and marked as use-for-deny-only in the new token.
 - `PrivilegesToDelete` - an optional pointer to a collection of privileges to be removed from the new token.
 - `RestrictedSids` - an optional pointer to a collection of (arbitrary) restricting SIDs that will be used to perform a secondary access check.
 - `NewTokenHandle` - a pointer to a variable that receives a handle to the filtered token. The new handle grants the same access rights as the provided existing token handle.

# Supported flags
 - `DISABLE_MAX_PRIVILEGE` (0x01) - remove all privileges from the new token except for `SeChangeNotifyPrivilege`.
 - `SANDBOX_INERT` (0x02) - allow the new token to bypass Software Restriction Policies and AppLocker rules. Note that the caller must have system-level privileges; otherwise, the function silently ignores this flag. To verify that the new token received the sandbox inert status, use `NtQueryInformationToken` with `TokenSandBoxInert` info class.
 - `LUA_TOKEN` (0x04) - perform UAC-like filtration by disabling administrative-equivalent SIDs (see `RtlIsElevatedRid`) and privileges.
 - `WRITE_RESTRICTED` (0x08) - use the secondary access check (against restricting SIDs) only when evaluating parts of `GENERIC_WRITE` access.

# Remarks
To avoid retaining unused resources, call `NtClose` to close the returned handle when it is no longer required.

It is often convenient to use a full access handle for the existing (input) token because the system copies the granted access rights from the provided handle. Alternatively, you can reopen the new handle after filtration via `NtDuplicateObject`.

Note that this function does not support token pseudo-handles such as `NtCurrentProcessToken`. If you want to filter the current process/thread token, you need to open it first.

# Related Win32 API
 - [`CreateRestrictedToken`](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-createrestrictedtoken)

# See also
 - `NtDuplicateToken`
 - `NtCreateLowBoxToken`
 - `NtOpenProcessToken`
 - `NtOpenThreadToken`
 - `NtQueryInformationToken`
 - `NtSetInformationToken`
 - `RtlCheckTokenMembershipEx`
