Structure `SYSTEM_PAGEFILE_INFORMATION` is used as a result of call `NtQuerySystemInformation` with `SystemPageFileInformation` information class. If contains information about currently instaled Paged Files (files used by system for swap paged pool memory to disk).

### NextEntryOffset

Offset to next `SYSTEM_PAGEFILE_INFORMATION` structure or zero, if it's last one.

### TotalSize

Size of paged file, in pages (Size of page depend on machine type, for **x86** one page is *0x1000* (*4096*) bytes).

### TotalInUse

Number of currently used pages in paged file.

### PeakUsage

Maximum number of pages used in this boot session.

### PageFileName

System path to paged file.

# Documented by

* Tomasz Nowak

# See also

* `NtCreatePagingFile`
* `NtQuerySystemInformation`
* `SYSTEM_INFORMATION_CLASS`
