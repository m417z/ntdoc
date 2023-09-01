Function `NtReadFileScatter` reads specified block from file into multiple buffers. Each buffer must have one page length (*0x1000* bytes on **x86**).

### FileHandle

`HANDLE` to File Object opened with `FILE_READ_DATA` access and with `FILE_NO_INTERMEDIATE_BUFFERING` open option.

### Event

`HANDLE` to Event Object signaled when reading is complete. This parameter is optional, but caller should use one of notification way, because function always use asynchronous reading method.

### ApcRoutine

Optional pointer to user's *APC Routine*.

### ApcContext

User's parameter for `ApcRoutine`.

### IoStatusBlock

IO result of call.

### SegmentArray

Array of `FILE_SEGMENT_ELEMENT` unions. Any element point to allocated memory page address. Last element of array must be *NULL*.

### Length

Number of bytes to read.

### ByteOffset

Pointer to `LARGE_INTEGER` value indicates reading start position.

### Key

Optional pointer to user's key, used when file is locked (see `NtLockFile`).

---

See also `ReadFileScatter` description in *Microsoft SDK*.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateFile`
* `NtLockFile`
* `NtOpenFile`
* `NtReadFile`
* `NtUnlockFile`
* `NtWriteFileGather`
