Function NtCreateMailslotFile creates especial File \
Object called Mailslot. See Microsoft SDK for more \
information about Mailslots. \
MailslotFileHandle Result of call \- \
HANDLE to Mailslot File Object. \
DesiredAccess Access rights associated \
with opened handle. \
ObjectAttributes Pointer to \
OBJECT\_ATTRIBUTES structure contains valid object name. Name \
must be in format "\\\\??\\MAILSLOT\\..." \
where "..." means unique name of \
Mailslot. \
IoStatusBlock IO result of call. \
CreateOptions Can be combination \
of: \
FILE\_WRITE\_THROUGH \
FILE\_SYNCHRONOUS\_IO\_ALERT \
FILE\_SYNCHRONOUS\_IO\_NONALERT \
MailslotQuota \- ??? \
MaxMessageSize Maximum message size, or \
MAILSLOT\_SIZE\_AUTO for automatic message size. \
ReadTimeOut Timeout value, or \-1 \
for infinite waiting.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
FILE\_MAILSLOT\_QUERY\_INFORMATION \
FILE\_MAILSLOT\_SET\_INFORMATION \
NtQueryInformationFile \
NtReadFile \
NtSetInformationFile \
NtWriteFile
