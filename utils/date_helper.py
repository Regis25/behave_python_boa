import datetime
import re


class DateHelper:

    @staticmethod
    def convert_date(date):
        """
        Converts the date message to dd/mm/yy
        """
        today = datetime.datetime.now()
        if date == "today":
            return today
        if date == "tomorrow":
            return today + datetime.timedelta(days=1)
        if "days" in date:
            days = re.search(r"(\d*)", date)
            return today + datetime.timedelta(days=int(days.group()))
        if "weeks" in date:
            weeks = re.search(r"(\d*)", date)
            return today + datetime.timedelta(weeks=int(weeks.group()))
