NtNotifyChangeDirectoryFile is used to process \
changes to directory File Object. Becouse function returns \
immediatelly with STATUS\_PENDING, you must decide to use \
Event Object or APC routine as notification form. \
FileHandle HANDLE to File Object \
opened with SYNCHRONIZE access and \
FILE\_DIRECTORY\_FILE option set. \
Event HANDLE to Event Object. \
Event can be created as \
NotificationEvent or \
SynchronizationEvent, but second one is better in this \
situation. \
ApcRoutine Address of user's APC \
routine, queued when change complete. \
ApcContext Optional parameter for \
ApcRoutine. \
IoStatusBlock IO result of call. \
Status member in IoStatusBlock can result \
STATUS\_NOTIFY\_ENUM\_DIR when Buffer was to small. \
Buffer User's allocated buffer for \
change informations. It contains one or more of FILE\_NOTIFY\_INFORMATION \
structures. \
BufferSize Size of Buffer, in bytes. \
CompletionFilter Mask specifing what \
sort of changes should be monitored. Can be combination \
of: \
FILE\_NOTIFY\_CHANGE\_FILE\_NAME \
FILE\_NOTIFY\_CHANGE\_DIR\_NAME \
FILE\_NOTIFY\_CHANGE\_NAME \
FILE\_NOTIFY\_CHANGE\_ATTRIBUTES \
FILE\_NOTIFY\_CHANGE\_SIZE \
FILE\_NOTIFY\_CHANGE\_LAST\_WRITE \
FILE\_NOTIFY\_CHANGE\_LAST\_ACCESS \
FILE\_NOTIFY\_CHANGE\_CREATION \
FILE\_NOTIFY\_CHANGE\_EA \
FILE\_NOTIFY\_CHANGE\_SECURITY \
FILE\_NOTIFY\_CHANGE\_STREAM\_NAME \
FILE\_NOTIFY\_CHANGE\_STREAM\_SIZE \
FILE\_NOTIFY\_CHANGE\_STREAM\_WRITE \
WatchTree If set, all subdirectiories \
of specified directory will be also monitored.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
EVENT\_TYPE \
FILE\_NOTIFY\_INFORMATION
