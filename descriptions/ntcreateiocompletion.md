Function `NtCreateIoCompletion` creates IO Completion Object. IO Completion Object is used for waiting on pending IO operation (reading or writing) in multi-process file access. It contains more informations about IO operation than synchronization event or *APC Routine*.

### IoCompletionHandle

Result of call - `HANDLE` to newly created IO Completion Object.

### DesiredAccess

Access mask for created `HANDLE`. Can be combination of:

* `IO_COMPLETION_QUERY_STATE`

* `IO_COMPLETION_MODIFY_STATE`
* `IO_COMPLETION_ALL_ACCESS`

### ObjectAttributes

Optionally contains object name, in Objects Namespace.

### NumberOfConcurrentThreads

Number of threads accessing File Object associated with IO Completion. If Zero, system reserves memory for number of threads equal to current nymber of processes.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `FILE_INFORMATION_CLASS`
* `NtOpenIoCompletion`
* `NtQueryIoCompletion`
* `NtRemoveIoCompletion`
* `NtSetInformationFile`
* `NtSetIoCompletion`
