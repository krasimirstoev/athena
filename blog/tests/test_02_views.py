from django.test import TestCase
from django.urls import reverse
from blog.models import Post, Page, Category

class PostViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.post = Post.objects.create(
            title="Test Post",
            body="This is a test post.",
            category=self.category
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertTemplateUsed(response, 'post_list.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertTemplateUsed(response, 'post_detail.html')

class PageViewTest(TestCase):
    def setUp(self):
        self.page = Page.objects.create(title="Test Page", body="This is a test page.")

    def test_page_detail_view(self):
        response = self.client.get(reverse('page_detail', args=[self.page.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Page")
        self.assertTemplateUsed(response, 'page_detail.html')
