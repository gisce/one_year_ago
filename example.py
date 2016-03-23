import logging
from one_year_ago import OneYearAgo
from datetime import datetime

logging.basicConfig(level=logging.INFO)

dia=datetime(2016,3 ,26) # !is_working, is_holiday
#dia=datetime(2016,5,1) # !is_working, is_holiday
#dia=datetime(2016,2,29) # is_working, !is_holiday

fa_un_any = OneYearAgo(dia)

print "Present:\t{}\nPast:   \t{}".format(fa_un_any.day_present, fa_un_any.day_year_ago)

#fa_un_any.get_one_year_ago()
#fa_un_any.get_year_ago(yearsago=2)
