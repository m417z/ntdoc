Function `NtQuerySemaphore` retrieve semaphore's parameters (see `SEMAPHORE_BASIC_INFORMATION`).

### SemaphoreHandle

`HANDLE` to Semaphore Object opened with `SEMAPHORE_QUERY_STATE` access.

### SemaphoreInformationClass

Information class descripted in `SEMAPHORE_INFORMATION_CLASS` section.

### SemaphoreInformation

Pointer to user's allocated buffer for result data.

### SemaphoreInformationLength

Size of `SemaphoreInformation` buffer, in bytes.

### ReturnLength

Optionally returns required buffer size.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateSemaphore`
* `NtOpenSemaphore`
* `SEMAPHORE_BASIC_INFORMATION`
* `SEMAPHORE_INFORMATION_CLASS`
