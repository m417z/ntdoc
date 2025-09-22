This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatedirectoryobject).

---

### DirectoryHandle

Pointer to newly created Directory Object after function call.

### DesiredAccess

As defined in \<ntddk.h\> can be one of following:

```cpp
#define DIRECTORY_QUERY                 (0x0001)
#define DIRECTORY_TRAVERSE              (0x0002)
#define DIRECTORY_CREATE_OBJECT         (0x0004)
#define DIRECTORY_CREATE_SUBDIRECTORY   (0x0008)
#define DIRECTORY_ALL_ACCESS (STANDARD_RIGHTS_REQUIRED | 0xF)
```

### ObjectAttributes

Pointer to object attributes. Structure must contain valid object name.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `NtOpenDirectoryObject`
* `NtQueryDirectoryObject`
