Marks an object as permanent, extending its lifetime past the last closed handle. Calling this function requires having `SeCreatePermanentPrivilege` enabled. To undo the operation, use `NtMakeTemporaryObject`.

# Parameters
 - `Handle` - a handle to a kernel object. The handle does not need to grant any specific access.

# Remarks
To make new objects have permanent state from their creation, include `OBJ_PERMANENT` in `OBJECT_ATTRIBUTES`.

# See also
 - `NtMakeTemporaryObject`
 - `OBJ_PERMANENT`
 - `OBJECT_BASIC_INFORMATION`
 - `NtQueryObject`
