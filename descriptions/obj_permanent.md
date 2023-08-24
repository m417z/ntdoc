This `OBJECT_ATTRIBUTES` flag indicates that the object should be marked as permanent. This flag alters the lifetime of the object, making it independent from reference counting. Creating or marking objects as permanent requires `SeCreatePermanentPrivilege`. To delete such object, make it temporary first via `NtMakeTemporaryObject`.

# Related flags
 - `OBJ_PROTECT_CLOSE`
 - `OBJ_INHERIT`
 - `OBJ_AUDIT_OBJECT_CLOSE`
 - `OBJ_NO_RIGHTS_UPGRADE`
 - `OBJ_EXCLUSIVE`
 - `OBJ_CASE_INSENSITIVE`
 - `OBJ_OPENIF`
 - `OBJ_OPENLINK`
 - `OBJ_KERNEL_HANDLE`
 - `OBJ_FORCE_ACCESS_CHECK`
 - `OBJ_IGNORE_IMPERSONATED_DEVICEMAP`
 - `OBJ_DONT_REPARSE`

# Remarks
To make an existing object permanent, use `NtMakePermanentObject`.

# See also
 - `OBJECT_ATTRIBUTES`
 - `NtMakePermanentObject`
 - `NtMakeTemporaryObject`
 - `NtQueryObject`
 - `OBJECT_BASIC_INFORMATION`
