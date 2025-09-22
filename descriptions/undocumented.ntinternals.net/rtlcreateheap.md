This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-rtlcreateheap).

---

### Flags

Flags are defined in **\<WinNT.h\>**. Can be one of following:

* `HEAP_NO_SERIALIZE`
* `HEAP_GROWABLE`
* `HEAP_GENERATE_EXCEPTIONS`
* `HEAP_ZERO_MEMORY`
* `HEAP_REALLOC_IN_PLACE_ONLY`
* `HEAP_TAIL_CHECKING_ENABLED`
* `HEAP_FREE_CHECKING_ENABLED`
* `HEAP_DISABLE_COALESCE_ON_FREE`
* `HEAP_CREATE_ALIGN_16`
* `HEAP_CREATE_ENABLE_TRACING`

### Base

Base address, where heap should be created. If memory was previously allocated at this address, heap is created at the nearest possible virtual address.

### Reserve

How much bytes should be reserved. See `NtAllocateVirtualMemory`.

### Commit

How many bytes should be committed. If `Reserve` is greater than zero, `Commit` must be less or equal to `Reserve`.

### Lock

If set, heap will be locked. See `RtlLockHeap` / `RtlUnlockHeap`.

### RtlHeapParams

Pointer to `RTL_HEAP_DEFINITION` structure. On *NT 4.0* all bytes of this (except length field) are set to zero.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `NtAllocateVirtualMemory`
* `NtLockVirtualMemory`
* `RTL_HEAP_DEFINITION`
* `RtlDestroyHeap`
* `RtlLockHeap`
* `RtlUnlockHeap`
