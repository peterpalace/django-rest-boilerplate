from django.db import IntegrityError
from django.test import TestCase
from .models import Profile, User


class UserTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        User.objects.create(
            email='mario.rossi@gmail.com',
            password="password",
            first_name="mario",
            last_name="rossi"
        )

    def test_user_create(self):
        self.assertRaises(
            IntegrityError,
            User.objects.create,
            email='lucia.rossi@gmail.com',
            password="password",
        )

    def test_profile_created(self):
        mario = User.objects.get(email="mario.rossi@gmail.com")
        self.assertEqual(
            mario.email, "mario.rossi@gmail.com"
        )
        self.assertIsNotNone(
            mario.profile
        )

    def test_profile_slug_created(self):
        mario = User.objects.get(email="mario.rossi@gmail.com")
        self.assertIsNotNone(
            mario.profile.slug
        )
        self.assertIsNot(
            mario.profile.slug,
            ""
        )
