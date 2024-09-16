This flags indicates the absence of other APC flags. The behavior defaults to regular APCs that require the thread to first enter an alertable wait via `NtDelayExecution` (or a similar function) or call `NtTestAlert`.

# Applicable to
 - `NtQueueApcThreadEx2`

# Related flags
 - `QUEUE_USER_APC_FLAGS_SPECIAL_USER_APC`
 - `QUEUE_USER_APC_FLAGS_CALLBACK_DATA_CONTEXT`

# Required OS version
This flag was introduced in Windows 11.
