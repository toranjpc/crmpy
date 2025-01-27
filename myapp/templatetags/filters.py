import jdatetime
from django import template
import datetime

register = template.Library()

@register.filter
def to_jalali_Year(gregorian_date):
    if gregorian_date:
        jalali_date = jdatetime.date.fromgregorian(date=gregorian_date)
        return jalali_date.strftime('%Y/%m/%d')
    return ''

@register.filter
def to_jalali_Hour(gregorian_date):
    if gregorian_date:
        if isinstance(gregorian_date, datetime.datetime):
            jalali_datetime = jdatetime.datetime.fromgregorian(datetime=gregorian_date)
            return jalali_datetime.strftime('%H:%M')
        elif isinstance(gregorian_date, datetime.date):
            return "00:00"
    return ''

@register.filter
def to_jalali(gregorian_date):
    if gregorian_date:
        if isinstance(gregorian_date, datetime.datetime):
            jalali_datetime = jdatetime.datetime.fromgregorian(datetime=gregorian_date)
            return jalali_datetime.strftime('%Y/%m/%d %H:%M')
        elif isinstance(gregorian_date, datetime.date):
            jalali_date = jdatetime.date.fromgregorian(date=gregorian_date)
            return jalali_date.strftime('%Y/%m/%d 00:00')
    return ''
