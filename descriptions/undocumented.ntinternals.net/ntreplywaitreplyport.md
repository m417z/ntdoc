`NtReplyWaitReplyPort` sends REPLY and waits for other side REPLY.

### PortHandle

`HANDLE` to Port Object.

### Reply

There's a pointer to `LPC_MESSAGE` structure. On input, should be filled with REPLY data by user. On output it contains REPLY from other side.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `LPC_MESSAGE`
* `NtAcceptConnectPort`
* `NtConnectPort`
* `NtReplyPort`
* `NtReplyWaitReceivePort`
* `NtRequestWaitReplyPort`
