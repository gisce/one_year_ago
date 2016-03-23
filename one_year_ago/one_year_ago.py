# -*- coding: utf-8 -*-
__author__ = 'XaviTorello'

from electrical_calendar import REECalendar

from datetime import datetime

from isoweek import Week

import logging

logger = logging.getLogger(__name__)


class OneYearAgo(object):

    day_present=datetime
    day_year_ago=datetime
    years_ago = 1


    def __init__(self, dia, years=1):
        assert type(dia) == datetime, "Day must be a datetime object"
        self.years_ago= int(years)
        self.day_present=dia
        self.get_year_ago(self.day_present, self.years_ago)


    def get_day_info(self,day):
        logger.debug ("Day info:\n"
                      "  year: {}\n"
                      "  week: {}\n"
                      "  weekday: {}"
                      .format(day[0], day[1], day[2]))


    def get_one_year_ago(self, dia=None):
        return self.get_year_ago(dia, 1)


    def compare_days(self, ree_cal, current, past, day, test, correctionOK, correctionKO, result=1):
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

        logger.debug ("{}? current: {}, past: {}".format(test,test_current,test_past))

        if test_current != test_past:
            logger.debug ( " - Present and past day don't accomplish {}".format(test))

            if test_current: # if current accomplish the test // current is_working_day
                if correctionOK:
                    test_OK = getattr(ree_cal, correctionOK)
                    return test_OK(past.year, past.week, day)
                else:
                    return ree_cal.get_same_holiday(current, past, day)  ## enhacement to return the variable holidays for this year WIP
                    #return datetime(past.year, current.day(day).month, current.day(day).day)
            else:
                if correctionKO:
                    test_KO = getattr(ree_cal, correctionKO)
                    return test_KO(past.year, past.week, day)
                else:
                    return ree_cal.get_same_holiday(current, past, day)
                    #return datetime(past.year, current.day(day).month, current.day(day).day)

        else:
            logger.debug ( " - Present and past day accomplish {}".format(test))
            return None


    def ensure_same_day_scenario(self, current, past, day):
        ree_cal = REECalendar()


        past_day = self.compare_days(ree_cal, current, past, day, "is_workable","get_next_workday","get_next_weekend_day", 1)
        past_day = self.compare_days(ree_cal, current, past, day, "is_holiday",None,None, 1)

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
            self.day_year_ago =  datetime.combine(past_new, datetime.min.time())
        else:
            self.day_year_ago =  datetime.combine(week_past.day(weekday), datetime.min.time())


        logger.debug ("SUMMARY")

        logger.debug (" - Present day: {}".format(week_current.day(weekday)))

        logger.debug (" - Past day ini: {}".format(week_past.day(weekday)))

        logger.debug (" - Past day correction: {}".format(self.day_year_ago.strftime("%Y-%m-%d")))

        logger.info ("{} year ago from {} was {}" .format(years_ago, self.day_present.strftime("%Y-%m-%d"), self.day_year_ago.strftime("%Y-%m-%d")))

        return self.day_year_ago


    def get_current_week(self):
        return self.day_present.isocalendar()[1]


    def get_past_week(self):
        return self.day_present.isocalendar()[1]

