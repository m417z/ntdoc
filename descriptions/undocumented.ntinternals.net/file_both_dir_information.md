This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_both_dir_information).

---

Structure `FILE_BOTH_DIR_INFORMATION` is returned as a result of call `NtQueryDirectoryFile` with `FileBothDirectoryInformation` \
information class. It's extended version of `FILE_FULL_DIR_INFORMATION` structure, \
additionally containing short file name. It's used in *Win32 API* calls `FindFirstFile` and `FindNextFile`.

### NextEntryOffset

Offset (in bytes) of next `FILE_BOTH_DIR_INFORMATION` structure placed in result buffer. If there's no more entries, `NextEntryOffset` is set to zero.

### FileIndex

File index value, or zero, if directory indexing is not available.

### CreationTime

Time of object creation.

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

### EaSize

Size of Extended Attributes associated with file. See also `FILE_EA_INFORMATION` structure.

### ShortNameLength

Length `ShortName` array, in bytes.

### ShortName[12]

Alternate file name, in UNICODE format. Empty string means:

1. Primary name is compatible with `8DOT3` **(MS DOS)** standard, and there's no reason to set the same name twice;
2. File system don't improve short names;

### FileName[1]

UNICODE string specifying file name.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `FILE_DIRECTORY_INFORMATION`
* `FILE_FULL_DIR_INFORMATION`
* `FILE_INFORMATION_CLASS`
* `FILE_NAME_INFORMATION`
* `FILE_NAMES_INFORMATION`
* `NtQueryDirectoryFile`
* `NtQueryOleDirectoryFile`
