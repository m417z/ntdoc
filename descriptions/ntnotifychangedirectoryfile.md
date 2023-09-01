`NtNotifyChangeDirectoryFile` is used to process changes to directory File Object. Because function returns immediately with `STATUS_PENDING`, you must decide to use Event Object or *APC* routine as notification form.

### FileHandle

`HANDLE` to File Object opened with `SYNCHRONIZE` access and `FILE_DIRECTORY_FILE` option set.

### Event

`HANDLE` to Event Object. Event can be created as `NotificationEvent` or `SynchronizationEvent`, but second one is better in this situation.

### ApcRoutine

Address of user's *APC* routine, queued when change complete.

### ApcContext

Optional parameter for `ApcRoutine`.

### IoStatusBlock

IO result of call. **Status** member in `IoStatusBlock` can result `STATUS_NOTIFY_ENUM_DIR` when `Buffer` was to small.

### Buffer

User's allocated buffer for change information. It contains one or more of `FILE_NOTIFY_INFORMATION` structures.

### BufferSize

Size of `Buffer`, in bytes.

### CompletionFilter

Mask specifying what sort of changes should be monitored. Can be combination of:

* `FILE_NOTIFY_CHANGE_FILE_NAME`
* `FILE_NOTIFY_CHANGE_DIR_NAME`
* `FILE_NOTIFY_CHANGE_NAME`
* `FILE_NOTIFY_CHANGE_ATTRIBUTES`
* `FILE_NOTIFY_CHANGE_SIZE`
* `FILE_NOTIFY_CHANGE_LAST_WRITE`
* `FILE_NOTIFY_CHANGE_LAST_ACCESS`
* `FILE_NOTIFY_CHANGE_CREATION`
* `FILE_NOTIFY_CHANGE_EA`
* `FILE_NOTIFY_CHANGE_SECURITY`
* `FILE_NOTIFY_CHANGE_STREAM_NAME`
* `FILE_NOTIFY_CHANGE_STREAM_SIZE`
* `FILE_NOTIFY_CHANGE_STREAM_WRITE`

### WatchTree

If set, all subdirectiories of specified directory will be also monitored.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `EVENT_TYPE`
* `FILE_NOTIFY_INFORMATION`
