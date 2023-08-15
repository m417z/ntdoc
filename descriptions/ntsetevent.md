This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwsetevent)

EventHandle HANDLE to Event \
Object opened with EVENT\_MODIFY\_STATE access. \
PreviousState State of Event Object \
before function call.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtClearEvent \
NtCreateEvent \
NtOpenEvent \
NtResetEvent
