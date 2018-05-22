"""
CracklePop program for Recurse School Application, 5/22/2018

Instructions:
Write a program that prints out the numbers 1 to 100 (inclusive).
If the number is divisible by 3, print Crackle instead of the number.
If it's divisible by 5, print Pop. If it's divisible by both 3 and 5,
print CracklePop. You can use any language.
"""


class CracklePop(object):
    def __init__(self, min=1, max=100):
        """Min is lowest input, Max is highest input."""
        self.min = min
        self.max = max
        self.values = []
        self.__calculate_values()

    def __calculate_values(self):
        """Calculate all self.values for instance."""
        for i in xrange(self.min, self.max + 1):
            self.values.append(
                self.__value_for(i)
            )


    def __value_for(self, num):
        """Returns value for a specific input number/value."""
        if not num % 3 and not num % 5:
            return 'CracklePop'
        elif not num % 5:
            return 'Pop'
        elif not num % 3:
            return 'Crackle'
        return num

if __name__ == "__main__":
    print(CracklePop().values)
