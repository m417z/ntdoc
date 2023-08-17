This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatesection) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatesection).

---

Function `NtCreateSection` creates Section Object (virtual memory block with associated file).

### SectionHandle

Result of call - `HANDLE` to Section Object.

### DesiredAccess

Access mask. Can be combination of:

* `SECTION_QUERY`

* `SECTION_MAP_WRITE`
* `SECTION_MAP_READ`

* `SECTION_MAP_EXECUTE`
* `SECTION_EXTEND_SIZE`

* `SECTION_ALL_ACCESS`

### ObjectAttributes

Pointer to `OBJECT_ATTRIBUTES` structure contains section name, in Object Namespace format.

### MaximumSize

Optionally define maximum size of section. Must be defined when caller create section based on system *PageFile*.

### PageAttributess

Can be one or combination of:

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

### SectionAttributes

Can be one or combination of:

* `SEC_FILE`

* `SEC_IMAGE`
* `SEC_RESERVE`

* `SEC_COMMIT`
* `SEC_NOCACHE`

### FileHandle

Optionally `HANDLE` to File Object opened with proper access.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateFile`
* `NtExtendSection`
* `NtFlushVirtualMemory`
* `NtMapViewOfSection`
* `NtOpenFile`
* `NtOpenSection`
* `NtQuerySection`
