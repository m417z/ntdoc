Function `NtQueryIoCompletion` receives number of file operations pending on specified IO Completion Object.

### IoCompletionHandle

`HANDLE` to IO Completion Object opened with `IO_COMPLETION_QUERY_STATE` access.

### InformationClass

See `IO_COMPLETION_INFORMATION_CLASS` for possible values.

### IoCompletionInformation

User's allocated buffer for result data.

### InformationBufferLength

Length of `IoCompletionInformation` buffer, in bytes.

### RequiredLength

Optionally receives required length of buffer.

# Documented by

* Tomasz Nowak

# See also

* `IO_COMPLETION_INFORMATION_CLASS`
* `NtCreateIoCompletion`
* `NtOpenIoCompletion`
* `NtRemoveIoCompletion`
* `NtSetIoCompletion`
