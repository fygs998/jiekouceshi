import unittest
class TESTLlianxi(unittest.TestCase):

    def test_01_add(self):
        print(111111111)
        a = 1
        b = 2
        c= 1+2
        self.assertEqual(c,3)

    def test_02_multiply(self):
        print(22222222222222)
        """注释"""
        a = 1
        b = 2
        c = a*b
        self.assertEqual(c,5)

if __name__=="__main__":
    unittest.main()

