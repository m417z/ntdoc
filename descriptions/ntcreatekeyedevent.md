Synchronization object called KeyedEvent is avaiable \
in Windows XP\+ systems. It's usefull when both \(or more\) \
threads have to wait for each other. \
KeyedEventHandle HANDLE to newly \
created KeyedEvent object. \
DesiredAccess The same values as for \
Event objects \(typically \
EVENT\_ALL\_ACCESS\). \
ObjectAttributes Optionally name of \
object. \
Reserved Have to be zero. Reserved for \
future use. \
Supported on system versions: \
Win XP/2003

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtOpenKeyedEvent \
NtReleaseKeyedEvent \
NtWaitForkeyedEvent
