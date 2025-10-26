# RtlDosPathNameToNtPathName_U

## Description

The **RtlDosPathNameToNtPathName_U** routine converts DosPathName to NtPathName by prepending these prefixes depending on the type of the path

* **NtPrefix**: `\??\` **(C:\\Users\\Sample -> \\??\\C:\\Users\\Sample)**
* **UncPrefix:** `\??\UNC\` **(\\\\server\\share\\path -> \\??\\UNC\\server\\share\\path)**

## Parameters

### `DosFileName` [IN]

A DOS-style file path/UNC Path that will be converted into NT Path.

If **DosFileName** only contains file component, it resolves it by using the process's current directory `(NtCurrentPeb()->ProcessParameters->CurrentDirectory)`

If **DosFileName** contains drive relative path **(e.g. C:Sample.txt)**, it retrieves the drive's current directory, combining it with the file component then prepend the **NtPrefix**. 

**(Note: If there's no file component, it simply prepends the NtPrefix to the current directory of the drive and then copies it into the `NtFileName->Buffer`)**

### `NtFileName` [OUT]

A pointer to a `UNICODE_STRING` where it receives the converted **DosFileName**

### `FilePart` [OUTOPT]

A string where if there's a file component on the Absolute Path of the **DosFileName**, this parameter receives the string of the file component **(e.g. Sample.txt)**.

If there's no file component, it uses the last folder as its file component **(e.g. C:\Sample -> "Sample")**.

### `RelativeName` [OUTOPT]

**(Only for Relative Path)** A pointer to an `RTL_RELATIVE_NAME_U` where additional info for Relative Path is stored.

## Return
Returns **TRUE** if successfully converted to an NT Path. **FALSE** otherwise

# See Also
- `RtlDosPathNameToNtPathName_U_WithStatus`
- `RtlDosPathNameToRelativeNtPathName_U`
- `RtlDosPathNameToRelativeNtPathName_U_WithStatus`




