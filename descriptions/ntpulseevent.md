EventHandle HANDLE to Event \
Object opened with EVENT\_MODIFY\_STATE access. \
PreviousState State of event before \
call. \
Function sets event to signaled state, releases all \(or one \- \
dependly of \
EVENT\_TYPE\) waiting threads, and resets event to non\-signaled \
state. If they're no waiting threads, NtPulseEvent \
just clear event state.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
EVENT\_TYPE \
NtClearEvent \
NtCreateEvent \
NtOpenEvent \
NtResetEvent \
NtSetEvent
