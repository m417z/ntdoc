This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information).

---

Structure `FILE_FULL_EA_INFORMATION` is used for get or store Extended Attributes for *NTFS* files and directories. \
Extended Attributes (*EA*) is a list of pair **Name-Value**. Name is capitalised *ASCII* string up to *256* characters long. Value is any data and can be up to *65536* bytes long.

Structure can be used in a call to `NtCreateFile` and `NtSetEaFile`, or as a result of call `NtQueryEaFile`.

### NextEntryOffset

Offset for next `FILE_FULL_EA_INFORMATION` structure in buffer, relative to currently used structure. If current structure is last one in buffer, this field has value *0*.

### Flags

???

### EaNameLength

Length of EA name, in bytes (without leading zero).

### EaValueLength

Length of EA value, in bytes (without leading zero).

### EaName[1]

User's allocated buffer contains ASCIIZ name and value. ASCII value must be finished by zero.

---

Structure `FILE_FULL_EA_INFORMATION` is also defined in *Win2000 DDK*.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `FILE_EA_INFORMATION`
* `FILE_GET_EA_INFORMATION`
* `NtCreateFile`
* `NtQueryEaFile`
* `NtSetEaFile`
