`OBJECT_INFORMATION_CLASS` specifies a kind of information of any object available in caller context. It's used with functions `NtQueryObject` and `NtSetInformationObject`.

### ObjectBasicInformation

* Action: `Query`
* Buffer size: *0x038*
* Structure: `OBJECT_BASIC_INFORMATION`

### ObjectNameInformation

* Action: `Query`
* Buffer size: *0x08*
* Structure: `OBJECT_NAME_INFORMATION`

### ObjectTypeInformation

* Action: `Query`
* Buffer size: *0x070*
* Structure: `OBJECT_TYPE_INFORMATION`

### ObjectAllInformation

* Action: `Query`
* Buffer size: *0x04+*
* Structure: `OBJECT_ALL_INFORMATION`
* Comment: Size of buffer depends on number of objects opened by caller.

### ObjectDataInformation

* Action: `Query, Set`
* Buffer size: *0x02*
* Structure: `OBJECT_DATA_INFORMATION`

# Documented by

* Tomasz Nowak

# See also

* `NtQueryObject`
* `NtSetInformationObject`
