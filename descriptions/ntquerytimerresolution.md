Function NtQueryTimerResolution returns resolution of \
system Timer in context of calling process. See also \
description of NtSetTimerResolution. \
MinimumResolution Means highest \
possible delay \(in 100\-ns units\) between timer events. \
MaximumResolution Means lowest possible \
delay \(in 100\-ns units\) between timer events. \
CurrentResolution Current timer \
resolution, in 100\-ns units.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtGetTickCount \
NtSetTimer \
NtSetTimerResolution
