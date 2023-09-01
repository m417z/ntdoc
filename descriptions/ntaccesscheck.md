Function `NtAccessCheck` should be used by server applications working in `SYSTEM` context for check access to object for connected client's token. See similar *Win32 API* **AccessCheck** in *Microsoft SDK*.

### SecurityDescriptor

Pointer to `SECURITY_DESCRIPTOR` structure.

### ClientToken

`HANDLE` to client's Token Object opened with `TOKEN_QUERY` access.

### DesiredAccess

`ACCESS_MASK` required by client.

### GenericMapping

Pointer to `GENERIC_MAPPING` structure. Caller can take it in a call to `NtQueryObject`.

### RequiredPrivilegesBuffer

Function fills this buffer with structure `PRIVILEGE_SET` contains required privileges.

### BufferLength

Pointer to `ULONG` value. On input this value means size of `RequiredPrivilegesBuffer` buffer. If buffer was to small, required buffer size is available on output.

### GrantedAccess

Pointer to `ACCESS_MASK` value receiving granted access for object.

### AccessStatus

Result of access check, in typical `NTSTATUS` format.

# Documented by

* Tomasz Nowak

# See also

* `NtImpersonateClientOfPort`
* `NtImpersonateThread`
* `NtOpenProcessToken`
* `NtOpenThreadToken`
* `NtPrivilegeCheck`
* `NtQueryObject`
* `NtQuerySecurityObject`
