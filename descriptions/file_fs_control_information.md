This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_control_information).

---

Structure `FILE_FS_CONTROL_INFORMATION` is user as input and output buffers in calls to `NtQueryVolumeInformationFile` and `NtSetVolumeInformationFile` with information class set to `FileFsControlInformation`.

### FreeSpaceStartFiltering

### FreeSpaceThreshold

### FreeSpaceStopFiltering

### DefaultQuotaThreshold

### DefaultQuotaLimit

### FileSystemControlFlags

# Documented by

* Bo Branten

# See also

* `FS_INFORMATION_CLASS`
* `NtQueryVolumeInformationFile`
* `NtSetVolumeInformationFile`
