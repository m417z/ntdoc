### HeapHandle

Address of heap.

### Protect

If set, memory is protected to `PAGE_READONLY`. If zero, protect with `PAGE_READWRITE`.

### Return value

Result is address of protected or unprotected heap.

# Documented by

* Tomasz Nowak

# See also

* `NtProtectVirtualMemory`
* `RtlLockHeap`
