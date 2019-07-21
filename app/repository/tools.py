from datetime import datetime, timedelta


def current_time():
    return datetime.now() - timedelta(hours=8)
