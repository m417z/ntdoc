Function NtCloseObjectAuditAlarm sends alarm to Event \
Log, section Security. Alarm informs about close user's created \
object. \
SubsystemName This string is sent to \
Event Log as the first parameter. \
ObjectHandle HANDLE to object, \
or NULL value. \
GenerateOnClose If set, event is \
generated.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib \
Privilege: SE\_AUDIT\_PRIVILEGE

See also: \
NtAccessCheckAndAuditAlarm \
NtDeleteObjectAuditAlarm \
NtOpenObjectAuditAlarm
