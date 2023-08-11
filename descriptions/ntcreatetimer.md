TimerHandle Result of call \- \
HANDLE to Timer Object. \
DesiredAccess Access mask for \
TimerHandle. Can be set of \(from \
&lt;WinNT.h&gt;\): \
TIMER\_QUERY\_STATE \
TIMER\_MODIFY\_STATE \
TIMER\_ALL\_ACCESS \
ObjectAttributes Optional name of Timer \
Object. \
TimerType Can be \
NotificationTimer or \
SynchronizationTimer \(enumerated type definition from \
&lt;ntdef.h&gt;\). See also \
EVENT\_TYPE.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
EVENT\_TYPE \
NtOpenTimer
