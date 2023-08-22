This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_volume_information).

---

Structure provides basic information about volume. It's filled in a result of call `NtQueryVolumeInformationFile` with `FileFsVolumeInformation` class.

### VolumeCreationTime

It means time of last Volume Formating Process.

### VolumeSerialNumber

Serial number of volume, associated in Volume Formating Process.

### VolumeLabelLength

Length of `VolumeLabel` array, in bytes.

### SupportsObjects

If TRUE, Object Files can be stored on specified volume.

### VolumeLabel[1]

Name of volume. Can be set with `FileFsLabelInformation`.

# Documented by

* Bo Branten
* Tomasz Nowak

# See also

* `FILE_FS_LABEL_INFORMATION`
* `FS_INFORMATION_CLASS`
* `NtQueryVolumeInformationFile`
