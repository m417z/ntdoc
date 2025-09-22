This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntopenprocesstoken).

---

### ProcessHandle

`HANDLE` to Process Object.

### DesiredAccess

Access mask for opened Token Object.

### TokenHandle

Result of call - `HANDLE` to Token Object associated with process specified by `ProcessHandle` parameter.

---

See also `PROCESS_INFORMATION_CLASS` with `ProcessAccessToken` information class.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateToken`
* `NtOpenThreadToken`
* `NtQueryInformationProcess`
* `NtSetInformationProcess`
* `PROCESS_INFORMATION_CLASS`
