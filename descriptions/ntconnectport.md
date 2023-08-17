`NtConnectPort` is used by client process for establish *LPC* connection with Named Port's owner.

### ClientPortHandle

Result of call - `HANDLE` to Port Object.

### ServerPortName

Name of port to connect to.

### SecurityQos

### ClientSharedMemory

Used when calling process created Section Object for shared memory. See `NtAcceptConnectPort` for details.

### ServerSharedMemory

Used when calling process didn't create Section Object. See `NtAcceptConnectPort` for details.

### MaximumMessageLength

Maximum communication message length. This value is calculated by server on port creation process (see `NtCreatePort`).

### ConnectionInfo

Pointer to RAW buffer containing information from client. That information is received by server through `LPC_MESSAGE` with `MessageType` field set to `LPC_CONNECTION_REQUEST`.

### ConnectionInfoLength

Size of `ConnectionInfo` buffer, in bytes.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `LPC_MESSAGE`
* `LPC_SECTION_MEMORY`
* `LPC_SECTION_OWNER_MEMORY`
* `NtAcceptConnectPort`
* `NtCompleteConnectPort`
* `NtCreatePort`
