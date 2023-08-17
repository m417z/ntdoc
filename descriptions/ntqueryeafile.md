This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryeafile).

---

`NtQueryEaFile` is used to read *EA* from *NTFS* file. For more information about *EA* see `FILE_FULL_EA_INFORMATION`.

### FileHandle

`HANDLE` to File Object opened with `FILE_READ_EA` access.

### IoStatusBlock

IO result of call.

### Buffer

Caller's allocated buffer for output data. See `FILE_FULL_EA_INFORMATION` for detailed description of fields avaiable in buffer.

### Length

Length of buffer, in bytes.

### ReturnSingleEntry

If set, only one entry is returned.

### EaList

Optional list of `FILE_GET_EA_INFORMATION` structures containing names of *EA*.

### EaListLength

Length of `EaList`, in bytes.

### EaIndex

Pointer to `ULONG` value contains 1-based index of queried attribute.

### RestartScan

If set, result is the first quered *EA*.

# Documented by

* Tomasz Nowak

# See also

* `FILE_FULL_EA_INFORMATION`
* `FILE_GET_EA_INFORMATION`
* `NtCreateFile`
* `NtSetEaFile`
