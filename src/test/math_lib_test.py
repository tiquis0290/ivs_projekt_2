import sys

import pytest

sys.path.append('./libs')
import calc_mathlib as mathlib

"""@package math_lib
       Tests for float operators
       - test_<operation>_basic - basic tests
       - test_<operation>_limit - limit situation of float
       - test_<operation>_error - test right error values (overflow, invalid inputs)
"""

# TODO desetina cilsa

class TestAdd:
    @pytest.mark.parametrize('testv, result', [((0, 0), 0), ((0, 42), 42), ((24, -42), -18)])
    def test_plus_basic(self, testv, result):
        assert mathlib.add(testv[0], testv[1]) == result

    def test_add_limit(self):
        assert mathlib.add(sys.float_info.max/2, sys.float_info.max/2) == sys.float_info.max

    def test_add_error(self):
        with pytest.raises(OverflowError):
            mathlib.add(sys.float_info.max, sys.float_info.max)

class TestSub:

    @pytest.mark.parametrize('testv, result', [((0, 0), 0), ((0, 42), -42), ((24, 42), -18)])
    def test_sub_basic(self, testv, result):
        assert mathlib.sub(testv[0], testv[1]) == result

    def test_sub_limit(self):
        assert mathlib.sub(sys.float_info.max, sys.float_info.max) == 0
        assert mathlib.sub(0, sys.float_info.max) == -sys.float_info.max

    def test_sub_error(self):
        with pytest.raises(OverflowError):
            mathlib.sub(mathlib.sub(0, sys.float_info.max), sys.float_info.max/2)

class TestMul:

    @pytest.mark.parametrize('testv, result', [((0, 0), 0), ((10, 42), 420), ((10.01, 40.02), 404.202), ((10, -42), -420), ((-10, -10), 100)])
    def test_mul_basic(self, testv, result):
        assert mathlib.mul(testv[0], testv[1]) == result

    def test_mul_limit(self):
        assert mathlib.mul(0, sys.float_info.max) == 0
        assert mathlib.mul(-1, sys.float_info.max) == -sys.float_info.max

    def test_mul_error(self):
        with pytest.raises(OverflowError):
            mathlib.mul(3, sys.float_info.max/2)

class TestDiv:

    @pytest.mark.parametrize('testv, result', [((100, 5), 20), ((42, 0.20), 210), ((420, -42), -10), ((-100, -10), 10)])
    def test_div_basic(self, testv, result):
        assert mathlib.div(testv[0], testv[1]) == result

    def test_div_limit(self):
        assert mathlib.div(sys.float_info.max, sys.float_info.max) == 1

    def test_div_error(self):
        with pytest.raises(ZeroDivisionError):
            mathlib.div(42, 0)

class TestFac:

    @pytest.mark.parametrize('testv, result', [(3, 6), (10, 3628800)])
    def test_fac_basic(self, testv, result):
        assert mathlib.fac(testv[0]) == result

    def test_fac_limit(self):
        assert mathlib.fac(0) == 1

    def test_fac_error(self):
        with pytest.raises(ValueError):
            mathlib.fac(-1)
        with pytest.raises(ValueError):
            mathlib.fac(4.2)
        with pytest.raises(OverflowError):
            mathlib.fac(sys.float_info.max/2)

class TestPow:

    @pytest.mark.parametrize('testv, result', [((10, 2), 100), ((10, -1), 0.1), ((4.2, 2), 17.64)])
    def test_pow_basic(self, testv, result):
        assert mathlib.pow(testv[0],testv[1]) == result

    # tohle nevim jestli vubec pujde porovnat
    def test_pow_limit(self):
        assert mathlib.pow(2, 1023) == sys.float_info.max/2
        assert mathlib.pow(0, 0) == 1

    def test_pow_error(self):
        with pytest.raises(ZeroDivisionError):
            mathlib.pow(0, -1)
        with pytest.raises(ValueError):
            mathlib.root(4, 0.5)
        with pytest.raises(OverflowError):
            mathlib.pow(sys.float_info.max/2, 2)
class TestRoot:

    @pytest.mark.parametrize('testv, result', [((100, 2), 10), ((64, 6), 2)])
    def test_root_basic(self, testv, result):
        assert mathlib.root(testv[0], testv[1]) == result

    def test_root_limit(self):
        assert mathlib.root(2, 1/1023) == mathlib.pow(2, 1023)

    def test_root_error(self):
        with pytest.raises(ZeroDivisionError):
            mathlib.root(42, 0)
        with pytest.raises(ValueError):
            mathlib.root(-1, 2)
        with pytest.raises(OverflowError):
            mathlib.root(sys.float_info.max/2, 00.1)

class TestAbs:

    @pytest.mark.parametrize('testv, result', [(42, 42), (0, 0), (-24, 24), (-24.15, 24.15)])
    def test_abs_basic(self, testv, result):
        assert mathlib.abs(testv) == result

    def test_abs_limit(self):
        assert mathlib.abs(sys.float_info.max) == mathlib.abs(-sys.float_info.max)
