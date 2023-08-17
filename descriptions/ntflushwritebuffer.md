Function `NtFlushWriteBuffer` does nothing...

---

It test *IRQ Level*, and call *HAL* export named `KeFlushWriteBuffer`.

`KeFlushWriteBuffer` as first **asm** code has ret, so it returns immediatelly.

Next `NtFlushWriteBuffer` clear `eax` (set result of call to `STATUS_SUCCESS`) and returns to *User-Mode*.

# Documented by

* Tomasz Nowak
