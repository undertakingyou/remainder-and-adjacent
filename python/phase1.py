import datetime


TZ = datetime.timezone(-datetime.timedelta(hours=0))


def remainder_and_adjacent():
    now = datetime.datetime.now(tz=TZ).replace(second=0, microsecond=0)
    next_hour = False
    if now.minute > 30:
        next_hour = True
    first = datetime.datetime.now(tz=TZ).replace(second=0, microsecond=0)
    second = datetime.datetime.now(tz=TZ).replace(hour=now.hour + 1,
                                                  second=0, microsecond=0)
    if next_hour:
        first = first.replace(hour=now.hour + 1, minute=00)  # Top of the hour
        second = second.replace(minute=30)
    else:
        first = first.replace(hour=now.hour, minute=30)
        second = second.replace(minute=00)

    response = list()

    for item in (first, second):
        difference = item - now
        response.append(
            {
                'value': int(difference.seconds/60),
                'units': 'mins',
                'start': now.isoformat(),
                'end': item.isoformat()
            }
        )

    return response


if __name__ == '__main__':
    print(remainder_and_adjacent())
