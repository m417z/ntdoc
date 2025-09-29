### ObjectHandle

Open handle to any NT object.

### ObjectInformationClass

See `NtQueryObject` for detailed description of possible information classes.

### ObjectInformation

Buffer with data to set.

### Length

Length of `ObjectInformation` buffer, in bytes.

---

Currently only one class in allowed in set mode: `ObjectDataInformation`. See description of `OBJECT_DATA_INFORMATION` structure.

# Documented by

* Tomasz Nowak

# See also

* `NtQueryObject`
* `OBJECT_DATA_INFORMATION`
