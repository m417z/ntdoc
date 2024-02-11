This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntreadfile) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwreadfile).

---

*(Also described in Win2000 DDK)*

### FileHandle

`HANDLE` to File Object opened with `FILE_READ_DATA` access.

### Event

Optional `HANDLE` to Event Object signaled when reading is done.

### ApcRoutine

User defined *APC* routine queued for execute after reading is done.

### ApcContext

User parameter to `ApcRoutine`.

### IoStatusBlock

Pointer to IO_STATUS structure received IO status of file reading.

### Buffer

User-allocated buffer for read data.

### Length

Length of `Buffer`, in bytes.

### ByteOffset

Offset from beginning of file, in bytes.

### Key

??? (In my opinion: use this, if you previously lock file, and now you want read it, but without unlocking).

# Related Win32 API
 - [`ReadFile`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-readfile) (Although it does more than just forwarding the arguments and invoking this procedure.) 

# Documented by

* Tomasz Nowak

# See also

* `NtCreateFile`
* `NtOpenFile`
* `NtWriteFile`
