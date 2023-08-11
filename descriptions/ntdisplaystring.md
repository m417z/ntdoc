Function NtDisplayString display specified string in \
text\-mode \(typically: blue screen\). \
Warning: Trying to display string without \
previously switch to text\-mode results as system hang. \
String Pointer to UNICODE\_STRING \
contains string to display. Some basic control characters are \
implemented \(like CR, LF\).

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib \
Privilege: SE\_TCB\_PRIVILEGE

See also:
