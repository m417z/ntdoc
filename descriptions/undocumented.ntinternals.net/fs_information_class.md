This enumeration is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/ne-wdm-_fsinfoclass).

---

`FS_INFORMATION_CLASS` enumeration type is used in a call to `NtQueryVolumeInformationFile` and `NtSetVolumeInformationFile`.

### FileFsVolumeInformation

* Action: `Query`
* Buffer size: *0x18*
* Structure: `FILE_FS_VOLUME_INFORMATION`

### FileFsLabelInformation

* Action: `Set`
* Buffer size: *0x08*
* Structure: `FILE_FS_LABEL_INFORMATION`

### FileFsSizeInformation

* Action: `Query`
* Buffer size: *0x18*
* Structure: `FILE_FS_SIZE_INFORMATION`

### FileFsDeviceInformation

* Action: `Query`
* Buffer size: *0x08*
* Structure: `FILE_FS_DEVICE_INFORMATION`

### FileFsAttributeInformation

* Action: `Query`
* Buffer size: *0x10*
* Structure: `FILE_FS_ATTRIBUTE_INFORMATION`

### FileFsControlInformation

* Action: `Query, Set`
* Buffer size: *0x30, 0x30*
* Structure: `FILE_FS_CONTROL_INFORMATION`

### FileFsFullSizeInformation

* Action: `Query`
* Buffer size: *0x38*
* Structure: ???

### FileFsObjectIdInformation

* Action: `Set`
* Buffer size: *0x38*
* Structure: ???

# Documented by

* Tomasz Nowak
* Bo Branten
* ReactOS

# See also

* `FILE_FS_ATTRIBUTE_INFORMATION`
* `FILE_FS_CONTROL_INFORMATION`
* `FILE_FS_DEVICE_INFORMATION`
* `FILE_FS_LABEL_INFORMATION`
* `FILE_FS_SIZE_INFORMATION`
* `FILE_FS_VOLUME_INFORMATION`
* `NtQueryVolumeInformationFile`
* `NtSetVolumeInformationFile`
