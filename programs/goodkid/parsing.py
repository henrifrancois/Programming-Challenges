import time
import re, urllib
from functools import wraps




def theme_crawler():
    """Crawls the web up to n number of pages,
     only indexing pages that go by a certain theme."""

    def base_crawler(page):
        pass

    def get_theme():
        pass

    def fn_timer(function):
        @wraps(function)
        def function_timer(*args, **kwargs):
            initial_time = time.time()
            result = function(*args, **kwargs)
            actual_time = time.now()
            print("Total time running %s: %s seconds"
                %(function.func_name, str(actual_time-initial_time))
                )
            return result
        return function_timer
