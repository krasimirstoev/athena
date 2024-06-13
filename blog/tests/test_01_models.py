from django.test import TestCase
from blog.models import Post, Page, Category

class PostModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.post = Post.objects.create(
            title="Test Post", 
            body="This is a test post.",
            category=self.category
        )

    def test_string_representation(self):
        self.assertEqual(str(self.post), self.post.title)

    def test_post_slug(self):
        self.assertEqual(self.post.slug, 'test-post')

class PageModelTest(TestCase):
    def setUp(self):
        self.page = Page.objects.create(title="Test Page", body="This is a test page.")

    def test_string_representation(self):
        self.assertEqual(str(self.page), self.page.title)

    def test_page_slug(self):
        self.assertEqual(self.page.slug, 'test-page')
