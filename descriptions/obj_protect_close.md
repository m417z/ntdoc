This `OBJECT_ATTRIBUTES` flag indicates that the handle should be protected from closing. Passing such handle to `NtClose` returns an error; trying to close it via `NtDuplicateObject` has no effect.

# Related flags
 - `OBJ_INHERIT`
 - `OBJ_AUDIT_OBJECT_CLOSE`
 - `OBJ_NO_RIGHTS_UPGRADE`
 - `OBJ_PERMANENT`
 - `OBJ_EXCLUSIVE`
 - `OBJ_CASE_INSENSITIVE`
 - `OBJ_OPENIF`
 - `OBJ_OPENLINK`
 - `OBJ_KERNEL_HANDLE`
 - `OBJ_FORCE_ACCESS_CHECK`
 - `OBJ_IGNORE_IMPERSONATED_DEVICEMAP`
 - `OBJ_DONT_REPARSE`

# See also
 - `OBJECT_ATTRIBUTES`
 - `NtQueryObject`
 - `NtSetInformationObject`
 - `OBJECT_HANDLE_FLAG_INFORMATION`
 - `OBJECT_BASIC_INFORMATION`
