### EventHandle

`HANDLE` to Event Object opened with `EVENT_MODIFY_STATE` access.

### PreviousState

Optional pointer to state of event before function call.

Difference between `NtResetEvent` and `NtClearEvent` is the first one can return state of event before call.

# Documented by

* Tomasz Nowak

# See also

* `NtClearEvent`
* `NtCreateEvent`
* `NtOpenEvent`
* `NtQueryEvent`
* `NtSetEvent`
