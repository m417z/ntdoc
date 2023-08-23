This flags indicates that the callback routine should receive the context (set of registers) that was interrupted when the thread was directed to call the APC function. The the documentation for [the corresponding Win32 flags](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/ne-processthreadsapi-queue_user_apc_flags) for more details.

# Applicable to
 - `NtQueueApcThreadEx2`

# Related flags
 - `QUEUE_USER_APC_FLAGS_NONE`
 - `QUEUE_USER_APC_FLAGS_SPECIAL_USER_APC`

# Required OS version
This flag was introduced in Windows 11.
