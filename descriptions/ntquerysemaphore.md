Function NtQuerySemaphore retrieve semaphore's \
    parameters \(see \
    SEMAPHORE\_BASIC\_INFORMATION\). \
    SemaphoreHandle HANDLE to \
    Semaphore Object opened with SEMAPHORE\_QUERY\_STATE \
    access. \
    SemaphoreInformationClass Information \
    class descripted in \
    SEMAPHORE\_INFORMATION\_CLASS section. \
    SemaphoreInformation Pointer to user's \
    allocated buffer for result data. \
    SemaphoreInformationLength Size of \
    SemaphoreInformation buffer, in \
    bytes. \
    ReturnLength Optionally returns \
    required buffer size. \
Documented by: \
    Tomasz Nowak \
    Requirements: \
Library: ntdll.lib \
See also: \
    NtCreateSemaphore \
    NtOpenSemaphore \
    SEMAPHORE\_BASIC\_INFORMATION \
    SEMAPHORE\_INFORMATION\_CLASS
