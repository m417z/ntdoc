EventHandle HANDLE to Event \
Object opened with EVENT\_MODIFY\_STATE access. \
PreviousState Optional pointer to state \
of event before function call. Difference between \
NtResetEvent and NtClearEvent is the \
first one can return state of event before call.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtClearEvent \
NtCreateEvent \
NtOpenEvent \
NtQueryEvent \
NtSetEvent
