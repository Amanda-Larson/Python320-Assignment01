"""
# Title: test_user_status
# Purpose: to test user_status.py
# Who: ALarson
# What/When: 4/24/2022 - started assignment
#
"""

import user_status as us
from unittest import TestCase
# import mock

# This tests if an object was instantiated...it works but is not the correct test
# class TestUserStatus(TestCase):
#     @mock.patch("user_status.UserStatus")
#     def test_user_status_called(self, mock_user_status):
#         mock_user_status.assert_called_with()


class TestUserStatusCollection(TestCase):
    """This class will test methods in UserStatusCollection class"""

    def test_user_status_collection(self):
        """This will test that the UserStatusCollection class creates an empty dict"""
        expected = {}
        self.assertEqual(expected, us.UserStatusCollection().database)

    def test_add_status(self):
        """This will test UserStatusCollection.add_status"""
        status_id = 203
        user_id = 222
        status_text = "Good night!"
        # I think this tests that if add_status is True, the database is not empty
        # If add_status is False, it would not add a status and may be empty
        if us.UserStatusCollection().add_status(status_id, user_id, status_text):
            self.assertIsNotNone(us.UserStatusCollection().database)