### ProcessHandle

Handle to Process Object opened with `PROCESS_VM_OPERATION` access.

### *BaseAddress

Pointer to base address to protect. Protection will change on all page containing specified address. On output, `BaseAddress` will point to page start address.

### NumberOfBytesToProtect

Pointer to size of region to protect. On output will be round to page size (4KB).

### NewAccessProtection

One or some of `PAGE_...` attributes.

### OldAccessProtection

Receive previous protection.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `NtAllocateVirtualMemory`
* `NtQueryVirtualMemory`
