This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationtoken) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryinformationtoken).

---

Function `NtQueryInformationToken` receives informations specified by information class from Token Object. See also *Win32 API* **GetTokenInformation**.

### TokenHandle

`HANDLE` to Token Object opened with `TOKEN_QUERY` access.

### TokenInformationClass

Information class descripted in `TOKEN_INFORMATION_CLASS` topic.

### TokenInformation

User's allocated buffer for output data. Format of output buffer depends on `TokenInformationClass` parameter.

### TokenInformationLength

Length of `TokenInformation` buffer, in bytes.

### ReturnLength

If output buffer is to small, value under this parameter receives required length.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateToken`
* `NtOpenProcessToken`
* `NtOpenThreadToken`
* `NtSetInformationToken`
* `TOKEN_INFORMATION_CLASS`
