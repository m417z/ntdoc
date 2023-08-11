Function NtQueryIoCompletion receives number of file \
operations pending on specified IO Completion Object. \
IoCompletionHandle HANDLE to IO \
Completion Object opened with IO\_COMPLETION\_QUERY\_STATE \
access. \
InformationClass See IO\_COMPLETION\_INFORMATION\_CLASS \
for possible values. \
IoCompletionInformation User's \
allocated buffer for result data. \
InformationBufferLength Length of \
IoCompletionInformation buffer, \
in bytes. \
RequiredLength Optionally receives \
required length of buffer.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
IO\_COMPLETION\_INFORMATION\_CLASS \
NtCreateIoCompletion \
NtOpenIoCompletion \
NtRemoveIoCompletion \
NtSetIoCompletion
