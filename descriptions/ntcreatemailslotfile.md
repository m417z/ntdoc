Function `NtCreateMailslotFile` creates especial File Object called *Mailslot*. See *Microsoft SDK* for more information about *Mailslots*.

### MailslotFileHandle

Result of call - `HANDLE` to Mailslot File Object.

### DesiredAccess

Access rights associated with opened handle.

### ObjectAttributes

Pointer to `OBJECT_ATTRIBUTES` structure contains valid object name. Name must be in format **"\\\\??\\MAILSLOT\\..."** where **"..."** means unique name of Mailslot.

### IoStatusBlock

IO result of call.

### CreateOptions

Can be combination of:

* `FILE_WRITE_THROUGH`
* `FILE_SYNCHRONOUS_IO_ALERT`
* `FILE_SYNCHRONOUS_IO_NONALERT`

### MailslotQuota

???

### MaxMessageSize

Maximum message size, or `MAILSLOT_SIZE_AUTO` for automatic message size.

### ReadTimeOut

Timeout value, or *-1* for infinite waiting.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `FILE_MAILSLOT_QUERY_INFORMATION`
* `FILE_MAILSLOT_SET_INFORMATION`
* `NtQueryInformationFile`
* `NtReadFile`
* `NtSetInformationFile`
* `NtWriteFile`
