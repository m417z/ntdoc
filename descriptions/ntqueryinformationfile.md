This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwqueryinformationfile).

---

*(Also avaiable in Microsoft 2000 DDK)*

### FileHandle

`HANDLE` to File Object.

### IoStatusBlock

Completion status of call.

### FileInformation

Caller's allocated buffer for result data.

### Length

Length of `FileInformation` buffer, in bytes.

### FileInformationClass

Enumerated information class. See `FILE_INFORMATION_CLASS` for detailed information about usage.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `FILE_INFORMATION_CLASS`
* `NtCreateFile`
* `NtOpenFile`
* `NtQueryAttributesFile`
* `NtQueryDirectoryFile`
* `NtSetInformationFile`
