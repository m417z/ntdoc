This enumeration defines types of information that can be queried or set for tokens. The enumeration is partially documented [in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/ne-ntifs-_token_information_class) and [in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/api/winnt/ne-winnt-token_information_class).

# Applicable to
 - `NtQueryInformationThread`
 - `NtSetInformationThread`

# Members

## TokenUser (1)
Retrieves the user SID associated with the token.

|                 | Query                           | Set
| --------------- | ------------------------------- | ---
| Type            | `TOKEN_USER` or `SE_TOKEN_USER` | N/A
| Required access | `TOKEN_QUERY`                   | N/A

### Remarks
The user SID is considered enabled for granting access checks when its attributes don't include the `SE_GROUP_USE_FOR_DENY_ONLY` flag. Note that this behavior differs from token groups which explicitly require `SE_GROUP_ENABLED` flag to be set. In other words, an enabled user has attributes set to zero; a filtered/disabled user (see `NtFilterToken`) has attributes set to `SE_GROUP_USE_FOR_DENY_ONLY`.

## TokenGroups (2)
Retrieves the list of SIDs (group membership) associated with the token.

|                 | Query          | Set
| --------------- | -------------- | ---
| Type            | `TOKEN_GROUPS` | N/A
| Required access | `TOKEN_QUERY`  | N/A

### Remarks
A group SID is considered enabled for granting access checks when its attributes include `SE_GROUP_ENABLED`. A group SID is considered enabled for denying access checks when its attributes include either `SE_GROUP_ENABLED` or `SE_GROUP_USE_FOR_DENY_ONLY`.

### See also
 - `NtFilterToken`
 - `NtAdjustGroupsToken`

## TokenPrivileges (3)
Retrieves the list of privileges present in the token.

|                 | Query              | Set
| --------------- | ------------------ | ---
| Type            | `TOKEN_PRIVILEGES` | N/A
| Required access | `TOKEN_QUERY`      | N/A

### Remarks
A privilege is considered enabled for access checks when its attributes include `SE_PRIVILEGE_ENABLED`.

### See also
 - `NtFilterToken`
 - `NtAdjustPrivilegesToken`

## TokenOwner (4)
Retrieves or sets the default owner SID for newly created objects.

|                 | Query         | Set
| --------------- | ------------- | ---
| Type            | `TOKEN_OWNER` | `TOKEN_OWNER`
| Required access | `TOKEN_QUERY` | `TOKEN_ADJUST_DEFAULT`

### Remarks
When changing the value, the provided SID must be either the user of the token or one of the groups that have the `SE_GROUP_OWNER` flag. Otherwise, the request fails with `STATUS_INVALID_OWNER`.

### See also
 - `RtlGetOwnerSecurityDescriptor`
 - `RtlSetOwnerSecurityDescriptor`

## TokenPrimaryGroup (5)
Retrieves or sets the default primary group SID for newly created objects.

|                 | Query                 | Set
| --------------- | --------------------- | ---
| Type            | `TOKEN_PRIMARY_GROUP` | `TOKEN_PRIMARY_GROUP`
| Required access | `TOKEN_QUERY`         | `TOKEN_ADJUST_DEFAULT`

### Remarks
When changing the value, the provided SID must be either the user or one of the groups of the token. Otherwise, the request fails with `STATUS_INVALID_PRIMARY_GROUP`.

### See also
 - `RtlGetGroupSecurityDescriptor`
 - `RtlSetGroupSecurityDescriptor`

## TokenDefaultDacl (6)
Retrieves or sets the default discretionary ACL (DACL) for newly created objects.

|                 | Query                | Set
| --------------- | -------------------- | ---
| Type            | `TOKEN_DEFAULT_DACL` | `TOKEN_DEFAULT_DACL`
| Required access | `TOKEN_QUERY`        | `TOKEN_ADJUST_DEFAULT`

### See also
 - `RtlGetDaclSecurityDescriptor`
 - `RtlSetDaclSecurityDescriptor`

## TokenSource (7)
Retrieves the string and LUID that identify the source of the token.

