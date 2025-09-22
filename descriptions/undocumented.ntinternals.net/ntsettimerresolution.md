Function `NtSetTimerResolution` sets resolution of system *Timer* in calling process context.

### DesiredResolution

Resolution to set. To receive minimum and maximum resolution values, call `NtQueryTimerResolution`.

### SetResolution

If set, system *Timer's* resolution is set to `DesiredResolution` value. If no, parameter `DesiredResolution` is ignored.

### CurrentResolution

Pointer to `ULONG` value receiving current timer's resolution, in *100-ns* units.

# Documented by

* Tomasz Nowak

# See also

* `NtGetTickCount`
* `NtQueryTimerResolution`
* `NtSetTimer`
