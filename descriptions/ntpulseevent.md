### EventHandle

`HANDLE` to Event Object opened with `EVENT_MODIFY_STATE` access.

### PreviousState

State of event before call.

---

Function sets event to signaled state, releases all (or one - depending on `EVENT_TYPE`) waiting threads, and resets event to non-signaled state. If they're no waiting threads, `NtPulseEvent` just clear event state.

# Documented by

* Tomasz Nowak

# See also

* `EVENT_TYPE`
* `NtClearEvent`
* `NtCreateEvent`
* `NtOpenEvent`
* `NtResetEvent`
* `NtSetEvent`