|                 | Query                | Set
| --------------- | -------------------- | ---
| Type            | `TOKEN_SOURCE`       | N/A
| Required access | `TOKEN_QUERY_SOURCE` | N/A

### See also
 - `NtCreateToken`

## TokenType (8)
Determines whether the token is a primary token or an impersonation token.

|                 | Query         | Set
| --------------- | ------------- | ---
| Type            | `TOKEN_TYPE`  | N/A
| Required access | `TOKEN_QUERY` | N/A

### See also
 - `NtDuplicateToken`

## TokenImpersonationLevel (9)
Retrieves the level of impersonation for impersonation-type tokens.

|                 | Query                          | Set
| --------------- | ------------------------------ | ---
| Type            | `SECURITY_IMPERSONATION_LEVEL` | N/A
| Required access | `TOKEN_QUERY`                  | N/A

### See also
 - `NtDuplicateToken`

## TokenStatistics (10)
Retrieves various statistics information for the token such its type, the number of groups and privileges, and the associated logon session LUID.

|                 | Query              | Set
| --------------- | ------------------ | ---
| Type            | `TOKEN_STATISTICS` | N/A
| Required access | `TOKEN_QUERY`      | N/A

## TokenRestrictedSids (11)
Retrieves the list of restricting groups for the secondary access check added via `NtFilterToken`.

|                 | Query          | Set
| --------------- | -------------- | ---
| Type            | `TOKEN_GROUPS` | N/A
| Required access | `TOKEN_QUERY`  | N/A

### See also
 - `NtFilterToken`

## TokenSessionId (12)
Retrieves or sets the session ID of the token.

|                    | Query         | Set
| ------------------ | ------------- | ---
| Type               | `ULONG`       | `ULONG`
| Required access    | `TOKEN_QUERY` | `TOKEN_ADJUST_DEFAULT \| TOKEN_ADJUST_SESSIONID`
| Required privilege | None          | `SeTcbPrivilege`

### Remarks
Attempting to change the session ID of a token that is assigned as a primary process token results in `STATUS_TOKEN_ALREADY_IN_USE`.

## TokenGroupsAndPrivileges (13)
Retrieves the list of SIDs, restricting SIDs, and privileges present in the token.

|                 | Query                         | Set
| --------------- | ----------------------------- | ---
| Type            | `TOKEN_GROUPS_AND_PRIVILEGES` | N/A
| Required access | `TOKEN_QUERY`                 | N/A

### See also
 - `NtFilterToken`
 - `NtAdjustPrivilegesToken`
 - `NtAdjustGroupsToken`

## TokenSessionReference (14)
Allows releasing token's reference to the associated logon session.

|                    | Query | Set
| ------------------ | ----- | ---
| Type               | N/A   | `ULONG` (`0`) or `BOOL` (`FALSE`)
| Required access    | N/A   | N/A
| Required privilege | None  | `SeTcbPrivilege`

## TokenSandBoxInert (15)
Retrieves whether the token allows bypassing Software Restriction Policies and AppLocker rules. This info class checks for the `TOKEN_SANDBOX_INERT` token flag.

|                 | Query             | Set
| --------------- | ----------------- | ---
| Type            | `ULONG` or `BOOL` | N/A
| Required access | `TOKEN_QUERY`     | N/A

### See also
 - `NtFilterToken`

## TokenAuditPolicy (16)
Retrieves and sets the per-user audit policy overrides for the token.

|                    | Query                 | Set
| ------------------ | --------------------- | ---
| Type               | `TOKEN_AUDIT_POLICY`  | `TOKEN_AUDIT_POLICY`
| Required access    | `TOKEN_QUERY`         | `TOKEN_ADJUST_DEFAULT`
| Required privilege | `SeSecurityPrivilege` | `SeTcbPrivilege`

### Remarks
Audit policy overrides can only be set once per token. Subsequent attempts to modify this information result in `STATUS_INVALID_PARAMETER`.

## TokenOrigin (17)
Retrieves and adjusts the LUID of the originating logon session for the token.

