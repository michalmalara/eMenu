from django.test import TransactionTestCase
from menu.tasks import send_email
from celery.contrib.testing.worker import start_worker


# class SendEmailTestCase(TransactionTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.celery_worker = start_worker(send_email)
#         cls.celery_worker.__enter__()
#
#     def test_success(self):
#         assert self.task.state == "SUCCESS"