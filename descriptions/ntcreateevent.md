This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwcreateevent)

EventHandle Result of call \- \
HANDLE to newly created Event Object. \
DesiredAccess Assess rights associated \
with created event. Can be one of following values from \
&lt;winnt.h&gt;: \
EVENT\_QUERY\_STATE \
EVENT\_MODIFY\_STATE \
EVENT\_ALL\_ACCESS \
ObjectAttributes Optional name of Event \
Object for multiprocess use. \
EventType See \
EVENT\_TYPE for details. \
InitialState State of event \
immediatelly after creation.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
EVENT\_TYPE \
NtOpenEvent
