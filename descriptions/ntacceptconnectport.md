`NtAcceptConnectPort` function is used in *LPC* communication by server process for establish connection with client. It should be called after `NtListenPort` completes.

### ServerPortHandle

Result of call - `HANDLE` to Port Object for established connection.

### AlternativeReceivePortHandle

### ConnectionReply

Pointer to `LPC_MESSAGE` structure received from `NtListenPort`. 

### AcceptConnection

If not set, connection on client's side will be refused.

### ServerSharedMemory

If connection uses large data buffers, and a `HANDLE` to Section Object for shared memory window is created on server side, server process shout set this parameter to pointer to `LPC_SECTION_OWNER_MEMORY` structure with filled **SectionHandle** member.

### ClientSharedMemory

Similar to `ServerSharedMemory`, but when connection client create Section Object. In this case server doesn't know section's `HANDLE`, but shared memory window is automatically maped to his address space. Size and base address of mapped memory are returned in `LPC_SECTION_MEMORY` structure.

---

This function returns `HANDLE` to newly created Port Object. All other *LPC* functions for currently accepted connection should use this `HANDLE`, not a base named port `HANDLE` created with `NtCreatePort`.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `LPC_MESSAGE`
* `LPC_SECTION_MEMORY`
* `LPC_SECTION_OWNER_MEMORY`
* `NtCompleteConnectPort`
* `NtCreatePort`
* `NtListenPort`
