This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_size_information).

---

Structure provides detailed information about volume physical size. Is returned in call to `NtQueryVolumeInformationFile` with `FileFsSizeInformation` information class.

### TotalAllocationUnits

### AvailableAllocationUnits

### SectorsPerAllocationUnit

### BytesPerSector

# Documented by

* Bo Branten
* Tomasz Nowak

# See also

* `FS_INFORMATION_CLASS`
* `NtQueryVolumeInformationFile`
