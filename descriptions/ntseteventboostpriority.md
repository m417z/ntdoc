Function NtSetEventPriorityBoost was added in \
Windows XP system. Has the same functionality as \
NtSetEvent, but thread that is waiting on specified \
Event will be executed immediatelly after context switch, \
regardless of waiting thread's priority. \
EventHandle HANDLE to previously \
created or opened Event object. Note that Event has to be \
created with \
EVENT\_TYPE set to SynchronizationEvent \(automatic \
reset\), in other cases function will return with error. \
Supported on system versions: \
Win XP/2003

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
EVENT\_TYPE \
NtCreateEvent \
NtOpenEvent \
NtSetEvent
