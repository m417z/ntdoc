Function `NtDisplayString` display specified string in *text-mode* (typically: blue screen).

**Warning:** Trying to display string without previously switch to text-mode results as system hang.

### String

Pointer to `UNICODE_STRING` contains string to display. Some basic control characters are implemented (like *CR*, *LF*).

# Documented by

* Tomasz Nowak

# Requirements

Privilege: `SE_TCB_PRIVILEGE`
