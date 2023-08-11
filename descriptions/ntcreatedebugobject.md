Function NtCreateDebugObject is used for Debug \
Object creation. Debug Object it's a new \
functionality implemented in Windows XP and above as support \
for debuging User Mode applications. In previous versions of \
NT debuging was implemented with Port objects \(see \
NtCreatePort\). Application can debug one or few different \
applications in the same time, but need to create as many \
Debug Objects as number of debuged processes. \
There're two methods of start debugging. To start application in \
debug mode, user need to use NtCreateProcessEx function \(avaiable \
on XP\+\) with HANDLE to previously created Debug \
Object. Or just attach debugger to working process by \
calling \
NtDebugActiveProcess. \
DebugObjectHandle Pointer to newly \
created Debug Object HANDLE. \
DesiredAccess Access mask for Debug \
Object. Can be one or more of following: \
DEBUGOBJECT\_WAIT\_STATE\_CHANGE \
DEBUGOBJECT\_ADD\_REMOVE\_PROCESS \
DEBUGOBJECT\_ALL\_ACCESS \
ObjectAttributes Optionally can define \
object's name. \
KillProcessOnExit If set, debuged \
process will be terminated with closing Debug \
Object. \
Supported on system versions: \
Win XP/2003

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
DBG\_STATE \
NtCreateProcessEx \
NtDebugActiveProcess
