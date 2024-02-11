This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeletefile).

---

It's very interesting NT System Call... Normally, file deletion is realised as `FileDispositionInformation` class in a call to `NtSetInformationFile`. When you use `NtDeleteFile`, file will be deleted immediately after call (system isn't waiting for close last `HANDLE` to file).

### ObjectAttributes

You can manipulate **ObjectName** and **RootDirectory** members. \
Example: \
  If you have only file name as Unicode string, use it as **ObjectName**. \
  If you have only a `HANDLE` to file, set it as **RootDirectory**. Set **ObjectName** as empty string.

# Related Win32 API
 - [`DeleteFile`](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-deletefile) (Although it does more than just forwarding the arguments and invoking this procedure.) 

# Documented by

* Tomasz Nowak

# See also

* `NtCreateFile`
* `NtOpenFile`
* `NtSetInformationFile`
