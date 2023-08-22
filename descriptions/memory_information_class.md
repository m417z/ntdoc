This enumeration is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/ne-ntifs-_memory_information_class).

---

Enumeration type `MEMORY_INFORMATION_CLASS` specify type of information returned in a call to `NtQueryVirtualMemory` function. Currently only one class is defined.

### MemoryBasicInformation

Result buffer contains structure `MEMORY_BASIC_INFORMATION`.

# Documented by

* Tomasz Nowak

# See also

* `MEMORY_BASIC_INFORMATION`
* `NtQueryVirtualMemory`
