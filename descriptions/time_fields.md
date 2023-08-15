This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/ns-wdm-time_fields)

TIME\_FIELDS structure is NTDLL version of \
Win 32 API SYSTEM\_TIME. It contains detailed \
information about date and time. \
Year Year, in range 1601 \- \
65535. \
Month Month, in range 1 \- \
12. \
Day Day, in range 1 \- 31, \
dependly on Month member. \
Hour Hour, in range 0 \- \
23. \
Minute Minute, in range 0 \- \
59. \
Second Second, in range 0 \- \
59. \
Milliseconds Milliseconds, in range \
0 \- 1000. \
Weekday Day of week, in range 0 \- \
6, where 0 means "Sunday", \
1 means "Monday" etc.

Documented by: \
Reactos \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtQuerySystemTime \
NtSetSystemTime \
RtlTimeFieldsToTime \
RtlTimeToTimeFields
