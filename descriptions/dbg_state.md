DBG\_STATE enumeration is used by Debug Objects \
as a member of DBGUI\_WAIT\_STATE\_CHANGE \
structure returned in successfull call to NtWaitForDebugEvent function. It \
describes current state of Debug Object. Possible values \
are: \
DbgIdle \
DbgReplyPending \
DbgCreateThreadStateChange \
DbgCreateProcessStateChange \
DbgExitThreadStateChange \
DbgExitProcessStateChange \
DbgExceptionStateChange \
DbgBreakpointStateChange \
DbgSingleStepStateChange \
DbgLoadDllStateChange \
DbgUnloadDllStateChange \
Supported on system versions: \
Win XP/2003

Documented by: \
Reactos \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
DBGUI\_WAIT\_STATE\_CHANGE \
NtWaitForDebugObject
