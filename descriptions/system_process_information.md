Structure SYSTEM\_PROCESS\_INFORMATION contains list of \
processes and threads and it's avaiable via \
NtQuerySystemInformation function with SystemProcessInformation \
information class. \
NextEntryOffset Offset from begining of \
output buffer to next process entry. On last entry contains \
zero. \
NumberOfThreads Number of process'es \
threads. Also number of members in Threads array descripted below. \
Reserved\[3\] Reserved. \
CreateTime Process creation time, in \
100\-ns units. \
UserTime Effective time in User \
Mode. \
KernelTime Effective time in Kernel \
Mode. \
ImageName Process name, based on \
executable file name. \
BasePriority Process base \
priority. \
ProcessId Unique identifier of \
process. \
InheritedFromProcessId Creator's \
identifier. \
HandleCount Nr of open \
HANDLEs. \
Reserved2\[2\] Reserved. \
PrivatePageCount Number of memory pages \
assigned to process. \
VirtualMemoryCounters Memory \
performance counters. \
IoCounters IO performance \
counters. \
Threads\[0\] Array of \
SYSTEM\_THREAD structures descripting process's threads.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtQuerySystemInformation \
SYSTEM\_INFORMATION\_CLASS \
SYSTEM\_THREAD
