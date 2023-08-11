Function NtPrivilegeObjectAuditAlarm doesn't work, as \
the most of other auditing functions... \
SubsystemName \- ??? \
ObjectHandle This can be any \
value. \
ClientToken HANDLE to Token \
Object opened with TOKEN\_QUERY access. \
DesiredAccess \- ??? \
ClientPrivileges Pointer to PRIVILEGE\_SET structure filled with valid \
data. \
AccessGranted \- ???

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib \
Privilege: SE\_AUDIT\_PRIVILEGE

See also: \
NtAccessCheckAndAuditAlarm \
NtOpenObjectAuditAlarm \
NtPrivilegedServiceAuditAlarm \
PRIVILEGE\_SET
