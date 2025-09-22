### ThreadHandle

Handle to thread object.

### SuspendCount

Returns number of suspend request for thread `ThreadHandle` before call `NtAlertResumeThread`. If this number is *0*, \
thread will continue execution.

Difference between `AlertResumeThread` and `ResumeThread` it's the first one sets Thread Object to alerted state (so before thread will continue execution, all APC will be executed).

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `NtCreateThread`
* `NtOpenThread`
* `NtResumeThread`
* `NtSuspendThread`
