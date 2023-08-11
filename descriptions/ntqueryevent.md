EventHandle HANDLE to Event \
Object opened with EVENT\_QUERY\_STATE access. \
EventInformationClass See \
EVENT\_INFORMATION\_CLASS for details. \
EventInformation Caller's allocated \
buffer for result data. \
EventInformationLength Length of \
EventInformation buffer, in \
bytes. \
ReturnLength Returns required/used size \
of EventInformation buffer. \
Currently there're only one information class for use with Event \
Object. See \
EVENT\_INFORMATION\_CLASS for details.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
EVENT\_BASIC\_INFORMATION \
EVENT\_INFORMATION\_CLASS \
NtCreateEvent \
NtOpenEvent