|                    | Query          | Set
| ------------------ | -------------- | ---
| Type               | `TOKEN_ORIGIN` | `TOKEN_ORIGIN`
| Required access    | `TOKEN_QUERY`  | `TOKEN_ADJUST_DEFAULT`
| Required privilege | None           | `SeTcbPrivilege`

### Related Win32 API
 - [`LsaLogonUser`](https://learn.microsoft.com/en-us/windows/win32/api/ntsecapi/nf-ntsecapi-lsalogonuser)

## TokenElevationType (18)
Determines the elevation type of the logon session associated with the token.

|                 | Query                  | Set
| --------------- | ---------------------- | ---
| Type            | `TOKEN_ELEVATION_TYPE` | N/A
| Required access | `TOKEN_QUERY`          | N/A

### Remarks
This information is not per se a property of the token but rather its logon session.

## TokenLinkedToken (19)
Opens a copy of a token from the linked logon session or links logon sessions of the two tokens.

|                    | Query                | Set
| ------------------ | -------------------- | ---
| Type               | `TOKEN_LINKED_TOKEN` | `TOKEN_LINKED_TOKEN`
| Required access    | `TOKEN_QUERY`        | `TOKEN_ADJUST_DEFAULT \| TOKEN_QUERY` (on both handles)
| Required privilege | None                 | `SeCreateTokenPrivilege`

### Remarks
Querying this information class returns a primary token when the caller has `SeTcbPrivilege` enabled and an identification-level token otherwise.

Settings linked token requires both tokens to be primary and belong to logon sessions that are not already linked. The token passed in the first parameter to `NtSetInformationToken` provides the logon session to be marked as elevated while the token passed via the buffer becomes the limited logon session.

## TokenElevation (20)
Determines whether the token is elevated by checking if it contains any sensitive groups (see `RtlIsElevatedRid`) or privileges.

|                 | Query             | Set
| --------------- | ----------------- | ---
| Type            | `TOKEN_ELEVATION` | N/A
| Required access | `TOKEN_QUERY`     | N/A

## TokenHasRestrictions (21)
Determines whether the token has been filtered via `NtFilterToken`. This info class checks token flags for `TOKEN_IS_RESTRICTED | TOKEN_IS_FILTERED`.

|                 | Query             | Set
| --------------- | ----------------- | ---
| Type            | `ULONG` or `BOOL` | N/A
| Required access | `TOKEN_QUERY`     | N/A

### See also
 - `NtFilterToken`

## TokenAccessInformation (22)
Retrieves various access-related information such as the SID hashes, privileges, and token flags.

|                 | Query                      | Set
| --------------- | -------------------------- | ---
| Type            | `TOKEN_ACCESS_INFORMATION` | N/A
| Required access | `TOKEN_QUERY`              | N/A

## TokenVirtualizationAllowed (23)
Retrieves or sets whether the token allows enabling UAC filesystem and registry virtualization. This info class accesses the `TOKEN_VIRTUALIZE_ALLOWED` token flag.

|                    | Query             | Set
| ------------------ | ----------------- | ---
| Type               | `ULONG` or `BOOL` | `ULONG` or `BOOL`
| Required access    | `TOKEN_QUERY`     | `TOKEN_ADJUST_DEFAULT`
| Required privilege | None              | `SeCreateTokenPrivilege`

## TokenVirtualizationEnabled (24)
Retrieves or sets whether UAC filesystem and registry virtualization is enabled for the token. This info class accesses the `TOKEN_VIRTUALIZE_ENABLED` token flag.

|                    | Query             | Set
| ------------------ | ----------------- | ---
| Type               | `ULONG` or `BOOL` | `ULONG` or `BOOL`
| Required access    | `TOKEN_QUERY`     | `TOKEN_ADJUST_DEFAULT`

## TokenIntegrityLevel (25)
Retrieves or changes the integrity level of the token.

|                    | Query                   | Set
| ------------------ | ----------------------- | ---
| Type               | `TOKEN_MANDATORY_LABEL` | `TOKEN_MANDATORY_LABEL`
| Required access    | `TOKEN_QUERY`           | `TOKEN_ADJUST_DEFAULT`
| Required privilege | None                    | None to lower; `SeTcbPrivilege` to raise

### Remarks
Attempting to raise integrity level of a token that is assigned as a primary process token results in `STATUS_TOKEN_ALREADY_IN_USE`.

Lowering integrity automatically disables incompatible privileges and prevents them from being enabled.

## TokenUIAccess (26)
Retrieves or sets whether the token allows bypassing User Interface Privilege Isolation (UIPI). This info class accesses the `TOKEN_UIACCESS` token flag.

|                    | Query             | Set
| ------------------ | ----------------- | ---
| Type               | `ULONG` or `BOOL` | `ULONG` or `BOOL`
| Required access    | `TOKEN_QUERY`     | `TOKEN_ADJUST_DEFAULT`
| Required privilege | None              | None to disable; `SeTcbPrivilege` to enable

## TokenMandatoryPolicy (27)
Retrieves or sets mandatory policy for the token.

|                    | Query                    | Set
| ------------------ | ------------------------ | ---
| Type               | `TOKEN_MANDATORY_POLICY` | `TOKEN_MANDATORY_POLICY`
| Required access    | `TOKEN_QUERY`            | `TOKEN_ADJUST_DEFAULT`
| Required privilege | None                     | `SeTcbPrivilege`

### Remarks
Attempting to change mandatory policy of a token that is assigned as a primary process token results in `STATUS_TOKEN_ALREADY_IN_USE`.

## TokenLogonSid (28)
Finds (the first) logon SID (a group with `SE_GROUP_LOGON_ID` flag) in the list of token groups.

|                 | Query          | Set
| --------------- | -------------- | ---
| Type            | `TOKEN_GROUPS` | N/A
| Required access | `TOKEN_QUERY`  | N/A

## TokenIsAppContainer (29)
Determines whether the token is an AppContainer/LowBox token.

|                 | Query             | Set
| --------------- | ----------------- | ---
| Type            | `ULONG` or `BOOL` | N/A
| Required access | `TOKEN_QUERY`     | N/A
| Minimal version | Windows 8         | N/A

### Remarks
AppContainer tokens perform an additional access check against the corresponding AppContainer SID, `ALL APPLICATION PACKAGES` SID (`S-1-15-2-1`), and the list of provided capabilities.

### See also
 - `NtCreateLowBoxToken`

## TokenCapabilities (30)
Retrieves the list of capability SIDs associated with the token.

|                 | Query          | Set
| --------------- | -------------- | ---
| Type            | `TOKEN_GROUPS` | N/A
| Required access | `TOKEN_QUERY`  | N/A
| Minimal version | Windows 8      | N/A

### See also
 - `NtCreateLowBoxToken`

## TokenAppContainerSid (31)
Retrieves the AppContainer/Package SID associated with a LowBox token.

|                 | Query                            | Set
| --------------- | -------------------------------- | ---
| Type            | `TOKEN_APPCONTAINER_INFORMATION` | N/A
| Required access | `TOKEN_QUERY`                    | N/A
| Minimal version | Windows 8                        | N/A

### Remarks
AppContainer tokens perform an additional access check against the AppContainer SID, `ALL APPLICATION PACKAGES` SID (`S-1-15-2-1`), and the list of provided capabilities.

### See also
 - `NtCreateLowBoxToken`

## TokenAppContainerNumber (32)
Retrieves the token AppContainer/LowBox number.

|                 | Query         | Set
| --------------- | ------------- | ---
| Type            | `ULONG`       | N/A
| Required access | `TOKEN_QUERY` | N/A
| Minimal version | Windows 8     | N/A

## TokenUserClaimAttributes (33)
Retrieves the list of user claim attributes associated with the token.

|                 | Query                                   | Set
| --------------- | --------------------------------------- | ---
| Type            | `CLAIM_SECURITY_ATTRIBUTES_INFORMATION` | N/A
| Required access | `TOKEN_QUERY`                           | N/A
| Minimal version | Windows 8                               | N/A

### See also
 - `NtCreateTokenEx`

## TokenDeviceClaimAttributes (34)
Retrieves the list of device claim attributes associated with the token.

|                 | Query                                   | Set
| --------------- | --------------------------------------- | ---
| Type            | `CLAIM_SECURITY_ATTRIBUTES_INFORMATION` | N/A
| Required access | `TOKEN_QUERY`                           | N/A
| Minimal version | Windows 8                               | N/A

### See also
 - `NtCreateTokenEx`

## TokenRestrictedUserClaimAttributes (35)
Retrieves the list of restricted user claim attributes associated with the token.

|                 | Query                                   | Set
| --------------- | --------------------------------------- | ---
| Type            | `CLAIM_SECURITY_ATTRIBUTES_INFORMATION` | N/A
| Required access | `TOKEN_QUERY`                           | N/A
| Minimal version | Windows 8                               | N/A

### See also
 - `NtFilterTokenEx`

## TokenRestrictedDeviceClaimAttributes (36)
Retrieves the list of restricted device claim attributes associated with the token.

|                 | Query                                   | Set
| --------------- | --------------------------------------- | ---
| Type            | `CLAIM_SECURITY_ATTRIBUTES_INFORMATION` | N/A
| Required access | `TOKEN_QUERY`                           | N/A
| Minimal version | Windows 8                               | N/A

### See also
 - `NtFilterTokenEx`

## TokenDeviceGroups (37)
Retrieves the list of device group SIDs device claim attributes associated with the token.

|                 | Query          | Set
| --------------- | -------------- | ---
| Type            | `TOKEN_GROUPS` | N/A
| Required access | `TOKEN_QUERY`  | N/A
| Minimal version | Windows 8      | N/A

### See also
 - `NtCreateTokenEx`

## TokenRestrictedDeviceGroups (38)
Retrieves the list of restricted device group SIDs device claim attributes associated with the token.

|                 | Query          | Set
| --------------- | -------------- | ---
| Type            | `TOKEN_GROUPS` | N/A
| Required access | `TOKEN_QUERY`  | N/A
| Minimal version | Windows 8      | N/A

### See also
 - `NtFilterTokenEx`

## TokenSecurityAttributes (39)
Retrieves or modifies the list of security attributes associated with the token.

|                    | Query                                   | Set
| ------------------ | --------------------------------------- | ---
| Type               | `TOKEN_SECURITY_ATTRIBUTES_INFORMATION` | `TOKEN_SECURITY_ATTRIBUTES_AND_OPERATION_INFORMATION`
| Required access    | `TOKEN_QUERY`                           | `TOKEN_ADJUST_DEFAULT`
| Required privilege | None                                    | `SeTcbPrivilege`
| Minimal version    | Windows 8                               | Windows 8

### See also
 - `NtQuerySecurityAttributesToken`

## TokenIsRestricted (40)
Determines if the token is restricted (i.e., requires a secondary access check against the list of restricting SIDs). This info class checks token flags for `TOKEN_IS_RESTRICTED | TOKEN_WRITE_RESTRICTED`.

|                 | Query             | Set
| --------------- | ----------------- | ---
| Type            | `ULONG` or `BOOL` | N/A
| Required access | `TOKEN_QUERY`     | N/A
| Minimal version | Windows 8         | N/A

### See also
 - `NtFilterToken`

## TokenProcessTrustLevel (41)
Retrieves the process trust level (protection/PPL) SID associated with the token.

|                 | Query                       | Set
| --------------- | --------------------------- | ---
| Type            | `TOKEN_PROCESS_TRUST_LEVEL` | N/A
| Required access | `TOKEN_QUERY`               | N/A
| Minimal version | Windows 8.1                 | N/A

### See also
 - `PS_ATTRIBUTE_PROTECTION_LEVEL`

## TokenPrivateNameSpace (42)
This info class accesses the `TOKEN_PRIVATE_NAMESPACE` token flag.

|                    | Query                 | Set
| ------------------ | --------------------- | ---
| Type               | `ULONG` or `BOOL`     | `ULONG` or `BOOL`
| Required access    | `TOKEN_QUERY`         | `TOKEN_ADJUST_DEFAULT`
| Required privilege | None                  | `SeTcbPrivilege`
| Minimal version    | Windows 10 TH1 (1507) | Windows 10 TH1 (1507)

## TokenSingletonAttributes (43)
Retrieves the list of singleton attributes associated with the token.

|                 | Query                                   | Set
| --------------- | --------------------------------------- | ---
| Type            | `TOKEN_SECURITY_ATTRIBUTES_INFORMATION` | N/A
| Required access | `TOKEN_QUERY`                           | N/A
| Minimal version | Windows 10 RS1 (1607)                   | N/A

## TokenBnoIsolation (44)
Retrieves the Base Named Object Isolation rules for the token.

|                 | Query                             | Set
| --------------- | --------------------------------- | ---
| Type            | `TOKEN_BNO_ISOLATION_INFORMATION` | N/A
| Required access | `TOKEN_QUERY`                     | N/A
| Minimal version | Windows 10 RS2 (1703)             | N/A

### See also
 - `PROC_THREAD_ATTRIBUTE_BNO_ISOLATION`

## TokenChildProcessFlags (45)
Removes the child process creation restriction from the token.

|                    | Query | Set
| ------------------ | ----- | ---
| Type               | N/A   | `ULONG` (`0`) or `BOOL` (`FALSE`)
| Required access    | N/A   | `TOKEN_ADJUST_DEFAULT`
| Minimal version    | N/A   | Windows 10 RS3 (1709)
| Required privilege | N/A   | `SeTcbPrivilege`

### Remarks
To check the existing child process creation restrictions, query token flags and test them for `TOKEN_NO_CHILD_PROCESS`, `TOKEN_NO_CHILD_PROCESS_UNLESS_SECURE`, and `TOKEN_AUDIT_NO_CHILD_PROCESS`.

## See also
 - `NtQueryInformationProcess` with `PROCESSINFOCLASS` value of `ProcessChildProcessInformation` (73)
 - `PS_ATTRIBUTE_CHILD_PROCESS_POLICY`

## TokenIsLessPrivilegedAppContainer (46)
Determines if the token is a Less Privileged AppContainer (LPAC) token.

|                 | Query                  | Set
| --------------- | ---------------------- | ---
| Type            | `ULONG` or `BOOL`      | N/A
| Required access | `TOKEN_QUERY`          | N/A
| Minimal version | Windows 10 RS5 (1809)  | N/A

### Remarks
The LPAC flag replaces a regular AppContainer access check against `ALL APPLICATION PACKAGES` (`S-1-15-2-1`) with a check against `ALL RESTRICTED APPLICATION PACKAGES` (`S-1-15-2-2`).

Alternatively, you can query the `WIN://NOALLAPPPKG` attribute via the `NtQuerySecurityAttributesToken` function or the `TokenSecurityAttributes` info class and test for a non-zero value.

### See also
 - `PS_ATTRIBUTE_ALL_APPLICATION_PACKAGES_POLICY`

## TokenIsSandboxed (47)
Determines if the token is considered sandboxed (i.e., has integrity level below medium).

|                 | Query                  | Set
| --------------- | ---------------------- | ---
| Type            | `ULONG` or `BOOL`      | N/A
| Required access | `TOKEN_QUERY`          | N/A
| Minimal version | Windows 10 19H1 (1903) | N/A

### See also
 - `RtlCheckSandboxedToken`

## TokenIsAppSilo (48)
Determines if the token has the AppSilo capability (`S-1-15-3-65536`).

|                 | Query             | Set
| --------------- | ----------------- | ---
| Type            | `ULONG` or `BOOL` | N/A
| Required access | `TOKEN_QUERY`     | N/A
| Minimal version | Windows 11 22H2   | N/A

### Remarks
This info class value was previously known as `TokenOriginatingProcessTrustLevel`.

### See also
 - `RtlIsCapabilitySid`
 - `RtlDeriveCapabilitySidsFromName`

## TokenLoggingInformation (49)
Returns logging information associated with the token.

|                 | Query                       | Set
| --------------- | --------------------------- | ---
| Type            | `TOKEN_LOGGING_INFORMATION` | N/A
| Required access | `TOKEN_QUERY`               | N/A
| Minimal version | Windows 11 24H2             | N/A
