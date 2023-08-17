Function `NtWriteFileGather` writes specified block of file with data from memory pages. See `NtReadFileScatter` for more information.

### FileHandle

`HANDLE` to File Object opened with `FILE_WRITE_DATA` access and `FILE_NO_INTERMEDIATE_BUFFERING` open option.

**Warring:** You cannot use File Object opened with `FILE_APPEND_DATA` access.

### Event

`HANDLE` to Event Object signaled when writing will finish. Function always use asynchronous writing operation, so caller should define `Event` or `ApcRoutine` parameter.

### ApcRoutine

Pointer to user's *APC Routine*.

### ApcContext

Parameter for `ApcRoutine`.

### IoStatusBlock

IO result of call.

### SegmentArray

Array of `FILE_SEGMENT_ELEMENT` elements pointing to memory pages to write. Last array element must be *NULL*.

### Length

Number of bytes to write.

### ByteOffset

Pointer to `LARGE_INTEGER` value indicates starting position for write.

### Key

Pointer to user's defined key, used when file is locked (see `NtLockFile`).

# Documented by

* Tomasz Nowak

# See also

* `NtCreateFile`
* `NtLockFile`
* `NtOpenFile`
* `NtReadFileScatter`
* `NtWriteFile`
