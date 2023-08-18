Enumeration type `FILE_INFORMATION_CLASS` defines informational classes for File Objects. It's used by `NtQueryInformationFile`, `NtQueryDirectoryFile` and `NtSetInformationFile` functions.

### FileDirectoryInformation=1

* Action: `Query`
* Buffer size: *0x48*
* Structure: `FILE_DIRECTORY_INFORMATION`
* Function: `NtQueryDirectoryFile`

### FileFullDirectoryInformation

* Action: `Query`
* Buffer size: *0x48*
* Structure: `FILE_FULL_DIR_INFORMATION`
* Function: `NtQueryDirectoryFile`

### FileBothDirectoryInformation

* Action: `Query`
* Buffer size: *0x48*
* Structure: `FILE_BOTH_DIR_INFORMATION`
* Function: `NtQueryDirectoryFile`

### FileBasicInformation

* Action: `Query`
* Buffer size: *0x28*
* Structure: `FILE_BASIC_INFORMATION`
* Function: `NtQueryInformationFile`

<!-- -->

* Action: `Set`
* Buffer size: *0x28*
* Structure: `FILE_BASIC_INFORMATION`
* Function: `NtSetInformationFile`

### FileStandardInformation

* Action: `Query`
* Buffer size: *0x18*
* Structure: `FILE_STANDARD_INFORMATION`
* Function: `NtQueryInformationFile`

### FileInternalInformation

* Action: `Query`
* Buffer size: *0x08*
* Structure: `FILE_INTERNAL_INFORMATION`
* Function: `NtQueryInformationFile`

### FileEaInformation

* Action: `Query`
* Buffer size: *0x04*
* Structure: `FILE_EA_INFORMATION`
* Function: `NtQueryInformationFile`

### FileAccessInformation

`// 8       FILE_ACCESS_INFORMATION         0x04            NtQueryInformationFile`

### FileNameInformation

* Action: `Query`
* Buffer size: *0x08+*
* Structure: `FILE_NAME_INFORMATION`
* Function: `NtQueryInformationFile`

### FileRenameInformation

* Action: `Set`
* Buffer size: *0x10*
* Structure: `FILE_RENAME_INFORMATION`
* Function: `NtSetInformationFile`

### FileLinkInformation

* Action: `Set`
* Buffer size: *0x10*
* Structure: `FILE_LINK_INFORMATION`
* Function: `NtSetInformationFile`

### FileNamesInformation

* Action: `Query`
* Buffer size: *0x10*
* Structure: `FILE_NAMES_INFORMATION`
* Function: `NtQueryDirectoryFile`

### FileDispositionInformation

* Action: `Set`
* Buffer size: *0x01*
* Structure: `FILE_DISPOSITION_INFORMATION`
* Function: `NtSetInformationFile`

### FilePositionInformation

* Action: `Query`
* Buffer size: *0x08*
* Structure: `FILE_POSITION_INFORMATION`
* Function: `NtQueryInformationFile`

<!-- -->

* Action: `Set`
* Buffer size: *0x08*
* Structure: `FILE_POSITION_INFORMATION`
* Function: `NtSetInformationFile`

### FileFullEaInformation

`// 15      FILE_FULL_EA_INFORMATION        ???     ???`

### FileModeInformation

`// 16      FILE_MODE_INFORMATION           0x04    0x04    NtQueryInformationFile`

### FileAlignmentInformation

`// 17      FILE_ALIGNMENT_INFORMATION      0x04            NtQueryInformationFile`

### FileAllInformation

* Action: `Query`
* Buffer size: *0x68*
* Structure: `FILE_ALL_INFORMATION`
* Function: `NtQueryInformationFile`

### FileAllocationInformation

`// 19      FILE_ALLOCATION_INFORMATION             0x08`

### FileEndOfFileInformation

* Action: `Set`
* Buffer size: *0x08*
* Structure: `FILE_END_OF_FILE_INFORMATION`
* Function: `NtSetInformationFile`

### FileAlternateNameInformation

* Action: `Query`
* Buffer size: *0x08+*
* Structure: `FILE_NAME_INFORMATION`
* Function: `NtQueryInformationFile`

### FileStreamInformation

`// 22      FILE_STREAM_INFORMATION         0x20            NtQueryInformationFile`

### FilePipeInformation

`// 23      FILE_PIPE_INFORMATION           0x08    0x08    NtQueryInformationFile`

### FilePipeLocalInformation

`// 24      FILE_PIPE_LOCAL_INFORMATION     0x28            NtQueryInformationFile`

### FilePipeRemoteInformation

`// 25      FILE_PIPE_REMOTE_INFORMATION    0x10    0x10    NtQueryInformationFile`

### FileMailslotQueryInformation

`// 26      FILE_MAILSLOT_QUERY_INFORMATION 0x18            NtQueryInformationFile`

### FileMailslotSetInformation

`// 27      FILE_MAILSLOT_SET_INFORMATION           0x04`

### FileCompressionInformation

`// 28      FILE_COMPRESSION_INFORMATION    0x10            NtQueryInformationFile`

### FileCopyOnWriteInformation

`// 29      FILE_COPY_ON_WRITE_INFORMATION          0x10`

### FileCompletionInformation

* Action: `Set`
* Buffer size: *0x08*
* Structure: `FILE_COMPLETION_INFORMATION`
* Function: `NtSetInformationFile`

### FileMoveClusterInformation

`// 31                                              0x10`

### FileQuotaInformation

`// 32      FILE_QUOTA_INFORMATION                  0x10                                    -\> FileOleClassIdInformation`

### FileReparsePointInformation

`// 33                                              0x08                                    -\> FileOleStateBitsInformation`

### FileNetworkOpenInformation

* Action: `Query`
* Buffer size: *0x38*
* Structure: `FILE_NETWORK_OPEN_INFORMATION`
* Function: `NtQueryInformationFile`

### FileObjectIdInformation

`// 35      FILE_ATTRIBUTE_TAG_INFORMATION          0x14`

### FileTrackingInformation

`// 36                                      0xC0            NtQueryInformationFile          -\> FileOleAllInformation`

### FileOleDirectoryInformation

`// 37                                      0x60            NtQueryDirectoryFile`

### FileContentIndexInformation

`// 38                                              0x01`

### FileInheritContentIndexInformation

`// 39                                              0x01`

### FileOleInformation

`// 40                                      0x38    0x38    NtQueryInformationFile`

### FileMaximumInformation

`// 41`

# Documented by

* Tomasz Nowak
* Bo Branten
* SysInternals

# See also

* `NtQueryDirectoryFile`
* `NtQueryInformationFile`
* `NtQueryOleDirectoryFile`
* `NtSetInformationFile`
