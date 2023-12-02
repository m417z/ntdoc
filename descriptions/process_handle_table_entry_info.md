This structure defines information about a handle opened by the process.

# Applicable to
 - `PROCESS_HANDLE_SNAPSHOT_INFORMATION`

# Members

## HandleValue
The value of the handle.

## HandleCount
The number of handles pointing to the object.

## PointerCount
The number of pointers to the object.

## GrantedAccess
The access mask granted on the handle.

## ObjectTypeIndex
The index of this type in the global list of kernel types.

### See also
 - `NtQueryObject` with `OBJECT_INFORMATION_CLASS` value of `ObjectTypesInformation` (3).

## HandleAttributes
A bit mask containing attributes of the handle/object:

 - `OBJ_PROTECT_CLOSE` - the handle is protected from closing.
 - `OBJ_INHERIT` - the handle is inheritable.
 - `OBJ_PERMANENT` - object has permanent lifetime.
 - `OBJ_EXCLUSIVE` - the handle/object is exclusive and prevents other handles from being open to the object.

## Reserved
This field in unused.

# Required OS version
This structure was introduced in Windows 8.
