# -*- coding: utf-8 -*-
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.core import MON, TUE, WED, THU, FRI, SAT, SUN

from datetime import datetime

from isoweek import Week

import logging

logger = logging.getLogger(__name__)



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


    def get_next_workday(self,year, week, weekday):
        """
        Get the next working day. If entering date is friday or a weekend day, get the first workday of the next week

        It doesn't take care about the holidays, that's are controlled as a second test in ensure_same_day_scenario method

        Returns a datetime.date
        """
        if weekday >=FRI:
            weekday=MON
            week+=1
        else:
            weekday+=1

        return  Week(year, week).day(weekday)



    def get_next_weekend_day(self,year, week, weekday):
        """
        Get the next weekend day. If entering date is friday or a weekend day, get the first workday of the next week

        Returns a datetime.date
        """

        logger.info("Getting next weekend day since {}".format(Week(year, week).day(weekday)))

        if weekday==SUN:
            weekday=SAT
            week+=1
        else:
            weekday=SAT

        logger.info("{}".format(Week(year, week).day(weekday)))

        return  Week(year, week).day(weekday)


    def is_workable(self, day):
        if type(day) is datetime:
            day = day.date()

        if day.weekday() in self.get_weekend_days():
             return False

        return True



class OneYearAgo():

    day_present=datetime
    day_one_year_ago=datetime
    years_ago = 1


    def __init__(self, dia, years=1):
        self.years_ago= int(years)
        self.day_present=dia
        self.get_one_year_ago()


    def get_day_info(self,day):
        logger.debug ("Day info:\n"
                      "  year: {}\n"
                      "  week: {}\n"
                      "  weekday: {}"
                      .format(day[0], day[1], day[2]))


    def get_one_year_ago(self, dia=None):
        self.get_year_ago(dia, 1)


    def compare_days(self, ree_cal, current, past, day, test, correctionOK, correctionKO, result):
        """
        Trigger any function to compare two days

        Very useful to standarize the tests to perform for two dates

        If both days have the same value for the test all is done!

        Else, review the present day to ensure that the past day have the same condition
        ,so , if test present is OK, execute correctionOK function, if not, correctionKO

        Ie, is_working_day test, with get_next_workday as correction function if present is working_day, and get_next_weekend_day if isn't

            if present is tuesday and past is sunday
            we must ensure that the past day is the next working day, in this case monday of the next week
            . so trigger


        :param ree_cal: calendar to use
        :param current: present day
        :param past: past day
        :param test: function to execute
        :param result: bool that identifies if both tests must have the same result (1) or diffenent (0)
        :return:
        """

        test_function = getattr(ree_cal, test)
        test_current = test_function(current.day(day))
        test_past = test_function(past.day(day))

        logger.info ("{}? current: {}, past: {}".format(test,test_current,test_past))

        if test_current != test_past:
            logger.info ( "Present and past day don't accomplish {}".format(test))

            if test_current: # if current is accomplish the test // current is_working_day
                test_OK = getattr(ree_cal, correctionOK)
                return test_OK(past.year, past.week, day)
            else:
                test_KO = getattr(ree_cal, correctionKO)
                return test_KO(past.year, past.week, day)

        else:
            logger.info ( "Present and past day accomplish {}".format(test))
            return None


    def ensure_same_day_scenario(self, current, past, day):
        ree_cal = REECalendar()


        past_day = self.compare_days(ree_cal, current, past, day, "is_workable","get_next_workday","get_next_weekend_day", 1)
        past_day = self.compare_days(ree_cal, current, past, day, "is_holiday","get_next_workday","get_next_weekend_day", 1)


        if past_day != None:
            return past_day
        #self.compare_days(ree_cal, current, past, day, "is_holiday", 1)


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

        past_new = self.ensure_same_day_scenario(week_current, week_past, weekday)

        if past_new:
            self.day_one_year_ago =  datetime.combine(past_new, datetime.min.time() )
        else:
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
