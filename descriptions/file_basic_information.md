This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_basic_information).

---

Structure `FILE_BASIC_INFORMATION` is used in a call to function `NtSetInformationFile` with `FileBasicInformation` information class, and is received in a call to `NtQueryInformationFile` with the same information class. Also function `NtQueryAttributesFile` uses as a result `FILE_BASIC_INFORMATION`, but it fills only `FileAttributes` field. See required function's description for details.

### CreationTime

Time of file creation, in *100-ns* units.

### LastAccessTime

Time of last open operation, in *100-ns* units.

### LastWriteTime

Time of last write operation, in *100-ns* units.

### ChangeTime

Time of any last change, in *100-ns* units.

### FileAttributes

File attributes. See `NtCreateFile` for possibilities.

---

Structure is also available in *Microsoft DDK*.

# Documented by

* Tomasz Nowak

# See also

* `FILE_INFORMATION_CLASS`
* `NtCreateFile`
* `NtQueryAttributesFile`
* `NtQueryInformationFile`
* `NtSetInformationFile`
