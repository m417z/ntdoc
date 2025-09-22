This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntallocatevirtualmemory) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwallocatevirtualmemory).

---

### ProcessHandle

Handle to Process Object opened with `PROCESS_VM_OPERATION` access.

### *BaseAddress

If not zero, system tries to allocate virtual memory block on this virtual address. If BaseAddress is zero, system use first free virtual location.

### AllocationType

Can be `MEM_RESERVE` or `MEM_COMMIT`.

### Protect

One or combination of `PAGE_***` attributes.

# Documented by

* ReactOS
* Tomasz Nowak

# See also

* `NtFreeVirtualMemory`
* `NtMapViewOfSection`
