import psutil


def get_memory_state():
    return psutil.virtual_memory().percent


def get_cpu_state():
    return psutil.cpu_percent(0)

# def get_hd_state():
