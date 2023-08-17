Structure `FILE_NAMES_INFORMATION` is used as a result of call `NtQueryDirectoryFile` with `FileNamesInformation` information class. It's shorter then other directory informational structures, so can be used for better performance, when only file names are required.

### NextEntryOffset

Offset (in bytes) of next `FILE_NAMES_INFORMATION` entry, or zero if last.

### FileIndex

Index of file, or zero if Directory Indexing is disabled.

### FileNameLength

Length of FileName array, in bytes.

### FileName[1]

Name of file, in UNICODE format.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `FILE_BOTH_DIR_INFORMATION`
* `FILE_DIRECTORY_INFORMATION`
* `FILE_FULL_DIR_INFORMATION`
* `FILE_INFORMATION_CLASS`
* `NtQueryDirectoryFile`
