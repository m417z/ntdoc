This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntopenthreadtoken).

---

### ThreadHandle

`HANDLE` to thread object.

### DesiredAccess

Access mask for opened Token Object.

### OpenAsSelf

???

### TokenHandle

Result of call - `HANDLE` to Token Object associated with `ThreadHandle` thread.

---

Usually Win32 threads don't have associated Tokens. If you want to associate Token for Thread Object, use \
`NtSetInformationThread` with `ThreadImpersonationToken` information class.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `NtCreateToken`
* `NtOpenProcessToken`
* `NtOpenThread`
* `NtSetInformationThread`
* `THREAD_INFORMATION_CLASS`
