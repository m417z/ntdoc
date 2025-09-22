This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntunlockfile) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwunlockfile).

---

### FileHandle

`HANDLE` to File Object with locked region.

### IoStatusBlock

IO result of function call.

### ByteOffset

Offset in file where unlock region begins.

### Length

Length of region to unlock.

### Key

Pointer to 4-bytes key associated with lock. See `NtLockFile` for additional information about locking by key usage.

# Documented by

* ReactOS
* Tomasz Nowak

# See also

* `NtCreateFile`
* `NtLockFile`
* `NtOpenFile`
* `NtReadFile`
* `NtReadFileScatter`
* `NtWriteFile`
* `NtWriteFileGather`
