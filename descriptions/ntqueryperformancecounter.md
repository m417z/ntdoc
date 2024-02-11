This function is [documented in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/devnotes/ntqueryperformancecounter).

---

### PerformanceCounter

Result is number of processor ticks after last reset.

### PerformanceFrequency

It's number of processor ticks per one second.

---

Another method of `uptime` calculation:

`UpTime = PerformanceCounter / PerformanceFrequency;`

# Related Win32 API
 - [`QueryPerformanceCounter`](https://learn.microsoft.com/en-us/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter)
 - [`QueryPerformanceFrequency`](https://learn.microsoft.com/en-us/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency)

# Documented by

* Sven B. Schreiber
* Tomasz Nowak
