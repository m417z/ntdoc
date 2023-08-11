Function NtCreateIoCompletion creates IO Completion \
Object. IO Completion Object is used for waiting on pending IO \
operation \(reading or writing\) in multi\-process file access. It \
contains more informations about IO operation than synchronization \
event or APC Routine. \
IoCompletionHandle Result of call \- \
HANDLE to newly created IO Completion Object. \
DesiredAccess Access mask for created \
HANDLE. Can be combination of: \
IO\_COMPLETION\_QUERY\_STATE \
IO\_COMPLETION\_MODIFY\_STATE \
IO\_COMPLETION\_ALL\_ACCESS \
ObjectAttributes Optionally contains \
object name, in Objects Namespace. \
NumberOfConcurrentThreads Number of \
threads accessing File Object associated with IO Completion. If \
Zero, system reserves memory for number of threads equal to current \
nymber of processes.

Documented by: \
Tomasz Nowak \
Reactos \
Requirements:

Library: ntdll.lib

See also: \
FILE\_INFORMATION\_CLASS \
NtOpenIoCompletion \
NtQueryIoCompletion \
NtRemoveIoCompletion \
NtSetInformationFile \
NtSetIoCompletion
