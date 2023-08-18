Function NtCreateDebugObject is used for Debug Object creation. Debug Object
it's a new functionality implemented in Windows XP and above as support for
debugging User Mode applications. In previous versions of NT debugging was
implemented with Port objects (see NtCreatePort). Application can debug one or
few different applications in the same time, but need to create as many Debug
Objects as number of debugged processes.

There're two methods of start debugging. To start application in debug mode,
user need to use NtCreateProcessEx function (available on XP+) with HANDLE to
previously created Debug Object. Or just attach debugger to working process by
calling NtDebugActiveProcess.

### DebugObjectHandle

Pointer to newly created Debug Object HANDLE.

### DesiredAccess

Access mask for Debug Object. Can be one or more of following:

* `DEBUGOBJECT_WAIT_STATE_CHANGE`
* `DEBUGOBJECT_ADD_REMOVE_PROCESS`
* `DEBUGOBJECT_ALL_ACCESS`

### ObjectAttributes

Optionally can define object's name.

### KillProcessOnExit

If set, debugged process will be terminated with closing Debug Object.

# Documented by

* Tomasz Nowak

# See also

* `DBG_STATE`
* `NtCreateProcessEx`
* `NtDebugActiveProcess`
