Function `NtImpersonateThread` assigns one thread's token to another. If source thread don't have associated Token Object, function use process'es token to impersonate destination thread.

### ThreadHandle

`HANDLE` to source Thread Object.

### ThreadToImpersonate

`HANDLE` to destination Thread Object opened with `THREAD_IMPERSONATE` access.

### SecurityQualityOfService

Pointer to `SECURITY_QUALITY_OF_SERVICE` structure filled by user.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `NtCreateThread`
* `NtImpersonateClientOfPort`
* `NtOpenThread`
* `SECURITY_QUALITY_OF_SERVICE`
