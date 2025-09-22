This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatefile).

---

*(Available also in 2000 DDK.)*

### FileHandle

Result of call - `HANDLE` to File Object.

### DesiredAccess

Access mask based on definitions in schema `FILE_*` from **\<WinNT.h\>**.

### ObjectAttributes

Name of file to create (or open), optionally path in name string. You can also define root directory, security descriptor and attributes `OBJ_CASE_INSENSITIVE` and `OBJ_INHERIT`.

### IoStatusBlock

Pointer to `IO_STATUS_BLOCK` structure, that receive final status of function call. Can be one of:

* `FILE_CREATED`
* `FILE_OPENED`
* `FILE_OVERWRITTEN`
* `FILE_SUPERSEDED`
* `FILE_EXISTS`
* `FILE_DOES_NOT_EXIST`

### AllocationSize

File size after creation.

### FileAttributes

Attributes for newly created file, as follows:

* `FILE_ATTRIBUTE_READONLY`
* `FILE_ATTRIBUTE_HIDDEN`
* `FILE_ATTRIBUTE_SYSTEM`
* `FILE_ATTRIBUTE_ARCHIVE`
* `FILE_ATTRIBUTE_NORMAL`
* `FILE_ATTRIBUTE_TEMPORARY`
* `FILE_ATTRIBUTE_OFFLINE`
* `FILE_ATTRIBUTE_NOT_CONTENT_INDEXED`

### ShareAccess

Specifies share method for opened object. Can be set to zero or any combination of flags:

* `FILE_SHARE_READ`
* `FILE_SHARE_WRITE`
* `FILE_SHARE_DELETE`

### CreateDisposition

Specifies disposition how to create or open object and can be one of:

* `FILE_SUPERSEDE` - If file exists, deletes it before creation of new one.
* `FILE_OPEN` - Fails, if file not exists.
* `FILE_CREATE` - Fails, if file exists.
* `FILE_OPEN_IF` - If file exists, opens it. If not, creates new one and then open it.
* `FILE_OVERWRITE` - If file not exists, create and open it. If exists, open them and reset content.
* `FILE_OVERWRITE_IF` - As `FILE_OVERWRITE`, but fails if file not exists.

### CreateOptions

Creation options.

### EaBuffer

Buffer for Extended Attributes contains one or more of `FILE_FULL_EA_INFORMATION` structures.

### EaLength

Length of `EaBuffer`.

# Related Win32 API
 - [`CreateFileA`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilea)
 - [`CreateFileW`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew)

# Documented by

* Tomasz Nowak

# See also

* `FILE_FULL_EA_INFORMATION`
* `NtDeleteFile`
* `NtOpenFile`
* `NtSetEaFile`
