This function is [documented in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/devnotes/ntremoveiocompletion).

---

Function `NtRemoveIoCompletion` is one of waiting calls and it's finished when at least one completion record will be available in specified *Io Completion* object. Records are added when I/O operation is finished, but previously *File* object have to been associated with *Io Completion* object. \
Association between *File* and *Io Completion* objects is added by call to `NtSetInformationFile` \
with `FileCompletionInformation` information class. Additionally every association have to have unique `Key` defined. This functionality allows to use one *Io Completion* object with different *File* objects. \
Every one *File* object can have only one *Io Completion* associated with it.

I/O operations won't be appended to *Io Completion* object except file operations will be called with non-zero value in `ApcContext` parameters.

### IoCompletionHandle

`HANDLE` to previously created or opened *Io Completion* object.

### CompletionKey

Receives completion `Key` informing about *File* object who finishes I/O.

### CompletionValue

Value of `ApcContext` file operation parameter. `CompletionValue` informs about operation finished.

### IoStatusBlock

Io status of finished operation.

### Timeout

Optionally pointer to time out value.

# Documented by

* Tomasz Nowak

# See also

* `FILE_COMPLETION_INFORMATION`
* `FILE_INFORMATION_CLASS`
* `NtCreateIoCompletion`
* `NtOpenIoCompletion`
* `NtReadFile`
* `NtSetInformationFile`
* `NtSetIoCompletion`
* `NtWriteFile`
