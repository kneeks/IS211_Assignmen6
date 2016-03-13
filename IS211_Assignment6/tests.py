# -*- coding: utf-8 -*-
"""
tests the conversion formulas on conversion file
"""


import unittest
import decimal
import conversions


class TestsConversions(unittest.TestCase):
    """
    Attributes: None
    """
    def Tests_C_K(self):
        """ Tests the conversion of Celcius to Kelvin.
        """
        expected = decimal.Decimal(273.15)
        returned = conversions.celcius_to_kelvin(0)
        self.assertEqual(returned, expected, msg='Error. Measurement is ',
                                                 'incorrect.')


    def Tests_C_F(self):
        """ Tests the conversion of from Celcius to Fahrenheit.
        """
        expected = 14
        returned = conversions.celcius_to_fahrenheit(-10)
        self.assertEqual(returned, expected, msg='Error. Measurement is ',
                                                 'incorrect.')


    def Tests_F_K(self):
        """ Tests the conversion of from Fahrenheit to Kelvin.
        """
        expected = decimal.Decimal(262.594)
        returned = conversions.fahrenheit_to_kelvin(13)
        self.assertEqual(returned, expected, msg='Error. Measurement is ',
                                                 'incorrect.')


    def Tests_F_C(self):
        """ Tests the conversion of from Fahrenheit to Celcius.
        """
        expected = 35
        returned = conversions.fahrenheit_to_celcius(95)
        self.assertEqual(returned, expected, msg='Error. Measurement is ',
                                                 'incorrect.')


    def Tests_K_F(self):
        """ Tests the conversion of from Kelvin to Fahrenheit.
        """
        expected = decimal.Decimal(80.33)
        returned = conversions.kelvin_to_fahrenheit(300)
        self.assertEqual(returned, expected, msg='Error. Measurement is ',
                                                 'incorrect.')
                                

    def Tests_K_C(self):
        """ Tests the conversion of from Kelvin to Celcius.
        """
        expected = decimal.Decimal(-273.15)
        returned = conversions.kelvin_to_celcius(0)
        self.assertEqual(returned, expected, msg='Error. Measurement is ',
                                                 'incorrect.')


if __name__ == '__main__':
    unittest.main()