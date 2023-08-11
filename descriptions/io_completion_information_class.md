Enumeration type IO\_COMPLETION\_INFORMATION\_CLASS is \
used with \
NtQueryIoCompletion function to get information about IO \
Completion object. Currently only one information class is \
defined. \
IoCompletionBasicInformation Buffer \
receiving data is descripted as \
IO\_COMPLETION\_BASIC\_INFORMATION structure and has 0x04 \
bytes length.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
IO\_COMPLETION\_BASIC\_INFORMATION \
NtQueryIoCompletion
