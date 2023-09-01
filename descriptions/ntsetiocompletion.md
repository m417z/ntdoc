Function `NtSetIoCompletion` increments pending IO counter in IO Completion Object. It can be used to manual finish IO operation.

### IoCompletionHandle

`HANDLE` to IO Completion Object opened with `IO_COMPLETION_MODIFY_STATE` access.

### CompletionKey

User's defined key received by `NtRemoveIoCompletion` function.

### IoStatusBlock

IO result of call.

### CompletionStatus

IO operation status.

### NumberOfBytesTransferred

Number of bytes transferred in manually finished IO operation.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateIoCompletion`
* `NtOpenIoCompletion`
* `NtQueryIoCompletion`
* `NtRemoveIoCompletion`
