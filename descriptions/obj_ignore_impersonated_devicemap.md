This `OBJECT_ATTRIBUTES` flag indicates that the open/create operation should ignore the DOS Devices map from the logon session of the impersonated token.

# Related flags
 - `OBJ_PROTECT_CLOSE`
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
 - `OBJ_DONT_REPARSE`

# See also
 - `OBJECT_ATTRIBUTES`
 - `NtOpenThreadToken`
 - `NtSetInformationThread` with `THREADINFOCLASS` value of `ThreadImpersonationToken` (5)
 - `NtSetInformationProcess` with `PROCESSINFOCLASS` value of `ProcessDeviceMap` (23)
