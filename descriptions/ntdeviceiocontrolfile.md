This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwdeviceiocontrolfile), [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntdeviceiocontrolfile), and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeviceiocontrolfile).

Function NtDeviceIoControlFile sends IOCTL\_\* \
control code to Device Driver. It is primary \(but not the best\) \
solution to communicate between application and Device Driver. \
FileHandle HANDLE to Device \
Object opened as a file. \
Event Optional HANDLE to Event \
Object signalled on the end of processing request. \
ApcRoutine Optional pointer to user's \
APC Routine called on the end of processing request. \
ApcContext User's parameter to \
ApcRoutine. \
IoStatusBlock IO result of call. \
IoControlCode IO Control code \
\[IOCTL\_\*\]. \
InputBuffer User's allocated buffer \
with input data. \
InputBufferLength Length of \
InputBuffer, in bytes. \
OutputBuffer User's allocated buffer \
for result data. \
OutputBufferLength Length of \
OutputBuffer, in bytes. \
See also NtFsControlFile.

Documented by: \
Tomasz Nowak \
Reactos \
Requirements:

Library: ntdll.lib

See also: \
NtCreateFile \
NtFsControlFile \
NtOpenFile
