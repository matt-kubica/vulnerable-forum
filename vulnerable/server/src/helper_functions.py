import logging

logging.basicConfig(level=logging.DEBUG)

def get_user_from_session_id(cookie):
    from .auth import cookies
    return cookies[cookie] if cookie in cookies else None
