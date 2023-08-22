This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_rename_information).

---

Structure `FILE_RENAME_INFORMATION` is used as input buffer for function `NtSetInformationFile`, called with `FileRenameInformation` information class. Using this structure caller can rename file, or move it into other directory.

### ReplaceIfExists

If set, and file with the same name as destination exist, it will be replaced. If no, `STATUS_OBJECT_NAME_COLLISION` is returned.

### RootDirectory

Optional `HANDLE` to parent directory for destination file.

### FileNameLength

Length of `FileName` array, in bytes.

### FileName[1]

UNICODE string specifing destination file name. If `RootDirectory` is *NULL*, it must contains full system path, or only destination file name for in-place rename operation.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `FILE_INFORMATION_CLASS`
* `NtCreateFile`
* `NtNotifyChangeDirectoryFile`
* `NtOpenFile`
* `NtSetInformationFile`
