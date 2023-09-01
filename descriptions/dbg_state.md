`DBG_STATE` enumeration is used by **Debug Objects** as a member of `DBGUI_WAIT_STATE_CHANGE` structure returned in successful call to `NtWaitForDebugEvent` function. It describes current state of **Debug Object**. Possible values are:

### DbgIdle

### DbgReplyPending

### DbgCreateThreadStateChange

### DbgCreateProcessStateChange

### DbgExitThreadStateChange

### DbgExitProcessStateChange

### DbgExceptionStateChange

### DbgBreakpointStateChange

### DbgSingleStepStateChange

### DbgLoadDllStateChange

### DbgUnloadDllStateChange

# Documented by

* ReactOS
* Tomasz Nowak

# See also

* `DBGUI_WAIT_STATE_CHANGE`
* `NtWaitForDebugObject`
