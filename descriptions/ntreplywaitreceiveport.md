`NtReplyWaitReceivePort` is typically used by *LPC* server process for receive *LPC* requests incoming from client process.

### PortHandle

`HANDLE` to Port Object returned by

### ReceivePortHandle

### Reply

If other side waiting for reply message, you can send it by specifying *LPC* Message Buffer as this parameter.

### IncomingRequest

Pointer to user's allocated buffer receiving request data. Received data starts with

---

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `LPC_MESSAGE`
* `NtAcceptConnectPort`
* `NtReplyPort`
* `NtReplyWaitReplyPort`
* `NtRequestPort`
* `NtRequestWaitReplyPort`
