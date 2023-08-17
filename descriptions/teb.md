Structure `TEB` *(Thread Environment Block)* is memory block containing system variables placed in *User-Mode* memory. Every created thread have own `TEB` block. User can get address of `TEB` by call `NtCurrentTeb` function.

### Tib

Structure `NT_TIB` is avaiable in **\<WinNT.h\>** header file.

### EnvironmentPointer

### Cid

### ActiveRpcInfo

### ThreadLocalStoragePointer

### Peb

Pointer to `PEB` structure contains *Process Environment Block*.

### LastErrorValue

### CountOfOwnedCriticalSections

### CsrClientThread

### Win32ThreadInfo

### Win32ClientInfo[0x1F]

### WOW32Reserved

### CurrentLocale

### FpSoftwareStatusRegister

### SystemReserved1[0x36]

### Spare1

### ExceptionCode

### SpareBytes1[0x28]

### SystemReserved2[0xA]

### GdiRgn

### GdiPen

### GdiBrush

### RealClientId

### GdiCachedProcessHandle

### GdiClientPID

### GdiClientTID

### GdiThreadLocaleInfo

### UserReserved[5]

### GlDispatchTable[0x118]

### GlReserved1[0x1A]

### GlReserved2

### GlSectionInfo

### GlSection

### GlTable

### GlCurrentRC

### GlContext

### LastStatusValue

### StaticUnicodeString

### StaticUnicodeBuffer[0x105]

### DeallocationStack

### TlsSlots[0x40]

### TlsLinks

### Vdm

### ReservedForNtRpc

### DbgSsReserved[0x2]

### HardErrorDisabled

### Instrumentation[0x10]

### WinSockData

### GdiBatchCount

### Spare2

### Spare3

### Spare4

### ReservedForOle

### WaitingOnLoaderLock

### StackCommit

### StackCommitMax

### StackReserved

# Documented by

* ReactOS
* Tomasz Nowak

# See also

* `NtCurrentTeb`
* `PEB`
* `THREAD_BASIC_INFORMATION`
