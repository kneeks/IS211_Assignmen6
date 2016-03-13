# -*- coding: utf-8 -*-
"""
all forumlas in one file
"""

class ConversionNotPossible(Exception): pass


class NonNumericNotPossible(Exception): pass
    

class NegativeNotPossible(Exception): pass
    

conversion_dictionary = {
('fahrenheit','kelvin'):('(x + 459.67) * 5.00/9.00'),
('fahrenheit','celcius'):('(x - 32.00)* 5.00/9.00'),
('kelvin','celcius'):('x - 273.15'),
('kelvin','fahrenheit'):('x * 9.00/5.00 - 459.67'),
('celcius','kelvin'):('x + 273.15'),
('celcius','fahrenheit'):('x * 9.000/5.000 + 32.00'),
('meters','yards'):('x * 1.09361'),
('meters','miles'):('x / 1609.34'),
('yards','miles'):('x / 1760.00'),
('yards','meters'):('x * 0.9144'),
('yards','miles'):('x / 1760.00'),
('yards','meters'):('x * 0.9144')
}


def convert(fromunit,tounit,value):
    if(type(value) is not int and type(value) is not long and type(value) is not float):
        raise NonNumericNotPossible, 'Value input needs to be numeric.'
    elif(conversion_dictionary[(fromunit,tounit)] is None):
        raise ConversionNotPossible, 'Cannot match units.'
    elif ((fromunit == 'miles' or fromunit == 'yards' or fromunit == 'meters') and value < 0):
        raise NegativeNotPossible, 'Distance unit is negative!'
    else:
        x = value#for variable in dict
        result = eval(conversion_dictionary[(fromunit,tounit)])
        return round(result,2)