This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_label_information).

---

Structure is an input buffer for `NtSetVolumeInformationFile` call with information class `FileFsLabelInformation`.

### VolumeLabelLength

Length of `VolumeLabel` array, in bytes.

### VolumeLabel[1]

Label for specified volume.

# Documented by

* Bo Branten
* Tomasz Nowak

# See also

* `FS_INFORMATION_CLASS`
* `NtSetVolumeInformationFile`
