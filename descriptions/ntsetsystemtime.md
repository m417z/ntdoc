Function NtSetSystemTime sets system time. See \
NtQuerySystemTime \
for detailed information. \
SystemTime Pointer to \
LARGE\_INTEGER contains UTC time to set. \
PreviousTime Optionally receives time \
before change.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib \
Privilege: SE\_SYSTEMTIME\_PRIVILEGE

See also: \
NtQuerySystemTime \
RtlTimeFieldsToTime \
RtlTimeToTimeFields
