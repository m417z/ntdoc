Function `NtPrivilegeObjectAuditAlarm` doesn't work, as the most of other auditing functions...

### SubsystemName

???

### ObjectHandle

This can be any value.

### ClientToken

`HANDLE` to Token Object opened with `TOKEN_QUERY` access.

### DesiredAccess

???

### ClientPrivileges

Pointer to `PRIVILEGE_SET` structure filled with valid data.

### AccessGranted

???

# Documented by

* Tomasz Nowak

# Requirements

Privilege: `SE_AUDIT_PRIVILEGE`

# See also

* `NtAccessCheckAndAuditAlarm`
* `NtOpenObjectAuditAlarm`
* `NtPrivilegedServiceAuditAlarm`
* `PRIVILEGE_SET`
