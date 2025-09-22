This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_get_ea_information).

---

Structure `FILE_GET_EA_INFORMATION` is used in a call to `NtQueryEaFile` function. See `FILE_FULL_EA_INFORMATION` for detailed information about *EA*.

### NextEntryOffset

Relative offset for next `FILE_GET_EA_INFORMATION` structure in buffer.

### EaNameLength

Length of *EA* name, in bytes (without leading zero).

### EaName[1]

*ASCIIZ* name of *EA*, case insensitive.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `FILE_FULL_EA_INFORMATION`
* `NtQueryEaFile`
