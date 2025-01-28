Converts the NTSTATUS to a DOS error code and then sets the error code to the current thread.

# Parameters
 - `Status` - the NTSTATUS that will be converted to DOS Error Code

# Related Win32 API
- [`SetLastError`](https://learn.microsoft.com/en-us/windows/win32/api/errhandlingapi/nf-errhandlingapi-setlasterror)
- [`SetLastErrorEx`](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setlasterrorex)

# See also
- `RtlNtStatusToDosError`
- `RtlNtStatusToDosErrorNoTeb`
- `RtlSetLastWin32Error`
- `RtlGetLastWin32Error`
- `RtlRestoreLastWin32Error`
