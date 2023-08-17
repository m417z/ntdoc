Function `NtPrivilegedServiceAuditAlarm` doesn't work on *NT40-SP6*. For more information see description of **PrivilegedServiceAuditAlarm** in *Microsoft SDK*.

### SubsystemName

???

### ServiceName

???

### ClientToken

`HANDLE` to Token Object opened with `TOKEN_QUERY` access.

### ClientPrivileges

Pointer to `PRIVILEGE_SET` structure contains valid data.

### AccessGranted

???

# Documented by

* Tomasz Nowak

# Requirements

Privilege: `SE_AUDIT_PRIVILEGE`

# See also

* `NtOpenObjectAuditAlarm`
* `NtPrivilegeObjectAuditAlarm`
* `PRIVILEGE_SET`
