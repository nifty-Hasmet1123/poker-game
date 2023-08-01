import unittest
# import doctest

"""
    There is a cycle called red green refactor cycle.
    Red = In this stage you write a sample test. And you get that test to fail. It has to fail because the code for it doesn't exist yet.
    Green = In this stage the sample test are fully functional and receives no errors from the system.
    Refactor = In this stage this is the part where you improved/clean the code without altering its behaviour.

    Test Driven Development was largely inspired and promoted by American software developer Kent Beck and it exist as one pillar 
    of a software development philosophy or methodology called Extreme Programming or XP. This will increase the chances of delivering 
    better code, which has less bugs and is more stable, is delivered on time or ahead of time and easy to change and to adopt.
"""

class Multiplication():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def __repr__(self):
        return "Multiplication of two numbers which is {} and {}".format(self.number1, self.number2)
    
    def multiply(self):
        return self.number1 * self.number2
        # total = 0
        # for _ in range(self.number1):
        #     total += self.number2
        # return total

    # you can also do this without the init
    # def multiply(self, number1, number2):
    #     return number1 * number2
    
class TestProduct(unittest.TestCase):
    def test_driven_multiplication(self):
        """Test for multiplication of 2 numbers"""

        product = Multiplication(number1 = 3, number2 = 3)
        # product = Multiplication()
        self.assertEqual(
            product.multiply(),
            9
        )

def func():
    return "Magic"

if callable(func): 
    dictionary = {}
    dictionary[func()] = "pass function"

# print(dictionary)
    
if __name__ == "__main__":
    unittest.main() 