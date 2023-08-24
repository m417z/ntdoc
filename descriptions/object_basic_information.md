Basic kernel handle/object information, common to all object types.

# Applicable to
 - `NtQueryObject` with `ObjectBasicInformation`.

# Members

## Attributes
A bit mask containing attributes of the handle/object:

 - `OBJ_PROTECT_CLOSE` - the handle is protected from closing.
 - `OBJ_INHERIT` - the handle is inheritable.
 - `OBJ_PERMANENT` - object has permanent lifetime.
 - `OBJ_EXCLUSIVE` - the handle/object is exclusive and prevents other handles from being open to the object.

## GrantedAccess
The access mask granted on the handle.

## HandleCount
The number of handles pointing to the object.

## PointerCount
The number of pointers to the object.

## PagedPoolCharge
The number of paged pool bytes charged for the object.

## NonPagedPoolCharge
The number of non-paged pool bytes charged for the object.

## Reserved[3]
Unused field.

## NameInfoSize
The number of bytes required to query object name information.

### See also
 - `NtQueryObject` with `ObjectNameInformation`.

## TypeInfoSize
The number of bytes required to query object type information.

### See also
 - `NtQueryObject` with `ObjectTypeInformation`.

## SecurityDescriptorSize
The number of bytes required to query the security descriptor of the object. Note that the system populates this field only when the handle grants `READ_CONTROL` access.

### See also
 - `NtQuerySecurityObject`

## CreationTime
The time of creation for symbolic link objects.

### See also
 - `NtCreateSymbolicLinkObject`
