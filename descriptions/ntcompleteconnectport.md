`NtCompleteConnectPort` is called by server process after all initializations for new connection.

### PortHandle

`HANDLE` to Port Object received with `NtAcceptConnectPort` call.

---

Return from `NtConnectPort` on client's side is synchronised with return from this call. Both sides of *LPC* connection are ready for sending and receiving *LPC* messages.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `NtAcceptConnectPort`
* `NtConnectPort`
