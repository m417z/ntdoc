This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenevent).

---

### EventHandle

Result of call - `HANDLE` to Event Object.

### DesiredAccess

See `NtCreateEvent` for possible access rights.

### ObjectAttributes

Must contain valid Event Object name, in NT Objects Namespace.

---

Only named events can be opened by this function call.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateEvent`
