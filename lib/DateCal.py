#!/usr/bin/env python
# -- coding: utf-8 --
from datetime import datetime
from datetime import date
from dateutil import relativedelta
import json

__version__ = '0.0.1'

class DateCal():

    def __init__(self):
        ROBOT_LIBRARY_SCOPE = 'GLOBAL'
        ROBOT_LIBRARY_VERSION = __version__
        self.today = date.today()

    def convert_date_to_string(self,dateJSon):
        """
        Arguments:
        | dateJSon | Test Data from Testcase excel |

        Example:
        | *keyword                  |      *dateJSon*                                                |
        | Convert Date To String    |  {"day":"01","month":"01","year":"1995","language":"TH"}       | 
        """
        self.DATE_DIC = json.loads(dateJSon)
        dateStr = "{}-{}-{}".format(self.DATE_DIC["year"],self.DATE_DIC["month"],self.DATE_DIC["day"])
        
        return dateStr
        
        
    def age_between(self,birthday):
        """
        Arguments: 
        | birthday |  Test Data from Testcase excel |

        Example:
        | *keyword         | *dateStr*               |
        | Age Between      | 1985-06-11              |
        """
        self.birth = datetime.strptime(birthday, "%Y-%m-%d")
        difference = relativedelta.relativedelta(self.today,self.birth)

        years = difference.years
        months = difference.months
        days = difference.days
        

        expResult = '{"statuscode":200,"output": ["' +str(years)+ ' ปี '+str(months)+' เดือน '+str(days)+' วัน"]}'

        return expResult



test = DateCal()
exp = test.age_between("1985-06-11")
print(exp)

               


    