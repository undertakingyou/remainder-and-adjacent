import datetime


TZ = datetime.timezone(-datetime.timedelta(hours=0))
HOUR = datetime.timedelta(hours=1)


def remainder_and_adjacent(current_schedule):
    """Return what times would take up the remainder and be adjacent.

    Args:
        current_schedule list(reservations): List of reservations
            that we need to work around.

    Returns:
        list
    """
    try:
        for i in range(len(current_schedule)):
            for item in ('start', 'end'):
                current_schedule[i][item] = datetime.datetime.fromisoformat(
                    current_schedule[i][item])
    except Exception:
        raise ValueError('unable to process the current schedule')

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

    for index, item in (('first', first), ('second', second)):
        difference = item - now
        suggested_time = {
            'value': int(difference.seconds/60),
            'units': 'mins',
            'start': now.isoformat(),
            'end': item.isoformat()
        }
        for event in current_schedule:
            if now < event.get('start')\
                    and item <= event.get('start'):
                # We have an event, but our suggestion will finish before we
                # need to worry about it.
                continue
            elif now < event.get('start')\
                    and event.get('start') < item:
                # We have an event that starts after now, but the suggested
                # end time is after that start time, adjust our end.
                new_diff = event.get('start') - now
                suggested_time['value'] = int(new_diff.seconds/60)
                suggested_time['end'] = event.get('start').isoformat()
            elif event.get('start') < now\
                    and event.get('end') < item:
                # We have a currently running event, that will end before our
                # suggestion is over. We need to adjust our start time.
                new_diff = event.get('end') - item
                suggested_time['value'] = int(new_diff.seconds/60)
                suggested_time['start'] = event.get('end').isoformat()
            elif event.get('start') < now\
                    and item < event.get('end'):
                # We have an event that completely eclipses our suggestion. We
                # need to abort the suggestion.
                suggested_time = {}

        # Finally, add the suggestion
        response.append(suggested_time)

    if response[0] == response[1]:
        del(response[1])

    return response
