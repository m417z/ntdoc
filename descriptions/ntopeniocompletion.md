Function `NtOpenIoCompletion` opens existing IO Completion Object. IO Completion must be created as named object.

### IoCompletionHandle

Result of call - pointer to `HANDLE` value.

### DesiredAccess

Can be one or combination of:

* `IO_COMPLETION_QUERY_STATE`

* `IO_COMPLETION_MODIFY_STATE`
* `IO_COMPLETION_ALL_ACCESS`

### ObjectAttributes

Pointer to `OBJECT_ATTRIBUTES` structure containing valid IO Completion name.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `NtCreateIoCompletion`
