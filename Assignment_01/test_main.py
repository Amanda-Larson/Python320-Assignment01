# header
# title
# date
# name
#


from unittest import TestCase
import main



# main tests
class TestInitUser(TestCase):
    """This will test the user collection __init__ and that it
    creates an empty database/dictionary"""

    def test_init_user_collection(self):
        """This will test the user collection __init__ and that it
        creates an empty database/dictionary
        """
        # test that it was instantiated?
        # expect an instantiated object which has a database/empty dictionary
        expected = {}
        # actual = main.init_user_collection()
        # message = 'test'
        self.assertEqual(expected, main.init_user_collection().database)
        # self.assertIsInstance(expected, actual, message)


class TestInitStatus(TestCase):
    """
    This will test the status collection __init__ and that it creates an
    empty database/dictionary
    """

    def test_init_status_collection(self):
        """This will test the status collection __init__ and that it creates
        an empty database/dictionary"""
        expected = {}
        self.assertEqual(expected, main.init_status_collection().database)


class TestMainUserFunctions(TestCase):
    """This class will test the functions re: users in main.py"""

    def setUp(self) -> None:
        user_id = 225
        email = 'email@email.com'
        user_name = 'Amanda'
        user_last_name = 'Larson'

        self.load_users = main.load_users(filename='accounts.csv')
        self.save_users = main.save_users(filename='accounts.csv')
        self.add_user = main.add_user(user_id, email, user_id, user_last_name)
        self.update_user = main.update_user(user_id, email, user_name, user_last_name)
        self.delete_user = main.delete_user(user_id)
        self.search_user = main.search_user(user_id)

    def test_load_users(self):
        """This will test loading users"""

    def test_save_users(self):
        """This will test saving users to file"""

    def test_add_users(self):
        """This will test adding a new user"""

    def test_update_users(self):
        """This will test updating a user"""

    def test_delete_users(self):
        """This will test deleting a user"""

    def test_search_users(self):
        """This will test searching for a user"""

    def tearDown(self) -> None:
        pass


class TestMainStatusFunctions(TestCase):
    """This class will test the functions re: status in main.py"""

    def setUp(self) -> None:
        status_test = 'Good morning, Starshine!'
        user_id = 225
        status_id = 100

        self.load_status_updates = main.load_status_updates(filename='status_updates.csv')
        self.save_status_updates = main.save_status_updates(filename='status_updates.csv')
        self.add_status = main.add_status(user_id, status_id, status_test)
        self.update_status = main.update_status(status_id, user_id, status_test)
        self.delete_status = main.delete_status(status_id)
        self.search_status = main.search_status(status_id)

    def test_load_status_updates(self):
        """This will test loading status updates from file"""

    def test_save_status_updates(self):
        """This will test saving status updates to file"""

    def test_add_status(self):
        """This will test adding a status"""

    def test_update_status(self):
        """This will test updating a status"""

    def test_delete_status(self):
        """This will test deleting a status"""

    def test_search_status(self):
        """This will test searching for a status"""
