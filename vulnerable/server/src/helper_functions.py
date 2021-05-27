import logging

logging.basicConfig(level=logging.DEBUG)

def getSecondIndexes(array):
    sorted = []
    for entry in array:
        sorted.append(entry[0])
    return sorted

def getUsernameFromSessionID(cookie):
        from .auth import cookies
        if cookie in cookies:
            return cookies[cookie]
        else:
            return None
