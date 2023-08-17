This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryobject) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryobject).

---

Function `NtQueryObject` retrives some informations about any or all objects opened by calling process. It can be used with any type of object.

### ObjectHandle

HANDLE to object.

### ObjectInformationClass

Kind of information to retrive. See `OBJECT_INFORMATION_CLASS` for possible values list.

### ObjectInformation

Output buffer allocated by caller.

### Length

Length of `ObjectInformation` buffer, in bytes.

### ResultLength

Pointer to `ULONG` value that contains required size of `ObjectInformation` buffer after function call.

# Documented by

* Tomasz Nowak

# See also

* `NtSetInformationObject`
* `OBJECT_INFORMATION_CLASS`
