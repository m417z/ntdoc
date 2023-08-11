Structure PEB \(Process Enviroment Block\) \
contains all User\-Mode parameters associated by system with \
current process. \
InheritedAddressSpace \
ReadImageFileExecOptions \
BeingDebugged \
Spare \
Mutant \
ImageBaseAddress Address of executable \
image in process' memory. \
LoaderData Pointer to PEB\_LDR\_DATA structure \
contains information filled by Loader. \
ProcessParameters Pointer to RTL\_USER\_PROCESS\_PARAMETERS \
structure. \
SubSystemData \
ProcessHeap Address of process' first \
heap allocated by Loader. \
FastPebLock Parameter for \
PEBLOCKROUTINE \(see below\). \
FastPebLockRoutine Address of \
fast\-locking routine for PEB. Definition of routine \
is: \
typedef void \
\(\*PPEBLOCKROUTINE\)\( \
PVOID PebLock \
\); \
FastPebUnlockRoutine PEB \
fast\-unlock routine. \
EnvironmentUpdateCount Counter of \
process environment updates. \
KernelCallbackTable \
EventLogSection \
EventLog \
FreeList \
TlsExpansionCounter \
TlsBitmap \
TlsBitmapBits\[0x2\] \
ReadOnlySharedMemoryBase \
ReadOnlySharedMemoryHeap \
ReadOnlyStaticServerData \
AnsiCodePageData \
OemCodePageData \
UnicodeCaseTableData \
NumberOfProcessors \
NtGlobalFlag \
Spare2\[0x4\] \
CriticalSectionTimeout \
HeapSegmentReserve \
HeapSegmentCommit \
HeapDeCommitTotalFreeThreshold \
HeapDeCommitFreeBlockThreshold \
NumberOfHeaps \
MaximumNumberOfHeaps \
\*ProcessHeaps \
GdiSharedHandleTable \
ProcessStarterHelper \
GdiDCAttributeList \
LoaderLock \
OSMajorVersion \
OSMinorVersion \
OSBuildNumber \
OSPlatformId \
ImageSubSystem \
ImageSubSystemMajorVersion \
ImageSubSystemMinorVersion \
GdiHandleBuffer\[0x22\] \
PostProcessInitRoutine \
TlsExpansionBitmap \
TlsExpansionBitmapBits\[0x80\] \
SessionId

Documented by: \
Reactos \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtQueryInformationProcess \
PEB\_FREE\_BLOCK \
PEB\_LDR\_DATA \
PROCESS\_BASIC\_INFORMATION \
RTL\_USER\_PROCESS\_PARAMETERS \
TEB
