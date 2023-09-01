### DirectoryObjectHandle

Handle to Directory Object opened with `DIRECTORY_QUERY` access.

### DirObjInformation

Pointer to `OBJDIR_INFORMATION` structure. Warning: structure has variable length depending on length of object name. \
To test for required length of buffer use `DataWritten` parameter.

### BufferLength

Length of `DirObjInformation` buffer.

### GetNextIndex

Decide of `ObjectIndex` parameter usage on output. \
  **If FALSE:** `ObjectIndex` is number of object in Object Directory. \
  **If TRUE:** `ObjectIndex` is index of next object to queried object (see below) in Object Directory.

### IgnoreInputIndex

Decide how to use `ObjectIndex` on function input. \
  **If FALSE:** `ObjectIndex` point to `ULONG` index of object in Object Directory. \
  **If TRUE:** `ObjectIndex` input value is ignored. Function always return information about first object in Object Directory.

### ObjectIndex

Pointer to `ULONG` value described above.

### DataWritten

Pointer to `ULONG` value receiving required / written buffer size. This parameter is optional.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateDirectoryObject`
* `NtOpenDirectoryObject`
* `OBJDIR_INFORMATION`
