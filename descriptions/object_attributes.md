Describes the name and other attributes of an object for open or creation operations. This structure is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows/win32/api/ntdef/ns-ntdef-_object_attributes). Use `InitializeObjectAttributes` to initialize this structure.

# Members
 - `Length` - the size of the structure; set it to `sizeof(OBJECT_ATTRIBUTES)`.
 - `RootDirectory` - an optional handle to an object relative to which the system should interpret the `ObjectName` field.
 - `ObjectName` - the absolute native name of the object when the `RootDirectory` field is `NULL` or a relative name otherwise. Set this value to `NULL` for unnamed objects.
 - `Attributes` - a set of bit flags described below.
 - `SecurityDescriptor` - an optional pointer to a security descriptor to protect the object with during creation.
 - `SecurityQualityOfService` - an optional pointer to a QoS structure that defines impersonation-related information.

# Known attribute values
 - `OBJ_PROTECT_CLOSE` - the handle is protected from closing.
 - `OBJ_INHERIT` - the handle is inheritable.
 - `OBJ_AUDIT_OBJECT_CLOSE`
 - `OBJ_NO_RIGHTS_UPGRADE` - prevents upgrading rights when duplicating the handle.
 - `OBJ_PERMANENT` - alters the lifetime management rules for the object, making it permanent.
 - `OBJ_EXCLUSIVE` - allow only one handle to the object.
 - `OBJ_CASE_INSENSITIVE` - treat the name of the object as case-insensitive.
 - `OBJ_OPENIF` - open the existing object instead of failing to create one on name collision.
 - `OBJ_OPENLINK` - open the reparse point instead of following it.
 - `OBJ_KERNEL_HANDLE` - make a kernel handle.
 - `OBJ_FORCE_ACCESS_CHECK` - force performing an access check even for kernel callers.
 - `OBJ_IGNORE_IMPERSONATED_DEVICEMAP` - ignore device map from the impersonated token.
 - `OBJ_DONT_REPARSE` - fail on encountering reparse points.
 - `OBJ_KERNEL_EXCLUSIVE`

See the corresponding pages for details.

# Remarks
Native API uses a different format of paths from the Win32 API. The root of the NT object namespace is the `\` directory. For more details about the relationship between Native and Win32 filenames, see this [blog post](https://googleprojectzero.blogspot.com/2016/02/the-definitive-guide-on-win32-to-nt.html).

# See also
 - `InitializeObjectAttributes`
