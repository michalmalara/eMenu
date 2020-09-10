from django.test import TestCase
from menu.tasks import send_email

class SendEmailTestCase(TestCase):

    def testNoError(self):
        result = send_email.delay()
        # self.assertTrue(result.successful())
