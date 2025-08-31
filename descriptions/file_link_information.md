This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_link_information).

---

Structure `FILE_LINK_INFORMATION` is used as input buffer for function `NtSetInformationFile` called with `FileLinkInformation` information class for make hard link to file.

On standard NT system only links to files are accepted. Caller cannot create link to directory (for *Poxis* compatibility reason).

### ReplaceIfExists

If set, and destination object already exists, it will be replaced with newly created link.

### RootDirectory

`HANDLE` to File Object specifying directory where link should be placed. Can be *NULL* if `FileName` parameter contains full path.

### FileNameLength

Length of `FileName` array, in bytes.

### FileName[1]

UNICODE string specifying name of link and optionally with path (see description of `RootDirectory`).

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `FILE_INFORMATION_CLASS`
* `FILE_RENAME_INFORMATION`
* `NtSetInformationFile`
