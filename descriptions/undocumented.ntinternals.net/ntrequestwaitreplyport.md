`NtRequestWaitReplyPort` is used typically by client side in *LPC* connection.

### PortHandle

`HANDLE` to Port Object.

### Request

Pointer to `LPC_MESSAGE` buffer contains request data.

### IncomingReply

Pointer to `LPC_MESSAGE` buffer filled on return with reply from other side.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `LPC_MESSAGE`
* `NtAcceptConnectPort`
* `NtConnectPort`
* `NtReplyPort`
* `NtReplyWaitReceivePort`
* `NtReplyWaitReplyPort`
* `NtRequestPort`
