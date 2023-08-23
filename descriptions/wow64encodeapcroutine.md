This macro encodes the function pointer and indicates to `NtQueueApcThread`, `NtQueueApcThreadEx`, or `NtQueueApcThreadEx2` that the APC should be executed in the WoW64 mode.

To decode the pointer back, use `Wow64DecodeApcRoutine`.

# See also
 - `RtlQueueApcWow64Thread`
