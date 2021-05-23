import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_emp = Employee('Artem','Khaimov',2500)

    def test_give_default_raise(self):
        self.my_emp.give_raise()
        self.assertEqual(self.my_emp.myraise,7500)

    def test_give_custom_raise(self):
        self.my_emp.give_raise(3500)
        self.assertEqual(self.my_emp.myraise,6000)


if __name__ == '__main__':
    unittest.main()