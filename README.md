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
from one_year_ago.one_year_ago import OneYearAgo, REECalendar
``` 

and 
```
from one_year_ago.one_year_ago import OneYearAgo, REECalendar

logging.basicConfig(level=logging.DEBUG)

print ree_cal.holidays(2016)

dia=datetime(2016,5,1)
dia=datetime.today()

a_year_ago = OneYearAgo(dia)

## Get one year ago from the current day
a_year_ago.get_one_year_ago()

## To set a different past years to get
a_year_ago.get_year_ago(yearsago=2)
```

## Example of use

[GIST usage example](https://gist.github.com/XaviTorello/3b90b44983986a751685)


