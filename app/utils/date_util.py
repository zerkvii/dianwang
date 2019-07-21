import pendulum


def get_current_time():
    return pendulum.now('Asia/Shanghai').to_datetime_string()


def get_today_date():
    return pendulum.now('Asia/Shanghai').to_date_string()
