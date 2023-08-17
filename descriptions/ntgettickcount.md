Function `NtGetTickCount` returns system *Timer's* ticks counter. This counter is also avaiable in `KUSER_SHARED_DATA` structure as **TickCountLow** member.

Calling `NtSetTimerResolution` doesn't effect in counter's update resolution.

# Documented by

* Tomasz Nowak

# See also

* `KUSER_SHARED_DATA`
* `NtSetTimerResolution`
