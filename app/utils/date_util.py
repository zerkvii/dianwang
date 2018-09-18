import pendulum


def get_current_time():
    return pendulum.now('Asia/Shanghai').to_datetime_string()
