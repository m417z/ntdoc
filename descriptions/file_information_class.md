Enumeration type FILE\_INFORMATION\_CLASS defines \
informational classes for File Objects. It's used by \
NtQueryInformationFile, \
NtQueryDirectoryFile and \
NtSetInformationFile functions. \
FileDirectoryInformation=1 \
Action \
: Query \
Buffer size \
: 0x48 \
Structure \
: FILE\_DIRECTORY\_INFORMATION \
Function \
: NtQueryDirectoryFile \
FileFullDirectoryInformation \
Action \
: Query \
Buffer size \
: 0x48 \
Structure \
: FILE\_FULL\_DIR\_INFORMATION \
Function \
: NtQueryDirectoryFile \
FileBothDirectoryInformation \
Action \
: Query \
Buffer size \
: 0x48 \
Structure \
: FILE\_BOTH\_DIR\_INFORMATION \
Function \
: NtQueryDirectoryFile \
FileBasicInformation \
Action \
: Query \
Buffer size \
: 0x28 \
Structure \
: FILE\_BASIC\_INFORMATION \
Function \
: NtQueryInformationFile \
Action \
: Set \
Buffer size \
: 0x28 \
Structure \
: FILE\_BASIC\_INFORMATION \
Function \
: NtSetInformationFile \
FileStandardInformation \
Action \
: Query \
Buffer size \
: 0x18 \
Structure \
: FILE\_STANDARD\_INFORMATION \
Function \
: NtQueryInformationFile \
FileInternalInformation \
Action \
: Query \
Buffer size \
: 0x08 \
Structure \
: FILE\_INTERNAL\_INFORMATION \
Function \
: NtQueryInformationFile \
FileEaInformation \
Action \
: Query \
Buffer size \
: 0x04 \
Structure \
: FILE\_EA\_INFORMATION \
Function \
: NtQueryInformationFile \
FileAccessInformation // 8 \
FILE\_ACCESS\_INFORMATION 0x04 NtQueryInformationFile \
FileNameInformation \
Action \
: Query \
Buffer size \
: 0x08\+ \
Structure \
: FILE\_NAME\_INFORMATION \
Function \
: NtQueryInformationFile \
FileRenameInformation \
Action \
: Set \
Buffer size \
: 0x10 \
Structure \
: FILE\_RENAME\_INFORMATION \
Function \
: NtSetInformationFile \
FileLinkInformation \
Action \
: Set \
Buffer size \
: 0x10 \
Structure \
: FILE\_LINK\_INFORMATION \
Function \
: NtSetInformationFile \
FileNamesInformation \
Action \
: Query \
Buffer size \
: 0x10 \
Structure \
: FILE\_NAMES\_INFORMATION \
Function \
: NtQueryDirectoryFile \
FileDispositionInformation \
Action \
: Set \
Buffer size \
: 0x01 \
Structure \
: FILE\_DISPOSITION\_INFORMATION \
Function \
: NtSetInformationFile \
FilePositionInformation \
Action \
: Query \
Buffer size \
: 0x08 \
Structure \
: FILE\_POSITION\_INFORMATION \
Function \
: NtQueryInformationFile \
Action \
: Set \
Buffer size \
: 0x08 \
Structure \
: FILE\_POSITION\_INFORMATION \
Function \
: NtSetInformationFile \
FileFullEaInformation // 15 \
FILE\_FULL\_EA\_INFORMATION ??? ??? \
FileModeInformation // 16 \
FILE\_MODE\_INFORMATION 0x04 0x04 NtQueryInformationFile \
FileAlignmentInformation // 17 \
FILE\_ALIGNMENT\_INFORMATION 0x04 NtQueryInformationFile \
FileAllInformation \
Action \
: Query \
Buffer size \
: 0x68 \
Structure \
: FILE\_ALL\_INFORMATION \
Function \
: NtQueryInformationFile \
FileAllocationInformation // 19 \
FILE\_ALLOCATION\_INFORMATION 0x08 \
FileEndOfFileInformation \
Action \
: Set \
Buffer size \
: 0x08 \
Structure \
: FILE\_END\_OF\_FILE\_INFORMATION \
Function \
: NtSetInformationFile \
FileAlternateNameInformation \
Action \
: Query \
Buffer size \
: 0x08\+ \
Structure \
: FILE\_NAME\_INFORMATION \
Function \
: NtQueryInformationFile \
FileStreamInformation // 22 \
FILE\_STREAM\_INFORMATION 0x20 NtQueryInformationFile \
FilePipeInformation // 23 \
FILE\_PIPE\_INFORMATION 0x08 0x08 NtQueryInformationFile \
FilePipeLocalInformation // 24 \
FILE\_PIPE\_LOCAL\_INFORMATION 0x28 NtQueryInformationFile \
FilePipeRemoteInformation // 25 \
FILE\_PIPE\_REMOTE\_INFORMATION 0x10 0x10 NtQueryInformationFile \
FileMailslotQueryInformation // 26 \
FILE\_MAILSLOT\_QUERY\_INFORMATION 0x18 NtQueryInformationFile \
FileMailslotSetInformation // 27 \
FILE\_MAILSLOT\_SET\_INFORMATION 0x04 \
FileCompressionInformation // 28 \
FILE\_COMPRESSION\_INFORMATION 0x10 NtQueryInformationFile \
FileCopyOnWriteInformation // 29 \
FILE\_COPY\_ON\_WRITE\_INFORMATION 0x10 \
FileCompletionInformation \
Action \
: Set \
Buffer size \
: 0x08 \
Structure \
: FILE\_COMPLETION\_INFORMATION \
Function \
: NtSetInformationFile \
FileMoveClusterInformation // 31 0x10 \
FileQuotaInformation // 32 \
FILE\_QUOTA\_INFORMATION 0x10 \-&gt; FileOleClassIdInformation \
FileReparsePointInformation // 33 0x08 \
\-&gt; FileOleStateBitsInformation \
FileNetworkOpenInformation \
Action \
: Query \
Buffer size \
: 0x38 \
Structure \
: FILE\_NETWORK\_OPEN\_INFORMATION \
Function \
: NtQueryInformationFile \
FileObjectIdInformation // 35 \
FILE\_ATTRIBUTE\_TAG\_INFORMATION 0x14 \
FileTrackingInformation // 36 0xC0 \
NtQueryInformationFile \-&gt; FileOleAllInformation \
FileOleDirectoryInformation // 37 0x60 \
NtQueryDirectoryFile \
FileContentIndexInformation // 38 0x01 \
FileInheritContentIndexInformation // \
39 0x01 \
FileOleInformation // 40 0x38 0x38 \
NtQueryInformationFile \
FileMaximumInformation // 41

Documented by: \
Tomasz Nowak \
Bo Branten \
SysInternals \
Requirements:

Library: ntdll.lib

See also: \
NtQueryDirectoryFile \
NtQueryInformationFile \
NtQueryOleDirectoryFile \
NtSetInformationFile
