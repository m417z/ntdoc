This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwmapviewofsection).

---

Function `NtMapViewOfSection` maps specified part of Section Object into process memory.

### SectionHandle

`HANDLE` to Section Object opened with one or more from `SECTION_MAP_EXECUTE`, `SECTION_MAP_READ`, `SECTION_MAP_WRITE` attributes.

### ProcessHandle

`HANDLE` to Process Object opened with `PROCESS_VM_OPERATION` access.

### *BaseAddress

Pointer to variable receiving virtual address of mapped memory. If this value is not *NULL*, system tries to allocate memory from specified value.

### ZeroBits

Indicates how many high bits must not be set in `BaseAddress`.

### CommitSize

Size of initially committed memory, in bytes.

### SectionOffset

Pointer to begin of mapped block in section. This value must be rounded up to `X64K` block size (*0x10000* on **X86**).

### ViewSize

Pointer to size of mapped block, in bytes. This value is rounded up to page size (*0x1000* on **x86**).

### InheritDisposition

How do child processes inherit mapped section. See description of enumeration type `SECTION_INHERIT`.

### AllocationType

Can be one of:

* `MEM_COMMIT`
* `MEM_RESERVE`

### Protect

Page protection. Can be one of:

* `PAGE_NOACCESS`
* `PAGE_READONLY`
* `PAGE_READWRITE`
* `PAGE_WRITECOPY`
* `PAGE_EXECUTE`
* `PAGE_EXECUTE_READ`
* `PAGE_EXECUTE_READWRITE`
* `PAGE_EXECUTE_WRITECOPY`
* `PAGE_GUARD`
* `PAGE_NOCACHE`
* `PAGE_WRITECOMBINE`

# Documented by

* Tomasz Nowak

# See also

* `NtAllocateVirtualMemory`
* `NtCreateSection`
* `NtOpenSection`
* `NtUnmapViewOfSection`
