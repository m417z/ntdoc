### ThreadHandle

Pointer to received handle to thread object.

### AccessMask

Access mask. See `WinNT.h` for details.

### ObjectAttributes

Attributes of thread to open. For standard threads there are empty.

### ClientId

Pointer to `CLIENT_ID` structure. Only `UniqueThread` member is required (difference to `NtOpenProcess`).

# Documented by

* Tomasz Nowak

# See also

* `NtCreateThread`
* `NtOpenProcess`
* `NtTerminateThread`
