from django.test import TestCase
from Task.models import Tag, Task


class ModelTests(TestCase):
    def setUp(self) -> None:
        self.tag = Tag.objects.create(name="test tag")
        self.task = Task.objects.create(content="Test task")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), self.tag.name)

    def test_task_str(self):
        self.assertEqual(str(self.task), self.task.content)