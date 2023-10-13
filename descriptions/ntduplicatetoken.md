Creates a copy of a token. This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntduplicatetoken) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwduplicatetoken).

# Parameters
 - `ExistingTokenHandle` - a handle to an existing token. The handle must grant `TOKEN_DUPLICATE` access.
 - `DesiredAccess` - the access mask to provide on the returned handle. This value is usually `TOKEN_ALL_ACCESS`.
 - `ObjectAttributes` - an optional pointer to an `OBJECT_ATTRIBUTES` structure that specifies attributes of the handle/object. The `SecurityQualityOfService->ImpersonationLevel` field is especially meaningful for this function because it controls the impersonation level of the new token.
 - `EffectiveOnly` - a boolean indicating whether the system should copy all groups and privileges (set to `FALSE`) or only currently enabled ones (set to `TRUE`).
 - `Type` - the type of the new token, either primary or impersonation.
 - `NewTokenHandle` - a pointer to a variable that receives a handle to the new token.

# Access masks

Access mask               | Use
------------------------- | -----
`TOKEN_ASSIGN_PRIMARY`    | Allows creating processes with this token and assigning the token as primary via `NtSetInformationProcess` with `ProcessAccessToken`.
`TOKEN_DUPLICATE`         | Allows duplicating the token via `NtDuplicateToken`.
`TOKEN_IMPERSONATE`       | Allows impersonating the token via `NtSetInformationThread` with `ThreadImpersonationToken`.
`TOKEN_QUERY`             | Allows querying most information classes via `NtQueryInformationToken`.
`TOKEN_QUERY_SOURCE`      | Allows querying `TokenSource` via `NtQueryInformationToken`.
`TOKEN_ADJUST_PRIVILEGES` | Allows adjusting token privileges via `NtAdjustPrivilegesToken`
`TOKEN_ADJUST_GROUPS`     | Allows adjusting token privileges via `NtAdjustGroupsToken`
`TOKEN_ADJUST_DEFAULT`    | Allows setting most information classes via `NtSetInformationToken`.
`TOKEN_ADJUST_SESSIONID`  | Allows setting `TokenSessionId` via `NtSetInformationToken`.
`TOKEN_ALL_ACCESS_P`      | All of the above except for the `TOKEN_ADJUST_SESSIONID` right, plus standard rights.
`TOKEN_ALL_ACCESS`        | All of the above plus standard rights.

# Notable return values
 - `STATUS_BAD_IMPERSONATION_LEVEL` - the caller attempted to raise impersonation level of a token or convert an anonymous- or identification-level token into a primary token.

# Remarks
Here is a table describing which type/level conversions are allowed:

Source ↓ \ Destination → | Anonymous | Identification | Impersonation | Delegation | Primary
-----------------------: | :-------: | :------------: | :-----------: | :--------: | :-----:
Anonymous                |    Yes    |        No      |       No      |      No    |    No
Identification           |    Yes    |       Yes      |       No      |      No    |    No
Impersonation            |    Yes    |       Yes      |      Yes      |      No    |   Yes
Delegation               |    Yes    |       Yes      |      Yes      |     Yes    |   Yes
Primary                  |    Yes    |       Yes      |      Yes      |     Yes    |   Yes

Note that this function does not support token pseudo-handles such as `NtCurrentProcessToken`. If you want to duplicate the current process/thread token, you need to open it first.

To avoid retaining unused resources, call `NtClose` to close the returned handle when it is no longer required.

# Related Win32 API
 - [`DuplicateToken`](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-duplicatetoken)
 - [`DuplicateTokenEx`](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-duplicatetokenex)

# See also
 - `NtOpenProcessToken`
 - `NtOpenThreadToken`
 - `NtFilterToken`
 - `NtCreateLowBoxToken`
 - `NtQueryInformationToken`
 - `NtSetInformationToken`
 - `NtCompareTokens`
