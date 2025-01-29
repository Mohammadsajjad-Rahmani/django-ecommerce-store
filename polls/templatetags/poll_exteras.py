from django import template
from jalali_date import date2jalali

register = template.Library()


# ba estefade az register mishe filter va tag haye jadid sakht

@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, "")


# register.filter("cut", cut)
# ham be ravesh bala mishe registeresh kard ham be ravesh decorator
# bishtar qasdemon inja ine ke khodemon template tag besazim


@register.filter(name='jalali_date')
def jalali_date(value):
    return date2jalali(value)


@register.filter(name='three_digit_currency')
def three_digit_currency(value: int):
    return '{:,}'.format(value) + '  تومان'


@register.simple_tag(name='multiply')
def multiply(count, price, **args):
    return three_digit_currency(count * price)
