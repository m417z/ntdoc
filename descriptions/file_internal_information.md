`FILE_INTERNAL_INFORMATION` structure is a result of call `NtQueryInformationFile` with `FileInternalInformation` information class. It's not possible to set file unique identifier.

### IndexNumber

File indentifier, unique for file's device.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `FILE_ALL_INFORMATION`
* `FILE_INFORMATION_CLASS`
* `NtCreateFile`
* `NtOpenFile`
* `NtQueryInformationFile`
