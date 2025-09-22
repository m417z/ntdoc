This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwseteafile).

---

See `NtQueryEaFile` for information about *EA*.

### FileHandle

`HANDLE` to File Object opened with `FILE_SET_EA` access.

### IoStatusBlock

IO result of call.

### EaBuffer

User's allocated input buffer containing one or more `FILE_FULL_EA_INFORMATION` structures.

### EaBufferSize

Size of `EaBuffer`, in bytes.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `FILE_FULL_EA_INFORMATION`
* `NtCreateFile`
* `NtQueryEaFile`
