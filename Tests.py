from unittest import TestCase
from hamcrest import assert_that, equal_to

import hamcrest

from hamcrest import *

from main import Employee, ProductionWorker


class TestProductionWorker(TestCase):

    def setUp(self):
        self.temp = ProductionWorker("Kowalski", "Jan", 1, 12)

    def test_True_get_lastname(self):
        assert_that(self.temp.get_lastname(), not_none())

    def test_True_get_firstname(self):
        assert_that(self.temp.get_firstname(), not_none())

    def test_True_get_change_number(self):
        assert_that(self.temp.get_change_number(), is_(1))

    def test_True_get_pay_hour(self):
        assert_that(self.temp.get_pay_hour(), is_(12))

    def test_False_get_pay_hour(self):
        assert_that(self.temp.get_pay_hour(), is_not(11))

    def test_True_set_lastname(self):
        self.temp.set_lastname("Nowak")
        assert_that(self.temp.get_lastname(), is_("Nowak"))

    def test_Fail_set_lastname_NotInt(self):
        assert_that(self.temp.set_lastname(123), raises(Exception))

    def test_True_set_change_number(self):
        self.temp.set_change_number(2)
        assert_that(self.temp.get_change_number(), less_than(3) and greater_than(0))

    def test_Fail_set_change_number_MoreThan2(self):
        assert_that(self.temp.set_change_number(5), raises(Exception))

    def test_True_equal_object(self):
        assert_that(self.temp, equal_to(ProductionWorker("Kowalski", "Jan", 1, 12)))

    def test_Fail_set_pay_hour(self):
        self.temp.set_pay_hour(2.22)
        assert_that(self.temp.get_pay_hour(), is_not(int))

    def tearDown(self):
        self.temp = None
