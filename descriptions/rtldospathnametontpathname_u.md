The `RtlDosPathNameToNtPathName_U` function converts a DOS path name to an NT path name by prepending the appropriate prefix based on the path type.

* NT prefix: `\??\` (for example, `C:\Users\Sample` to `\??\C:\Users\Sample`)
* UNC prefix: `\??\UNC\` (for example, `\\server\share\path` to `\??\UNC\server\share\path`)

# Parameters

## `DosFileName` [in]

A DOS-style file path or UNC path to convert to an NT path.

If `DosFileName` contains only a file component, the function resolves it by using the process's current directory (`NtCurrentPeb()->ProcessParameters->CurrentDirectory`).

If `DosFileName` contains a drive-relative path (for example, `C:Sample.txt`), the function retrieves the drive's current directory, combines it with the file component, and then prepends the NT prefix. 

Note: If there is no file component, the function prepends the NT prefix to the drive's current directory and copies it into `NtFileName->Buffer`.

## `NtFileName` [out]

A pointer to a `UNICODE_STRING` that receives the converted NT path.

## `FilePart` [out, optional]

A string that, if the absolute path in `DosFileName` includes a file component, receives the file component (for example, `Sample.txt`).

If there is no file component, the last folder is used as the file component (for example, `C:\Sample` to `Sample`).

## `RelativeName` [out, optional]

(Only for relative paths.) A pointer to an `RTL_RELATIVE_NAME_U` that stores additional information for a relative path.

# Return value
Returns `TRUE` if the conversion to an NT path succeeds; otherwise, `FALSE`.

# See also
- `RtlDosPathNameToNtPathName_U_WithStatus`
- `RtlDosPathNameToRelativeNtPathName_U`
- `RtlDosPathNameToRelativeNtPathName_U_WithStatus`
