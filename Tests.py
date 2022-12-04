import unittest

from hamcrest import assert_that, is_, is_not

from CustomMatchers import on_first_change, minimal_brutto_pay
from main import ProductionWorker


class ProductionWorkerTest(unittest.TestCase):

    def test_worker_change_true(self):
        worker = ProductionWorker("Nowak", "Jan", 1, 22)
        worker.set_change_number(1)
        assert_that(worker, is_(on_first_change()))

    def test_worker_change_false(self):
        worker = ProductionWorker("Nowak", "Jan", 2, 22)
        worker.set_change_number(2)
        assert_that(worker, is_not(on_first_change()))

    def test_worker_on_illegal_pay(self):
        worker = ProductionWorker("Nowak", "Jan", 2, 25)
        worker.set_pay_hour(11)
        assert_that(worker, is_not(minimal_brutto_pay()))

    def test_worker_on_legal_pay(self):
        worker = ProductionWorker("Nowak", "Jan", 2, 22)
        worker.set_pay_hour(20)
        assert_that(worker, is_(minimal_brutto_pay()))