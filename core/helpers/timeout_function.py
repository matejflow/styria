import signal
from contextlib import contextmanager
from threading import Timer

from .exceptions import TimeoutReachedException


@contextmanager
def timeout_function(seconds=5):
    """
    Raises exception of your code is not executed in given timeout
    Example:

    try:
        with timeout_function(60):
            your_code_ here
    except TimeoutError:
        do_someting
    """

    def signal_handler(signum, frame):
        raise TimeoutError("Timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)

    try:
        yield
    finally:
        signal.alarm(0)


def timer_object_timeout(seconds=5):
    """
    Returns threading Timer object, should use .start() and .cancel()
    If condition is not met, it raises TimeoutReachedException
    """
    def raise_timeout_exception():
        raise TimeoutReachedException(seconds=seconds)

    return Timer(seconds, raise_timeout_exception)
