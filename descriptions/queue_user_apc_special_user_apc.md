This constant defines a special value for `ReserveHandle` that allows queuing *special user-mode APCs*.

# Applicable to
 - `NtQueueApcThreadEx`

# Remarks
For the introduction to special user-mode APCs, see [this blog post](https://repnz.github.io/posts/apc/user-apc/#ntqueueapcthreadex-meet-special-user-apc).

Because execution of special APCs is not synchronized with the target thread (which might happen to acquire locks), it is crucial to keep the amount and complexity of the code invoked by the special APC routine to a minimum.

# Required OS version
This flag was introduced in Windows 10 RS5 (1809).
