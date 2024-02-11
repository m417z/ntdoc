This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntwritefile) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwwritefile).

---

*(Also described in Win 2000 DDK)*

### FileHandle

`HANDLE` to File Object opened with `FILE_WRITE_DATA` access.

### Event

`HANDLE` to Event Object signaled when write finished.

### ApcRoutine

User APC routine executed after writing is complete.

### ApcContext

Parameter to `ApcRoutine`.

### IoStatusBlock

IO result of call.

### Buffer

Buffer with data to write.

### Length

Length of `Buffer`, in bytes.

### ByteOffset

Offset from beginning of file, where write starts.

### Key

??? (See `NtReadFile`).

# Related Win32 API
 - [`WriteFile`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-writefile) (Although it does more than just forwarding the arguments and invoking this procedure.) 

# Documented by

* Tomasz Nowak

# See also

* `NtCreateFile`
* `NtOpenFile`
* `NtReadFile`
