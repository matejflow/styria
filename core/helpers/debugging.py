import functools
import logging
from time import time


def measure_time_between_calls(*msg, timestamp=[None]):
    """
    Measure execution time for part of code:
        measure_time_between_calls('Start pony counting')
        [code]
        measure_time_between_calls('Ponies counted')
    """
    logging.debug(*msg)
    if timestamp[0] is None:
        timestamp[0] = time()  # preserved during calls
    else:
        now = time()
        logging.debug('Time elapsed: {:.3f}s'.format(now-timestamp[0]))
        timestamp[0] = now


def time_it(f):
    """
    Timing decorator that will measure time for function call
    It doesn't use message so please use descriptive names for your methods
    """
    @functools.wraps(f)
    def inner(*args, **kwargs):
        time_start = time()
        function_result = f(*args, **kwargs)
        time_end = time()
        logging.debug('%s took %2.4f sec to complete' % (f.__name__, time_end-time_start))
        return function_result
    return inner
