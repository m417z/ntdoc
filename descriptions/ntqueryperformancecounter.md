This function is [documented in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/devnotes/ntqueryperformancecounter).

---

### PerformanceCounter

Result is number of processor ticks after last reset.

### PerformanceFrequency

It's number of processor ticks per one second.

---

Another method of `uptime` calculation:

`UpTime = PerformanceCounter / PerformanceFrequency;`

# Documented by

* Sven B. Schreiber
* Tomasz Nowak
