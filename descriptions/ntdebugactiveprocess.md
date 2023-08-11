Function NtDebugActiveProcess is used to attach \
Debug Object to any non\-debuged process. \
ProcessHandle HANDLE to process \
being debugged \(opened with enough access rigths \- see \
NtOpenProcess\). \
DebugObjectHandle HANDLE to \
previously created Debug Object. \
Supported on system versions: \
Win XP/2003

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateDebugObject \
NtOpenProcess \
NtRemoveProcessDebug
