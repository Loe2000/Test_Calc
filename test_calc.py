import unittest
import calc

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual (calc.add(1,3), 4)
    def test_add(self):
        self.assertEqual (calc.add(12,37), 49)
    

class testCaseSub(unittest.TestCase):
    def test_sub(self):
        self.assertEqual (calc.sub(3,7), -4)
    def test_sub(self):
        self.assertEqual (calc.sub(9,4), 5)
    
class testCaseMult(unittest.TestCase):
    def test_mult(self):
        self.assertEqual (calc.mult(6,5), 30)
    def test_mult2(self):
        self.assertEqual (calc.mult(2,7), 14)

class testCaseDiv(unittest.TestCase):
    def test_div(self):
        self.assertEqual (calc.div(10,5), 2)
    def test_div2(self):
        self.assertEqual (calc.div(12,2), 6)
    

if __name__ == "__main__":
    unittest.main()




