OBJECT\_INFORMATION\_CLASS specifies a kind of \
information of any object available in caller context. It's used \
with functions NtQueryObject and \
NtSetInformationObject. \
ObjectBasicInformation \
Action \
: Query \
Buffer size \
: 0x038 \
Structure \
: OBJECT\_BASIC\_INFORMATION \
ObjectNameInformation \
Action \
: Query \
Buffer size \
: 0x08 \
Structure \
: OBJECT\_NAME\_INFORMATION \
ObjectTypeInformation \
Action \
: Query \
Buffer size \
: 0x070 \
Structure \
: OBJECT\_TYPE\_INFORMATION \
ObjectAllInformation \
Action \
: Query \
Buffer size \
: 0x04\+ \
Structure \
: OBJECT\_ALL\_INFORMATION \
Comment \
: Size of buffer depends on number of objects opened by \
caller. \
ObjectDataInformation \
Action \
: Query, Set \
Buffer size \
: 0x02 \
Structure \
: OBJECT\_DATA\_INFORMATION

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtQueryObject \
NtSetInformationObject
