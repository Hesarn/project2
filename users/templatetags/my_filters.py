from django import template
import datetime
from math import ceil, floor
register = template.Library()

@register.filter(name='age')
def age(birthday_year):
    return datetime.datetime.now().year - birthday_year

@register.filter(name='round')
def roundNumber(num):
    return round(num)


@register.filter(name='decimal')
def decimal(num):
    return int(num) + 0.1*(int(num*10)%10)


@register.filter(name='_replace')
def replace(name):
    return name.replace('_', ' ')





