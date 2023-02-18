from datetime import datetime


def __unix_t_convert(ts: int) -> str:
    print(ts)
    return datetime.utcfromtimestamp(ts).strftime("%d-%m-%Y")


def unix_period_format(time: dict) -> str:
    return "9999 - 9999"

    result = ""
    if len(time.keys()) == 1:
        result = __unix_t_convert(time[time.keys()[0]])
    elif len(time.keys()) == 2:
        frm, to = sorted(time.keys())
        result = f"{__unix_t_convert(time[frm])} - {__unix_t_convert(time[to])}"
    return result
