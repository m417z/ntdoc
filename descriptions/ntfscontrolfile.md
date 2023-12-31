This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntfscontrolfile) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwfscontrolfile).

---

Function `NtFsControlFile` sends `FSCTL_*` code to File System Device Driver. See also description of `NtDeviceIoControlFile` function.

### FileHandle

`HANDLE` to File System Device Object opened as a file.

### Event

Optional `HANDLE` to Event Object.

### ApcRoutine

Optional pointer to user's *APC Routine*.

### ApcContext

Parameter for `ApcRoutine`.

### IoStatusBlock

IO result of call.

### FsControlCode

Control Code typically defined as `FSCTL_*`.

### InputBuffer

User's allocated buffer contains input data.

### InputBufferLength

Length of `InputBuffer`, in bytes.

### OutputBuffer

User's allocated buffer for results of call.

### OutputBufferLength

Length of `OutputBuffer`, in bytes.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `NtCreateFile`
* `NtDeviceIoControlFile`
* `NtOpenFile`
