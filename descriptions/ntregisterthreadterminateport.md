### PortHandle

`HANDLE` to previously connected Port Object.

---

Typically, `NtRegisterThreadTerminatePort` is used in `CsrNewThread` function, called before thread execution begins, but in thread context.

Function associate `PortHandle` with thread, and sends `LPC_TERMINATION_MESSAGE` to specified port immediately after call `NtTerminateThread`.

# Documented by

* Tomasz Nowak

# See also

* `CsrNewThread`
* `LPC_TERMINATION_MESSAGE`
* `NtConnectPort`
* `NtTerminateThread`
