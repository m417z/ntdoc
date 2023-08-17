Function `NtCreateToken` creates Token Object.

### TokenHandle

Result of call - pointer to `HANDLE` to Token Object.

### DesiredAccess

Can be one or more of following:

* `TOKEN_ASSIGN_PRIMARY`

* `TOKEN_DUPLICATE`
* `TOKEN_IMPERSONATE`

* `TOKEN_QUERY`
* `TOKEN_QUERY_SOURCE`

* `TOKEN_ADJUST_PRIVILEGES`
* `TOKEN_ADJUST_GROUPS`

* `TOKEN_ADJUST_DEFAULT`
* `TOKEN_ADJUST_SESSIONID`

* `TOKEN_ALL_ACCESS`

### ObjectAttributes

Pointer to `OBJECT_ATTRIBUTES` structure.

### TokenType

**(?)**, see `TOKEN_TYPE` enumeration type.

### AuthenticationId

**(?)**, see `NtAllocateLocallyUniqueId` security function.

### ExpirationTime

**(?)**, pointer to `LARGE_INTEGER` value contains time in *100-ns* format.

### TokenUser

**(?)**, see `TOKEN_USER` structure.

### TokenGroups

**(?)**, see `TOKEN_GROUPS` structure.

### TokenPrivileges

**(?)**, see `TOKEN_PRIVILEGES` structure.

### TokenOwner

**(?)**, see `TOKEN_OWNER` structure.

### TokenPrimaryGroup

**(?)**, see `TOKEN_PRIMARY_GROUP` structure.

### TokenDefaultDacl

**(?)**, see `TOKEN_DEFAULT_DACL` structure.

### TokenSource

**(?)**, see `TOKEN_SOURCE` structure.

# Documented by

* ReactOS

# Requirements

Privilege: `SE_CREATE_TOKEN_PRIVILEGE`

# See also

* `NtAllocateLocallyUniqueId`
* `NtDuplicateToken`
* `NtOpenProcessToken`
* `NtOpenThreadToken`
* `NtQueryInformationToken`
* `NtSetInformationToken`
