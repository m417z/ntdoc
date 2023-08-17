This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntquerydirectoryfile) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwquerydirectoryfile).

---

`NtQueryDirectoryFile` is used to enumerate entries (files or directories) placed into file container object (directory). *Win32 API* use it in `FindFirstFile`-`FindNextFile` routines.

### FileHandle

`HANDLE` to File Object opened with `FILE_DIRECTORY_FILE` option and `FILE_LIST_DIRECTORY` access.

### Event

Optional `HANDLE` to Event Object signaled after query complete.

### ApcRoutine

Optinal pointer to user's *APC* routine queued after query complete.

### ApcContext

Parameter for `ApcRoutine`.

### IoStatusBlock

Pointer to `IO_STATUS_BLOCK` structure. After enumeration complete, `Information` member of this structure contains number of bytes writed into `FileInformation` buffer. `Status` member contains IO result of call, and can be one of:

* `STATUS_SUCCESS` - Enumeration has results in `FileInformation` buffer.
* `STATUS_NO_MORE_FILES` - `FileInformation` buffer is empty, and next call isn't needed.
* `STATUS_NO_SUCH_FILE` - Returned when `FileMask` parameter specify exactly one file (don't contains `'*'` or `'?'` characters), and queried directory don't contains that file.

### FileInformation

User's allocated buffer for output data.

### Length

Length of `FileInformation` buffer, in bytes.

### FileInformationClass

Information class. Can be one of:

* `FileDirectoryInformation`
* `FileFullDirectoryInformation`
* `FileBothDirectoryInformation`
* `FileNamesInformation`
* `FileOleDirectoryInformation`

### ReturnSingleEntry

If set, only one entry is returned.

### FileMask

If specified, only information about files matches this wildchar mask will be returned.

`WARNING:` There's no rule specifing what to do when caller makes two calls to `NtQueryDirectoryFile` both with different masks. Typically `FileMask` specified in second call will be ignored, and results will match the first (for example: **NTFS.SYS**). The best solution is to close directory `HANDLE` after every call with `FileMask` parameter specified.

### RestartScan

Used with `ReturnSingleEntry` parameter. If set, `NtQueryDirectoryFile` continue enumeration after last enumerated element in previous call. If no, returns the first entry in directory.

---

For detailed information about results, see `FILE_INFORMATION_CLASS` with information classes specified above.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `NtCreateFile`
* `NtOpenFile`
* `NtQueryInformationFile`
* `NtQueryOleDirectoryFile`
* `NtQueryVolumeInformationFile`
