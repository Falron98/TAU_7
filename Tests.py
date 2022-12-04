import unittest

from assertpy import assert_that

from main import Car
from CustomMatchers import is_legal_value, not_int


class CarTest(unittest.TestCase):

    def setUp(self):
        self.temp = Car(2010, "VW")

    def test_Car_IsNotEmpty(self):
        assert_that(self.temp).is_not_none()

    def test_Car_BrakeShouldReturn0(self):
        self.temp.brake()
        assert_that(self.temp.get_speed()).is_legal_value()

    def test_Car_AccelerateShouldReturn5(self):
        self.temp.accelerate()
        assert_that(self.temp.get_speed()).is_equal_to(5)

    def test_Car_AttributesNotNone(self):
        assert_that(self.temp).is_not_none()

    def test_Car_WrongAttribute(self):
        assert_that("string").is_not_int()

    def test_Car_getSpeedGreaterThanMinus(self):
        assert_that(self.temp.get_speed()).is_greater_than(-1)

    def test_Car_getSpeedIsNotLessThan0(self):
        assert_that(self.temp.get_speed()).is_not_in(-5,-4,-3,-2,-1)

    def tearDown(self):
        self.temp = None
