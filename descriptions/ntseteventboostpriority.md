Function `NtSetEventPriorityBoost` was added in *Windows XP* system. Has the same functionality as `NtSetEvent`, but thread that is waiting on specified *Event* will be executed immediatelly after context switch, regardless of waiting thread's priority.

### EventHandle

`HANDLE` to previously created or opened *Event* object. Note that Event has to be created with `EVENT_TYPE` set to **SynchronizationEvent** (automatic reset), in other cases function will return with error.

# Documented by

* Tomasz Nowak

# See also

* `EVENT_TYPE`
* `NtCreateEvent`
* `NtOpenEvent`
* `NtSetEvent`
