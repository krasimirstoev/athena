from django.test import TestCase
from blog.forms import CommentForm

class CommentFormTest(TestCase):
    def test_comment_form_valid_data(self):
        form = CommentForm(data={
            'name': 'Test Name',
            'email': 'test@example.com',
            'comment': 'This is a test comment.',
            'web': 'http://example.com',
        })

        self.assertTrue(form.is_valid())

    def test_comment_form_no_data(self):
        form = CommentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # Name, email, and comment are required fields
