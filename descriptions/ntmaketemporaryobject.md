Removes the permanent flag from the object, restoring its lifetime to be dependant on the number of handles. This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwmaketemporaryobject).

# Parameters
 - `Handle` - a handle to a kernel object. The handle must grant `DELETE` access.

# Remarks
This function undoes the effects of `NtMakePermanentObject` and specifying `OBJ_PERMANENT` in `OBJECT_ATTRIBUTES`.

# See also
 - `NtMakePermanentObject`
 - `OBJ_PERMANENT`
 - `OBJECT_BASIC_INFORMATION`
 - `NtQueryObject`
