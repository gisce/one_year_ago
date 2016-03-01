# One Year Ago

OneYearAgo provides an Easy way to get the same day scenario (week, weekday, working day and holiday) for a previous year.

It's important to define that we understand "the same day" as the day in a previous year that accomplish:
- Same week of year
- Same weekday
  - Ensuring that if the present day is a working day, the past day must be too; and viceversa
  - (WIP) Ensuring that if the present day is a holiday the past day must be the more close date (if there are no more than 30days of difference between the gap) or XXX [issue #2]

## How to use it

Just import it    # WIP pip installer [issue #1]
```
from one_year_ago.one_year_ago import OneYearAgo
``` 

and 
```
logging.basicConfig(level=logging.DEBUG)

day=datetime(2016,5,1)
day=datetime.today()

a_year_ago = OneYearAgo(day)

## Get one year ago from the current day
a_year_ago.get_one_year_ago()

## To set a different past years to get
a_year_ago.get_year_ago(yearsago=2)
```

## Example of use

[GIST usage example](https://gist.github.com/XaviTorello/3b90b44983986a751685)


ipython dump
```
In [24]: dia=datetime(2016,11,1) # is_workable (friday), is_holiday

In [25]: fa_un_any.get_year_ago(dia, 1)
DEBUG:__main__:Calculating 1 year ago for 2016-11-01 00:00:00
DEBUG:__main__:is_workable? current: True, past: True
DEBUG:__main__: - Present and past day accomplish is_workable
DEBUG:__main__:is_holiday? current: True, past: False
DEBUG:__main__: - Present and past day don't accomplish is_holiday
DEBUG:electrical_calendar.electrical_calendar:  - Searching 2016/11/1 holiday on 2015
DEBUG:electrical_calendar.electrical_calendar:  - Found same holiday: 2015/11/1 [All Saints Day]
DEBUG:__main__:SUMMARY
DEBUG:__main__: - Present day: 2016-11-01
DEBUG:__main__: - Past day ini: 2015-10-27
DEBUG:__main__: - Past day correction: 2015-11-01
INFO:__main__:1 year ago from 2016-03-25 was 2015-11-01
Out[25]: datetime.datetime(2015, 11, 1, 0, 0)

In [26]: fa_un_any.get_year_ago(dia, 2)
DEBUG:__main__:Calculating 2 year ago for 2016-11-01 00:00:00
DEBUG:__main__:is_workable? current: True, past: True
DEBUG:__main__: - Present and past day accomplish is_workable
DEBUG:__main__:is_holiday? current: True, past: False
DEBUG:__main__: - Present and past day don't accomplish is_holiday
DEBUG:electrical_calendar.electrical_calendar:  - Searching 2016/11/1 holiday on 2014
DEBUG:electrical_calendar.electrical_calendar:  - Found same holiday: 2014/11/1 [All Saints Day]
DEBUG:__main__:SUMMARY
DEBUG:__main__: - Present day: 2016-11-01
DEBUG:__main__: - Past day ini: 2014-10-28
DEBUG:__main__: - Past day correction: 2014-11-01
INFO:__main__:2 year ago from 2016-03-25 was 2014-11-01
Out[26]: datetime.datetime(2014, 11, 1, 0, 0)

In [27]: fa_un_any.get_year_ago(dia, 3)
DEBUG:__main__:Calculating 3 year ago for 2016-11-01 00:00:00
DEBUG:__main__:is_workable? current: True, past: True
DEBUG:__main__: - Present and past day accomplish is_workable
DEBUG:__main__:is_holiday? current: True, past: False
DEBUG:__main__: - Present and past day don't accomplish is_holiday
DEBUG:electrical_calendar.electrical_calendar:  - Searching 2016/11/1 holiday on 2013
DEBUG:electrical_calendar.electrical_calendar:  - Found same holiday: 2013/11/1 [All Saints Day]
DEBUG:__main__:SUMMARY
DEBUG:__main__: - Present day: 2016-11-01
DEBUG:__main__: - Past day ini: 2013-10-29
DEBUG:__main__: - Past day correction: 2013-11-01
INFO:__main__:3 year ago from 2016-03-25 was 2013-11-01
Out[27]: datetime.datetime(2013, 11, 1, 0, 0)

In [28]: fa_un_any.get_year_ago(dia, 4)
DEBUG:__main__:Calculating 4 year ago for 2016-11-01 00:00:00
DEBUG:__main__:is_workable? current: True, past: True
DEBUG:__main__: - Present and past day accomplish is_workable
DEBUG:__main__:is_holiday? current: True, past: False
DEBUG:__main__: - Present and past day don't accomplish is_holiday
DEBUG:electrical_calendar.electrical_calendar:  - Searching 2016/11/1 holiday on 2012
DEBUG:electrical_calendar.electrical_calendar:  - Found same holiday: 2012/11/1 [All Saints Day]
DEBUG:__main__:SUMMARY
DEBUG:__main__: - Present day: 2016-11-01
DEBUG:__main__: - Past day ini: 2012-10-30
DEBUG:__main__: - Past day correction: 2012-11-01
INFO:__main__:4 year ago from 2016-03-25 was 2012-11-01
Out[28]: datetime.datetime(2012, 11, 1, 0, 0)




```
