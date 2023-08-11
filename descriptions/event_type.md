There are two Event types in WinNT: \
NotificationEvent Known also as \
manual\-reset event. Caller decide about state of event. You can use \
NtClearEvent or NtResetEvent to put Event Object into \
non\-signaled state. \
SynchronizationEvent Known as \
auto\-reset event. This type automatically change his state to \
non\-signaled after releasing any \(but only one\) waiting thread. \
To check what type of event do you have, use NtQueryEvent.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtClearEvent \
NtCreateEvent \
NtQueryEvent \
NtResetEvent
