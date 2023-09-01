This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_directory_information).

---

Structure `FILE_DIRECTORY_INFORMATION` is returned as a result of call `NtQueryDirectoryFile` with `FileDirectoryInformation` information class. It contains some typical information about directory entries.

### NextEntryOffset

Offset (in bytes) of next `FILE_DIRECTORY_INFORMATION` structure placed in result buffer. If there's no more entries, `NextEntryOffset` is set to zero.

### FileIndex

File index value, or zero, if directory indexing is not available.

### CreationTime

Time of object creation;

### LastAccessTime

Last access time. Means time when last open operation was performed.

### LastWriteTime

Time of last write data.

### ChangeTime

Time of last change.

### EndOfFile

Specify length of file, in bytes.

### AllocationSize

Specify real size of file on device. It must be equal or greater to `EndOfFile` member.

### FileAttributes

Attributes of file.

### FileNameLength

Length of `FileName` array, in bytes.

### FileName[1]

UNICODE string specifying file name.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `FILE_BOTH_DIR_INFORMATION`
* `FILE_FULL_DIR_INFORMATION`
* `FILE_INFORMATION_CLASS`
* `FILE_NAMES_INFORMATION`
* `NtQueryDirectoryFile`
