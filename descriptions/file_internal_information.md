This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_internal_information).

---

`FILE_INTERNAL_INFORMATION` structure is a result of call `NtQueryInformationFile` with `FileInternalInformation` information class. It's not possible to set file unique identifier.

### IndexNumber

File identifier, unique for file's device.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `FILE_ALL_INFORMATION`
* `FILE_INFORMATION_CLASS`
* `NtCreateFile`
* `NtOpenFile`
* `NtQueryInformationFile`
