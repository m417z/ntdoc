Function NtOpenObjectAuditAlarm does not work on \
NT40\-SP6. For additional information see description of \
ObjectOpenAuditAlarm function in Microsoft SDK. \
SubsystemName \- ??? \
ObjectHandle Can be any valid \
HANDLE to object, or NULL. \
ObjectTypeName \- ??? \
ObjectName \- ??? \
SecurityDescriptor Pointer to SECURITY\_DESCRIPTOR structure, or \
NULL. \
ClientToken HANDLE to Token \
Object previously opened with TOKEN\_QUERY access. \
DesiredAccess \- ??? \
GrantedAccess \- ??? \
Privileges Optionally pointer to \
PRIVILEGE\_SET structure filled by \
user with valid privileges. \
ObjectCreation \- ??? \
AccessGranted = ??? \
GenerateOnClose Optionally pointer to \
BOOLEAN value.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib \
Privilege: SE\_AUDIT\_PRIVILEGE

See also: \
NtAccessCheckAndAuditAlarm \
NtCloseObjectAuditAlarm \
NtDeleteObjectAuditAlarm \
PRIVILEGE\_SET \
SECURITY\_DESCRIPTOR
