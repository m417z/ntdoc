# Changelog

All notable documentation content changes are documented in this file.
<!-- content -->
## 25 Sep 2025
**Official Windows documentation**: NtDoc now includes documentation from the official Windows Driver Kit DDI reference and parts of the Win32 API reference.

## 16 Aug 2024
**Process operations ([#16](https://github.com/m417z/ntdoc/pull/16))**: `NtGetNextProcess`, `NtTerminateProcess`, `NtSuspendProcess`, `NtChangeProcessState`.

## 3 Dec 2023
**Process information ([#11](https://github.com/m417z/ntdoc/pull/11))**: `NtQueryInformationProcess`, `NtSetInformationProcess`, and 100+ `PROCESSINFOCLASS` values.
<!-- more -->
## 13 Oct 2023
**Token operations ([#8](https://github.com/m417z/ntdoc/pull/8))**: Various operations on tokens, capabilities, and AppContainer SIDs. 47 pages, including: `NtCreateTokenEx`, `NtOpenThreadTokenEx`, `NtQueryInformationToken`, `NtSetInformationToken`, `NtDuplicateToken`.

## 24 Aug 2023
**Handle/object operations ([#4](https://github.com/m417z/ntdoc/pull/4))**: Object attributes and common handle operations. 33 pages, including: `NtQueryObject`, `NtSetInformationObject`, `NtDuplicateObject`, `NtWaitForMultipleObjects`, `NtClose`.

## 23 Aug 2023
**Thread operations ([#3](https://github.com/m417z/ntdoc/pull/3))**: Thread-related functions and types. 55 pages, including: `NtCreateThreadEx`, `NtOpenThread`, `NtSuspendThread`, `NtResumeThread`, `NtQueryInformationThread`.
