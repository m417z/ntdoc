This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationtoken) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwsetinformationtoken).

---

Function `NtSetInformationToken` sets parameters of Token Objects. See also description of **SetTokenInformation** \
in *Win32 API SDK*.

### TokenHandle

`HANDLE` to Token Object opened with `TOKEN_ADJUST_DEFAULT` access.

### TokenInformationClass

Information class described in `TOKEN_INFORMATION_CLASS` topic.

### TokenInformation

User's allocated buffer containing data to set to.

### TokenInformationLength

Length of `TokenInformation` buffer, in bytes.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateToken`
* `NtOpenProcessToken`
* `NtOpenThreadToken`
* `NtQueryInformationToken`
* `TOKEN_INFORMATION_CLASS`
