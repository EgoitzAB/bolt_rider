#!/usr/bin/python3
# coding=utf-8

import unittest
from viabilidad_reparto import *
import requests

class Viabilidad_test(unittest.TestCase):

    def SetUp(self):
        url = "https://www.pre.cz/Files/households/electricity/documents-for-download/price-lists/pre-proud-standard-predi/"

    def test_get_url(self):
        url = "https://www.pre.cz/Files/households/electricity/documents-for-download/price-lists/pre-proud-standard-predi/"
        response = download_get_pdf(url)
        self.assertEqual(response, "electricity.pdf")

    def test_download_get_pdf(self):
        url = "https://www.pre.cz/Files/households/electricity/documents-for-download/price-lists/pre-proud-standard-predi/"
        expected = 'electricity.pdf'
        self.assertTrue(download_get_pdf(url))

    def test_eletricity_price(self):
        expected = 1
        self.assertEqual(float(1000)/1000, expected)

    def test_user_afirmative_input(self):
        afirmative = "y"
        self.assertTrue("Y".lower() == afirmative)
        self.assertTrue("y".lower() == afirmative)
        self.assertFalse("Yes".lower() == afirmative)
        #self.assertFalse(45.lower() == afirmative)



#    def test_write(self):
#        download = requests.get(url)
#        with download as r:
#            with open("electricity.pdf", "wb") as f:
#                f.write(r.content)
#                self.assertIsNotNone(f.write(r.content))




if __name__=='__main__':
    unittest.main()
