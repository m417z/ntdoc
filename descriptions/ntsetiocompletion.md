Function NtSetIoCompletion increments pending IO \
counter in IO Completion Object. It can be used to manual finish IO \
operation. \
IoCompletionHandle HANDLE to IO \
Completion Object opened with IO\_COMPLETION\_MODIFY\_STATE \
access. \
CompletionKey User's defined key \
received by \
NtRemoveIoCompletion function. \
IoStatusBlock IO result of call. \
CompletionStatus IO operation \
status. \
NumberOfBytesTransfered Number of bytes \
transfered in manually finished IO operation.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateIoCompletion \
NtOpenIoCompletion \
NtQueryIoCompletion \
NtRemoveIoCompletion
