Function NtAccessCheckAndAuditAlarm doesn't work \
properly on NT40\-SP6. For more information about alarms see \
description of similar function AccessCheckAndAuditAlarm in \
Microsoft SDK. \
SubsystemName \- ??? \
ObjectHandle Can be any valid \
HANDLE to object, or NULL. \
ObjectTypeName \- ??? \
ObjectName \- ??? \
SecurityDescriptor Pointer to \
"Absolute" SECURITY\_DESCRIPTOR structure. \
DesiredAccess \- ??? \
GenericMapping Pointer to \
GENERIC\_MAPPING structure valid for object specified above \
as ObjectHandle parameter. \
ObjectCreation \- ??? \
GrantedAccess Pointer to \
ACCESS\_MASK value \(?\). \
AccessStatus Pointer to NTSTATUS \
value \(?\). \
GenerateOnClose Pointer to \
BOOLEAN value \(?\). \
Function can be called only from impersonated thread. \(See \
NtImpersonateThread for more information\).

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib \
Privilege: SE\_AUDIT\_PRIVILEGE

See also: \
NtAccessCheck \
NtCloseObjectAuditAlarm \
NtDeleteObjectAuditAlarm \
NtImpersonateThread \
NtOpenObjectAuditAlarm \
SECURITY\_DESCRIPTOR
