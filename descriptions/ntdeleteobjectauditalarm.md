Function NtDeleteObjectAuditAlarm generates \
Security Audit Alarm, stored in Event Log. See also \
description of \
NtCloseObjectAuditAlarm. \
SubsystemName This string is passed as \
a parameter to event message. \
ObjectHandle HANDLE to any \
object. \
GenerateOnClose If set, event is \
generated.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib \
Privilege: SE\_AUDIT\_PRIVILEGE

See also: \
NtCloseObjectAuditAlarm \
NtOpenObjectAuditAlarm
