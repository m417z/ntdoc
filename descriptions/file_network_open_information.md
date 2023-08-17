This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_network_open_information).

---

`FILE_NETWORK_OPEN_INFORMATION` structure is used with two file functions:

1) `NtQueryFullAttributesFile`,

2) `NtQueryInformationFile` with `FileNetworkOpenInformation` information class.

### CreationTime

Indicates time of file creation.

### LastAccessTime

Time of last open file.

### LastWriteTime

Time of last write operation.

### ChangeTime

Time of any last change.

### AllocationSize

Number of bytes that file use on storage, equal or greater to `EndOfFile`.

### EndOfFile

Length of file, in bytes.

### FileAttributes

File attributes.

### Unknown

???

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `FILE_BASIC_INFORMATION`
* `FILE_INFORMATION_CLASS`
* `FILE_STANDARD_INFORMATION`
* `NtCreateFile`
* `NtOpenFile`
* `NtQueryAttributesFile`
* `NtQueryFullAttributesFile`
* `NtQueryInformationFile`
* `NtWriteFile`
