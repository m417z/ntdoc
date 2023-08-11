This function is used for signal KeyedEvent object \
with value specified as Key \
parameter. If there are no other thread \(or threads\) waiting for \
the same KeyedEvent with the same Key value, waiting is performed up to \
NtWaitForKeyedEvent called by any other thread. \
KeyedEventHandle HANDLE to \
KeyedEvent object. \
Key Value used as KEY. Note that \
this value has to have lowest bit cleared \(must divide by \
two\). \
Alertable If set, waiting can be broken \
by alerting thread. \
Timeout Optional pointer for timeout \
value. \
Supported on system versions: \
Win XP/2003

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateKeyedEvent \
NtOpenKeyedEvent \
NtWaitForKeyedEvent
