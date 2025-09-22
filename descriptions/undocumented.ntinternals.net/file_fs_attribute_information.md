This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_attribute_information).

---

`FILE_FS_ATTRIBUTE_INFORMATION` is output buffer in a call to `NtQueryVolumeInformationFile` function with `FileFsAttributeInformation` information class.

### FileSystemAttributes

??? *(0x1F)*

### MaximumComponentNameLength

Maximum length of file name on specified device.

### FileSystemNameLength

Length of `FileSystemName` array, in bytes.

### FileSystemName[1]

Name of File System on specified device (ex. **"NTFS"**).

# Documented by

* Bo Branten
* Tomasz Nowak

# See also

* `FS_INFORMATION_CLASS`
* `NtQueryVolumeInformationFile`
