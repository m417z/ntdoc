Function NtGetTickCount returns system Timer's \
ticks counter. This counter is also avaiable in KUSER\_SHARED\_DATA structure as \
TickCountLow member. \
Calling NtSetTimerResolution \
doesn't effect in counter's update resolution.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
KUSER\_SHARED\_DATA \
NtSetTimerResolution
