Function NtQueryIntervalProfile retrieves currently \
set delay between performance counter's ticks. See also description \
of \
NtSetIntervalProfile function. \
ProfileSource Performance counter \
identifier defined in \
KPROFILE\_SOURCE enumeration type. \
Interval Pointer to ULONG value \
receiving current interval, in ms. If received value is \
zero, counter specified in ProfileSource parameter is hardware counter \
\(performacne counter build in CPU\).

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
KPROFILE\_SOURCE \
NtCreateProfile \
NtSetIntervalProfile
