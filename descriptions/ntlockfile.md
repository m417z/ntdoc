This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntlockfile) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwlockfile).

---

### FileHandle

`HANDLE` to File Object opened with `FILE_READ_DATA` access.

### LockGrantedEvent

Optional `HANDLE` to Event Object, whitch is signaled when lock is created (typically used with `ReturnImmediately` parameter set to `TRUE`).

### ApcRoutine

APC routine executed when lock is granted.

### ApcContext

Optional parameter for `ApcRoutine`.

### IoStatusBlock

IO result of call.

### ByteOffset

Offset (in bytes) to begin of file region to lock.

### Length

Length of region to lock, in bytes.

### Key

Pointer to user's defined 4-bytes key associated with this lock. It can be used in multi-thread process to allow reading or writing data only for one specified thread, whitch known `Key` value.

### ReturnImmediately

If `TRUE`, function returns immediately. Caller is informed about lock creation by `LockGrantedEvent` or by executing `ApcRoutine`.

### ExclusiveLock

If set, all read and write operation are denied for other processes. If not, only write operation is denied.

# Documented by

* ReactOS
* Tomasz Nowak

# See also

* `NtCreateFile`
* `NtOpenFile`
* `NtReadFile`
* `NtReadFileScatter`
* `NtUnlockFile`
* `NtWriteFile`
* `NtWriteFileGather`
