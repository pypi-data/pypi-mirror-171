import logging
import threading
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool
from typing import Any, Callable


def __thread_fn__(event: threading.Event, fn: Callable, *args: Any, **kwargs: Any):
    pass


def RunInThread(fn: Callable, *args: Any, executor: ThreadPoolExecutor = None, **kwargs: Any) -> threading.Event:
    event = threading.Event()

    def thread_fn():
        if fn is not None:
            try:
                fn(*args, **kwargs)
            except Exception as e:
                logging.error(e)
        event.set()

    if executor is None:
        t = threading.Thread(target=thread_fn)
        t.start()
    else:
        executor.submit(thread_fn)
    return event


def Wait(event: threading.Event):
    timeout = 5.0
    while not event.is_set():
        event.wait(timeout)
