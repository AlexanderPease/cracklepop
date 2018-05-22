"""
CracklePop program for Recurse School Application, 5/22/2018

Instructions:
Write a program that prints out the numbers 1 to 100 (inclusive).
If the number is divisible by 3, print Crackle instead of the number.
If it's divisible by 5, print Pop. If it's divisible by both 3 and 5,
print CracklePop. You can use any language.
"""
import unittest


class CracklePop(object):
    def __init__(self, min=1, max=100):
        """Min is lowest input, Max is highest input."""
        self.min = min
        self.max = max

    def output(self):
        """Returns a list of all outputs."""
        output = []
        for i in xrange(self.min, self.max + 1):
            output.append(self.value_for(i))
        return output

    def value_for(self, num):
        """Returns value for a specific input."""
        if not num % 3 and not num % 5:
            return 'CracklePop'
        elif not num % 5:
            return 'Pop'
        elif not num % 3:
            return 'Crackle'
        return num


class TestCracklePop(unittest.TestCase):
    def __init__(self):
        self.test = CracklePop()

    def test_sample_values(self):
        """Spot check known values."""
        self.assertTrue(self.test.value_for(3) == 'Crackle')
        self.assertTrue(self.test.value_for(20) == 'Pop')
        self.assertTrue(self.test.value_for(45) == 'CracklePop')

    def test_divisible_by_3(self):
        """No values should be divisible by 3."""
        for value in self.test.output():
            if isinstance(value, int):
                self.assertTrue(value % 3)

    def test_divisible_by_5(self):
        """No values should be divisible by 3."""
        for value in self.test.output():
            if isinstance(value, int):
                self.assertTrue(value % 5)


if __name__ == "__main__":
    print(CracklePop().output())
