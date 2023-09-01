This function is [documented in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntquerymultiplevaluekey).

---

Function `NtQueryMultipleValueKey` returns data of one or more values under specified Key Object.

### KeyHandle

`HANDLE` to Key Object opened with `KEY_READ` access.

### ValuesList

Array of `KEY_MULTIPLE_VALUE_INFORMATION` structures contains names of values to query.

### NumberOfValues

Number of members in `ValueList` array.

### DataBuffer

User's allocated buffer receiving queried value's data.

### BufferLength

Pointer to value specifying length of `DataBuffer`, in bytes.

### RequiredLength

Optionally pointer to value receiving required `DataBuffer` length, in bytes.

# Documented by

* Tomasz Nowak

# See also

* `KEY_MULTIPLE_VALUE_INFORMATION`
* `NtCreateKey`
* `NtEnumerateValueKey`
* `NtOpenKey`
* `NtQueryValueKey`
