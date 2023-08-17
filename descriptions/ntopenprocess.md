This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ntopenprocess) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwopenprocess).

---

### AccessMask

* PROCESS_TERMINATE

* PROCESS_CREATE_THREAD
* PROCESS_SET_SESSIONID

* PROCESS_VM_OPERATION
* PROCESS_VM_READ

* PROCESS_VM_WRITE
* PROCESS_DUP_HANDLE

* PROCESS_CREATE_PROCESS
* PROCESS_SET_QUOTA

* PROCESS_SET_INFORMATION
* PROCESS_QUERY_INFORMATION

* PROCESS_ALL_ACCESS

### ObjectAttributes

For standard processes, all fields of `ObjectAttributes` should be *NULL*.

### ClientId

Process id and thread id must be fill with valid values.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateProcess`
* `NtTerminateProcess`
