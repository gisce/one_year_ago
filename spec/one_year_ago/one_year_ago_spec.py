# -*- coding: utf-8 -*-
__author__ = 'XaviTorello'

from expects import *
from expects.testing import failure

from one_year_ago import OneYearAgo

import datetime

with description("One Year Ago"):
    with context('must be initialized'):
        with it('with a day to compute'):
            dia = datetime.datetime(2016, 2, 29)  # is_working, !is_holiday
            fa_un_any = OneYearAgo(dia)

    with context('can\'t be initialized'):
        with it('without a valid day to compute'):
            def ini_str():
                fa_un_any = OneYearAgo("rolf")
            expect(ini_str).to(raise_error(
                AssertionError, 'Day must be a datetime object'))

        with it('without day'):
            def ini_null():
                fa_un_any = OneYearAgo()
            expect(ini_null).to(raise_error(TypeError))

        with it('with a None day'):
            def ini_null():
                fa_un_any = OneYearAgo(None)
            expect(ini_null).to(raise_error(
                AssertionError, 'Day must be a datetime object'))

    with context('must reach the previous date correctly'):
        with it('for 2016/02/29, 1 year ago was: 2015/02/23'):
            dia = datetime.datetime(2016, 2, 29)
            dia_expected = datetime.datetime(2015, 2, 23)

            fa_un_any = OneYearAgo(dia).day_year_ago
            assert fa_un_any == dia_expected, "The calculated day for {} is not correct: {} (proposal) vs {} (correct)".format(
                dia, fa_un_any, dia_expected)

        with it('for 2016/02/29, 2 year ago was: 2014/02/24'):
            dia = datetime.datetime(2016, 2, 29)
            dia_expected = datetime.datetime(2014, 2, 24)

            fa_dos_anys = OneYearAgo(dia, years=2).day_year_ago

            assert fa_dos_anys == dia_expected, "The calculated day for {} is not correct: {} (proposal) vs {} (correct)".format(
                dia, fa_dos_anys, dia_expected)

    with context('calculated day must ensure mantain same weekday status'):
        with it('2016/3/23 (Wednesday) -> 2015/3/18 (Wednesday)'):
            dia = datetime.datetime(2016, 3, 23)  # Weekday (Wednesday)
            fa_un_any = OneYearAgo(dia).day_year_ago
            assert fa_un_any.isoweekday() == dia.isoweekday(), "Not have the same week day; present: {}({}), past: {}({})".format(
                dia, dia.isoweekday(), fa_un_any, fa_un_any.isoweekday())

    with context('calculated day must ensure mantain same weekend day status'):
        with it('2016/3/26 (Saturday) -> 2015/3/21 (Saturday)'):
            dia = datetime.datetime(2016, 3, 26)  # Weekend (Saturday)
            fa_un_any = OneYearAgo(dia).day_year_ago
            assert fa_un_any.isoweekday() == dia.isoweekday(), "Not have the same week day; present: {}({}), past: {}({})".format(
                dia, dia.isoweekday(), fa_un_any, fa_un_any.isoweekday())

    with context('calculated day for today must ensure mantain same weekday/weekend status'):
        with it('2016/3/26 (Saturday) -> 2015/3/21 (Saturday)'):
            dia = datetime.datetime.today()
            fa_un_any = OneYearAgo(dia).day_year_ago
            assert fa_un_any.isoweekday() == dia.isoweekday(), "Not have the same week day; present: {}({}), past: {}({})".format(
                dia, dia.isoweekday(), fa_un_any, fa_un_any.isoweekday())


# todo TEST week number

# todo TEST holidays scenario
