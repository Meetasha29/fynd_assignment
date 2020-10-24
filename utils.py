import functools
from contextlib import ContextDecorator

from connectors.database import db


class Atomic(ContextDecorator):

    def __init__(self, instance, session_close=True):
        instance.auto_commit = False
        self.session_close = session_close

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.session_close:
            if exc_type:
                db.session.rollback()
            else:
                db.session.commit()


def parse_response(func=None, status=400, success=200):
    if func is None:
        return functools.partial(parse_response, status, success)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        status_code = status
        response = func(*args, **kwargs)
        if response.success:
            status_code = success
        response = response.to_dict()
        db.session.close()
        return response, status_code
    return wrapper
