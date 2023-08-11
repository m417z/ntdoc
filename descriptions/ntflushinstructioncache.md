Function NtFlushInstructionCache empties execution \
cache for specified region of code. It shoult be used always after \
modification of process's executable memory \(for example when \
NtLdr fills imported function's entries\). \
ProcessHandle HANDLE to Process \
Object. \
BaseAddress Starting memory address to \
flush. \
NumberOfBytesToFlush Length of flushed \
memory block.

Documented by: \
Reactos \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtOpenProcess
