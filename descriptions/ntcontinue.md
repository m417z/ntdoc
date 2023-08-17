### ThreadContext

Pointer to `CONTEXT` structure for current thread.

### RaiseAlert

If set, remove *Alerted* state from current Thread Object.

---

You can use `NtContinue` after processing exception for continue executing thread. \
System uses `NtContinue` also in `APC` processing.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `NtCreateThread`
* `NtGetContextThread`
* `NtSetContextThread`
