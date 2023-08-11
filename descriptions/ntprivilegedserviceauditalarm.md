Function NtPrivilegedServiceAuditAlarm doesn't work \
on NT40\-SP6. For more information see description of \
PrivilegedServiceAuditAlarm in Microsoft SDK. \
SubsystemName \- ??? \
ServiceName \- ??? \
ClientToken HANDLE to Token \
Object opened with TOKEN\_QUERY access. \
ClientPrivileges Pointer to PRIVILEGE\_SET structure contains valid \
data. \
AccessGranted \- ???

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib \
Privilege: SE\_AUDIT\_PRIVILEGE

See also: \
NtOpenObjectAuditAlarm \
NtPrivilegeObjectAuditAlarm \
PRIVILEGE\_SET
