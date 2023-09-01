Function `NtFlushInstructionCache` empties execution cache for specified region of code. It should be used always after modification of process's executable memory (for example when *NtLdr* fills imported function's entries).

### ProcessHandle

`HANDLE` to Process Object.

### BaseAddress

Starting memory address to flush.

### NumberOfBytesToFlush

Length of flushed memory block.

# Documented by

* ReactOS
* Tomasz Nowak

# See also

* `NtOpenProcess`
