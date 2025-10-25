# RtlDosPathNameToNtPathName_U

## Description

The <b>RtlDosPathNameToNtPathName_U</b> routine converts DosPathName to NtPathName by prepending these prefixes depending on what type of path

* <b>NtPrefix</b>: `\??\` <b>(C:\\Users\\Sample -> \\??\\C:\\Users\\Sample)</b>
* <b>UncPrefix:</b> `\??\UNC\` <b>(\\\\server\\share\\path -> \\??\\UNC\\server\\share\\path)</b>

## Parameters

### -DosFileName [IN]

A DOS-style file path/UNC Path that will be converted into Nt-Style Path.

If <b>DosFileName</b> only contains file component, it resolves it by using the process's current directory `(NtCurrentPeb()->ProcessParameters->CurrentDirectory)`

If <b>DosFileName</b> contains drive relative path <b>(e.g. C:Sample.txt)</b>, it retrieves the drive's current directory, combining it with the file component then prepend the <b>NtPrefix</b>. 

<b>(Note: If there's no file component, it simply prepends the NtPrefix to the current directory of the drive and then copies it into the `NtFileName->Buffer`)</b>

### -NtFileName [OUT]

A pointer of `UNICODE_STRING` where it receives the converted <b>DosFileName</b>

### -FilePart [OUTOPT]

A string where if there's a file component on the Absolute Path of the <b>DosFileName</b>, this parameter receives the string of the file component <b>(e.g. Sample.txt)</b>.

If there's no file component, it uses the last folder as its file component <b>(e.g. C:\Sample -> "Sample")</b>

### -RelativeName [OUTOPT]

<b>(Only for Relative Path)</b> A pointer of `RTL_RELATIVE_NAME_U` where additional info for Relative Path are stored

## Return
Returns <b>TRUE</b>  if successfully converted into Nt-Style Path. <b>FALSE</b> otherwise

# See Also
<a href="https://ntdoc.m417z.com/rtldospathnametontpathname_u_withstatus">RtlDosPathNameToNtPathName_U_WithStatus</a>


<a href="https://ntdoc.m417z.com/rtldospathnametorelativentpathname_u">RtlDosPathNameToRelativeNtPathName_U</a>


<a href="https://ntdoc.m417z.com/rtldospathnametorelativentpathname_u_withstatus">RtlDosPathNameToRelativeNtPathName_U_WithStatus</a>