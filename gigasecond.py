from datetime import timedelta
def add_gigasecond(moment):
    second = 10**9
    print("second {}".format(second))
    result = moment + timedelta(seconds = second)
    print("moment : {} , timedelta(seconds = second) : {} , result : {}".format(moment,timedelta(seconds=second),result))
    return result
