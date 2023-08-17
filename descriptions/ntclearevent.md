### EventHandle

`HANDLE` to Event Object opened with `EVENT_MODIFY_STATE` attribute.

---

There're no functional difference between `NtClearEvent` and `NtResetEvent`, but the first works faster (see `NtResetEvent`).

# Documented by

* Tomasz Nowak

# See also

* `NtCreateEvent`
* `NtOpenEvent`
* `NtResetEvent`
* `NtSetEvent`
