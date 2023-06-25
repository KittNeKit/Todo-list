from django.test import TestCase
from django.utils import timezone

from Task.forms import TaskForm


class FormTests(TestCase):
    def test_create_correct_deadline_date(self):
        form_data = {
            "content": "Testing",
            "deadline_date": timezone.now() + timezone.timedelta(days=1)
        }
        form = TaskForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_create_deadline_date_in_the_past(self):
        form_data = {
            "content": "Testing 2",
            "deadline_date": timezone.now() + timezone.timedelta(days=-3),
        }

        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())