`NtImpersonateClientOfPort` is called by LPC server process to get security context of client. That means: client's Token Object is associated with calling server thread (like `NtSetInformationThread` with `ThreadImpersonationToken` information class).

### PortHandle

`HANDLE` to Port Object opened with `NtAcceptConnectPort` call.

### Request

Pointer to `LPC_MESSAGE` structure contains reason of impersonation.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `LPC_MESSAGE`
* `NtAcceptConnectPort`
* `NtOpenThreadToken`
* `NtQueryInformationThread`
* `NtSetInformationThread`
