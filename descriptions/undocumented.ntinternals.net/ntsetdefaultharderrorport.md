`NtSetDefaultHardErrorPort` is typically called only once. After call, kernel set `BOOLEAN` flag named `_ExReadyForErrors` to `TRUE`, and all other tries to change default port are broken with `STATUS_UNSUCCESSFUL` error code.

### PortHandle

`HANDLE` to named Port Object.

---

Listener of default HardError port receive `HARDERROR_MSG` *LPC* messages when any process call `NtRaiseHardError` function.

# Documented by

* Tomasz Nowak

# Requirements

Privilege: `SE_TCB_PRIVILEGE`

# See also

* `HARDERROR_MSG`
* `NtRaiseHardError`
