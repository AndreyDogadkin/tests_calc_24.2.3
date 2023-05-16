from calculatior import Calculator
import pytest


class TestSuite:

    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_subst_success(self):
        assert self.calc.subtraction(self, 2, 1) == 1

    def test_devi_success(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_multi_success(self):
        assert self.calc.multiply(self, 2, 2) == 4
