# -*- coding: utf-8 -*-
"""
conversion forumulas for temperatures
"""

import decimal


def celcius_to_kelvin(celcius):
    """
    Args:
        conversion (float) : Celcius to Kelvin
    Returns:
        conversion (float) : Returns Kelvin
    """
    conversion = decimal.Decimal(celcius) + decimal.Decimal('273.15')
    return round(conversion, 3)


def celcius_to_fahrenheit(celcius):
    """
    Args:
        conversion (float) : Celcius to Fahrenheit
    Returns:
        conversion (float) : Returns Fahrenheit
    """
    conversion = (((decimal.Decimal(celcius)* 9) / 5) + 32)
    return conversion    


def fahrenheit_to_kelvin(fahrenheit):
    """
    Args:
        conversion (float) : Fahrenheit to Kelvin
    Returns:
        conversion (float) : Returns Kelvin
    """
    conversion = ((decimal.Decimal(fahrenheit) - 32) * 5) / 9
    conversion += decimal.Decimal(273.15)
    return round(conversion, 3)


def fahrenheit_to_celcius(fahrenheit):
    """
    Args:
        conversion (float) : Fahrenheit to Celcius
    Returns:
        conversion (float) : Returns Celcius
    """
    conversion = ((decimal.Decimal(fahrenheit) - 32) * 5) / 9
    return round(conversion, 3)


def kelvin_to_fahrenheit(kelvin):
    """
    Args:
        conversion (float) : Kelvin to Fahrenheit
    Returns:
        conversion (float) : Returns Fahrenheit
    """
    conversion = (((decimal.Decimal(kelvin) - decimal.Decimal('273.15')) / 5) * 9) + 32
    return round(conversion, 3)


def kelvin_to_celcius(kelvin):
    """
    Args:
        conversion (float) : Kelvin to Celcius
    Returns:
        conversion (float) : Returns Celcius
    """
    conversion = decimal.Decimal(kelvin) - decimal.Decimal('273.15')
    return round(conversion, 3)