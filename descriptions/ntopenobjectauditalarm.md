Function `NtOpenObjectAuditAlarm` does not work on *NT40-SP6*. For additional information see description of **ObjectOpenAuditAlarm** function in *Microsoft SDK*.

### SubsystemName

???

### ObjectHandle

Can be any valid `HANDLE` to object, or *NULL*.

### ObjectTypeName

???

### ObjectName

???

### SecurityDescriptor

Pointer to `SECURITY_DESCRIPTOR` structure, or *NULL*.

### ClientToken

`HANDLE` to Token Object previously opened with `TOKEN_QUERY` access.

### DesiredAccess

???

### GrantedAccess

???

### Privileges

Optionally pointer to `PRIVILEGE_SET` structure filled by user with valid privileges.

### ObjectCreation

???

### AccessGranted

???

### GenerateOnClose

Optionally pointer to `BOOLEAN` value.

# Documented by

* Tomasz Nowak

# Requirements

Privilege: `SE_AUDIT_PRIVILEGE`

# See also

* `NtAccessCheckAndAuditAlarm`
* `NtCloseObjectAuditAlarm`
* `NtDeleteObjectAuditAlarm`
* `PRIVILEGE_SET`
* `SECURITY_DESCRIPTOR`
