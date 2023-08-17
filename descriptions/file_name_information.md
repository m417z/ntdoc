This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_name_information).

---

Structure `FILE_NAME_INFORMATION` contains name of queried file object. It's used as a result of call `NtQueryInformationFile` with `FileNameInformation` or `FileAlternateNameInformation` information class.

### FileNameLength

Length of `FileName`, in bytes.

### FileName[1]

UNICODE name of file. If caller query about `FileNameInformation`, `FileName` additionally contains path to file, and begins with **'/'** (full path to file relative to device).

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `FILE_ALL_INFORMATION`
* `FILE_INFORMATION_CLASS`
* `NtQueryInformationFile`
