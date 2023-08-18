This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntduplicatetoken) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwduplicatetoken).

---

Function `NtDuplicateToken` creates new Token Object basing on existing Token Object.

### ExistingToken

`HANDLE` to Token Object opened with `TOKEN_DUPLICATE` access.

### DesiredAccess

Access mask for newly created token. Can be combination of:

* `TOKEN_ASSIGN_PRIMARY`
* `TOKEN_DUPLICATE`
* `TOKEN_IMPERSONATE`
* `TOKEN_QUERY`
* `TOKEN_QUERY_SOURCE`
* `TOKEN_ADJUST_PRIVILEGES`
* `TOKEN_ADJUST_GROUPS`
* `TOKEN_ADJUST_DEFAULT`
* `TOKEN_ADJUST_SESSIONID`

### ObjectAttributes

Optionally pointer to `OBJECT_ATTRIBUTES` structure, containing token's name.

### ImpersonationLevel

Level of impersonation for new token.

### TokenType

Type of new token.

### NewToken

Result of call - pointer to `HANDLE` to new Token Object.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `NtCreateToken`
* `NtOpenProcessToken`
* `NtOpenThreadToken`
* `NtQueryInformationToken`
* `NtSetInformationToken`
