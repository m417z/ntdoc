This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwsetevent).

---

### EventHandle

`HANDLE` to Event Object opened with `EVENT_MODIFY_STATE` access.

### PreviousState

State of Event Object before function call.

# Documented by

* Tomasz Nowak

# See also

* `NtClearEvent`
* `NtCreateEvent`
* `NtOpenEvent`
* `NtResetEvent`
