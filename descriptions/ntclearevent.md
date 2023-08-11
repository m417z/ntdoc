EventHandle HANDLE to Event \
Object opened with EVENT\_MODIFY\_STATE attribute. \
There're no functional difference between \
NtClearEvent and NtResetEvent, but the first works faster \
\(see \
NtResetEvent\).

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateEvent \
NtOpenEvent \
NtResetEvent \
NtSetEvent
