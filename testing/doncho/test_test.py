from unittest import TestCase, main

from testing.doncho.person import Person

class TestPerson(TestCase):
    FIRST_NAME = 'Doncho'
    LAST_NAME = "Minkov"
    AGE = 19

    @classmethod
    def setUpClass(cls) -> None:
        """
        Runs once before all tests
        :return:
        """
        pass
    def setUp(self) -> None:
        """
        Runs Before each test
        :return:
        """
        pass
    def tearDown(self) -> None:
        '''
           Runs After each test
           :return:
           '''
        pass
    @classmethod
    def tearDownClass(cls):
        '''
        Runs Once After all test
        :return:
        '''
        pass


    def test_fullname__expect_to_be_correct(self):
        person = Person('Doncho', 'Minkov', 19)

        actual_fullname = person.fullname
        expected_fullname = "Doncho Minkov"

        self.assertEqual(expected_fullname, actual_fullname)

    def test_get_info__expect_to_be_correct(self):
        person = Person('Doncho', 'Minkov', 19)

        actual_info = person.get_info()
        expected_info = 'My name is Doncho Minkov and I am 19-years-old'

        self.assertEqual(expected_info, actual_info)

if __name__ == "__main__":
    main()
