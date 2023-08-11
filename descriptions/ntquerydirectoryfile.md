NtQueryDirectoryFile is used to enumerate entries \
\(files or directories\) placed into file container object \
\(directory\). Win32 API use it in \
FindFirstFile\-FindNextFile routines. \
FileHandle HANDLE to File Object \
opened with FILE\_DIRECTORY\_FILE option and \
FILE\_LIST\_DIRECTORY access. \
Event Optional HANDLE to Event \
Object signaled after query complete. \
ApcRoutine Optinal pointer to user's \
APC routine queued after query complete. \
ApcContext Parameter for ApcRoutine. \
IoStatusBlock Pointer to \
IO\_STATUS\_BLOCK structure. After enumeration complete, \
Information member of this structure contains number \
of bytes writed into FileInformation buffer. Status \
member contains IO result of call, and can be one of: \
STATUS\_SUCCESS \- Enumeration has results in FileInformation buffer. \
STATUS\_NO\_MORE\_FILES \- FileInformation buffer is empty, and next \
call isn't needed. \
STATUS\_NO\_SUCH\_FILE \- Returned when FileMask parameter specify exactly one file \
\(don't contains '\*' or \
'?' characters\), and \
queried directory don't contains that file. \
FileInformation User's allocated buffer \
for output data. \
Length Length of FileInformation buffer, in bytes. \
FileInformationClass Information class. \
Can be one of: \
FileDirectoryInformation \
FileFullDirectoryInformation \
FileBothDirectoryInformation \
FileNamesInformation \
FileOleDirectoryInformation \
ReturnSingleEntry If set, only one \
entry is returned. \
FileMask If specified, only information \
about files matches this wildchar mask will be returned. \
WARNING: There's no rule specifing \
what to do when caller makes two calls to \
NtQueryDirectoryFile both with different masks. \
Typically FileMask specified in \
second call will be ignored, and results will match the first \(for \
example: NTFS.SYS\). The best solution is to close \
directory HANDLE after every call with FileMask parameter specified. \
RestartScan Used with ReturnSingleEntry parameter. If set, \
NtQueryDirectoryFile continue enumeration after last \
enumerated element in previous call. If no, returns the first entry \
in directory. \
For detailed information about results, see FILE\_INFORMATION\_CLASS with \
information classes specified above.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
NtCreateFile \
NtOpenFile \
NtQueryInformationFile \
NtQueryOleDirectoryFile \
NtQueryVolumeInformationFile
