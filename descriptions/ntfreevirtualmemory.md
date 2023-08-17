This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntfreevirtualmemory) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwfreevirtualmemory).

---

### RegionSize

If you put pointer to *NULL* value as `RegionSize`, system will free all region, and put size of it in result.

### FreeType

Can be one of the values:  `MEM_DECOMMIT`, or `MEM_RELEASE`.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `NtAllocateVirtualMemory`
