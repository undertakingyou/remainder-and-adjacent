# Python Solution
This is the solution done in python.

## To Run
### Phase 1
To run, simply cd to the directory that contains the phase 1 file, and then
execute `python ./phase1.py`, the output will be the string version of the
python dictionary that matches the required format.

### Phoses 2 and 3
Phases two and three are done together, because it is just more cases around
when to modify the original suggtions. To run cd to the directory containing
the phase2and3.py file and use a tool like the python shell
or ipython. You will execute something like the following:
```python
In [1]: from phase2and3 import remainder_and_adjacent

In [2]: from phase2and3 import TZ

In [3]: import datetime

In [4]: start = datetime.datetime(2020, 3, 12, 22, 45, tzinfo=TZ)

In [5]: end = datetime.datetime(2020, 3, 12, 23, 15, tzinfo=TZ)

In [6]: first_event = {
   ...: 'title': 'something',
   ...: 'description': '',
   ...: 'start': start.isoformat(),
   ...: 'end': end.isoformat()
   ...: }

In [7]: remainder_and_adjacent([first_event])
```
 The output will be the string version of python dictionary that matches the
 required format.
