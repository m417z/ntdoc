This `OBJECT_ATTRIBUTES` flag indicates that the handle should be inheritable. Whether the child processes actually inherit this handle depends on the flags used during process creation and some other attributes of the object.

# Related flags
 - `OBJ_PROTECT_CLOSE`
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
 - `NtCreateProcess`
 - `NtCreateProcessEx`
 - `NtCreateUserProcess`
