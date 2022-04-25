# header
# title
# date
# name
#


from users import UserCollection
import main
from unittest import TestCase


#main tests
class TestInitUser(TestCase):

    def test_init_user_collection(self):
        #test that it was instatiated?
        #expect an instatiated object which has a database/empty dictionary
        expected = {}
        # actual = main.init_user_collection()
        # message = 'test'
        self.assertEqual(expected, main.init_user_collection().database)
        # self.assertIsInstance(expected, actual, message)

class TestInitStatus(TestCase):

    def test_init_status_collection(self):
        expected = {}
        self.assertEqual(expected, main.init_status_collection().database)

class TestLoadUsers(TestCase):

    def test_load_users(self):
        # csv --> UserCollection
        # users = {}
        #

class TestAddUser(TestCase):

    def test_add_user(self):
        pass