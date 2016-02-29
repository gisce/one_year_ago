# -*- coding: utf-8 -*-
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.core import THU, MON, FRI, SAT

from datetime import datetime

from isoweek import Week

import logging

logger = logging.getLogger(__name__)


import calendar

from workalendar.core import Calendar

class REECalendar (WesternCalendar, ChristianMixin):
    "REE Spanish Electrical Network (Red Eléctrica de España) Calendar"
    include_epiphany = False
    include_immaculate_conception = True
    include_good_friday = True
    include_assumption = True
    include_all_saints = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, u"Día del trabajador"),
        (10, 12, u"Fiesta nacional de España"),
        (12, 6, u"Día de la Constitución Española")
    )


class OneYearAgo():
    day_present=datetime
    day_one_year_ago=datetime
    years_ago = 1

    def __init__(self, dia, years=1):
        self.years_ago= int(years)
        self.day_present=dia


    def get_day_info(self,day):
        logger.debug ("Day info:\n"
                      "  year: {}\n"
                      "  week: {}\n"
                      "  weekday: {}"
                      .format(day[0], day[1], day[2]))


    def get_one_year_ago(self, dia=None):
        self.get_year_ago(dia, 1)

    def get_year_ago(self, dia=None, yearsago=None):

        if not dia:
            dia=self.day_present

        years_ago = self.years_ago
        if yearsago:
            years_ago = int(yearsago)


        logger.debug("Calculating {} year ago for {}".format(years_ago, dia))

        current = dia.isocalendar()  #0 year, 1 week, 2, weekday
        year = current[0]
        week = current[1]
        weekday = current[2]-1 #Isocalendar uses american weekdays


        week_current = Week(year, week)

        week_past = week_current.replace(year-years_ago, week)

        self.day_one_year_ago =  datetime.combine(week_past.day(weekday), datetime.min.time() )

        logger.debug ("Present day: {}".format(week_current.day(weekday)))
        self.get_day_info(self.day_present.isocalendar())

        logger.debug ("One year ago: {}".format(week_past.day(weekday)))
        self.get_day_info(self.day_one_year_ago.isocalendar())


        logger.info ("{} year ago from {} was {}" .format(years_ago, self.day_present, self.day_one_year_ago))


    def get_current_week(self):
        return self.day_present.isocalendar()[1]

    def get_past_week(self):
        return self.day_present.isocalendar()[1]


