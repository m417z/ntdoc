This function is [documented in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/devnotes/ntquerysection).

---

### InformationClass

Use one of following:

* `SectionBasicInformation // Result is SECTION_BASIC_INFORMATION structure`
* `SectionImageInformation // Result is SECTION_IMAGE_INFORMATION structure`

`SectionImageInformation` Are available only for file-based sections.

# See also

* `NtCreateProcess`
* `NtCreateSection`
* `NtOpenSection`
* `SECTION_BASIC_INFORMATION`
* `SECTION_IMAGE_INFORMATION`
