Function `NtCreateNamedPipeFile` creates *Named Pipe* File Object. Named Pipes are especial kind of files, so all functionality is provided with file's functions like `NtReadFile`, `NtWriteFile` etc. \
Named Pipes are frequently used in NT system, for example as **stdin** and **stdout** handles.

### NamedPipeFileHandle

Result of call - pointer to `HANDLE` to Named Pipe.

### DesiredAccess

Access rights for object's handle. Can be one or combination of:

* `FILE_READ_DATA`

* `FILE_WRITE_DATA`
* `FILE_CREATE_PIPE_INSTANCE`

* `FILE_READ_ATTRIBUTES`
* `FILE_WRITE_ATTRIBUTES`

* `SYNCHRONIZE`
* `READ_CONTROL`

* `WRITE_OWNER`
* `WRITE_DAC`

* `ACCESS_SYSTEM_SECURITY`
Also combination of Generic rights are supported.

### ObjectAttributes

Pointer to `OBJECT_ATTRIBUTES` structure contains name of named pipe. Name must begin with **"/??/PIPE/"** string, that is Symbolic Link to *NamedPipe* device object.

### IoStatusBlock

IO result of call.

### ShareAccess

Can be combination of following:

* `FILE_SHARE_READ`

* `FILE_SHARE_WRITE`
* `FILE_SHARE_DELETE`

### CreateDisposition

Use `FILE_CREATE`, `FILE_OPEN` or `FILE_OPEN_IF`.

### CreateOptions

See description of `NtCreateFile` for possible creation flags.

### WriteModeMessage

If set, writing to created pipe are processed in *Message Mode*. If not, all writes are in *Byte Mode*.

### ReadModeMessage

The same functionality as `WriteModeMessage` parameter, but for reading data.

### NonBlocking

If set, all operations on created pipe are asynchronous.

### MaxInstances

Maximum number of open handles for Named Pipe, or `FILE_PIPE_UNLIMITED_INSTANCES` constant.

### InBufferSize

Input buffer size, in bytes.

### OutBufferSize

Output buffer size, in bytes.

### DefaultTimeOut

Pointer to `LARGE_INTEGER` value specifing pipe's time out, in *100-ns* units. Negative value means relative time.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `FILE_INFORMATION_CLASS`
* `FILE_PIPE_INFORMATION`
* `FILE_PIPE_LOCAL_INFORMATION`
* `FILE_PIPE_REMOTE_INFORMATION`
* `NtFsControlFile`
* `NtQueryInformationFile`
* `NtReadFile`
* `NtSetInformationFile`
* `NtWriteFile`
