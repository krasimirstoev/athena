from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post, Comment

class LatestPostsFeed(Feed):
    title = "Latest Blog Posts"
    link = "/rss/posts/"
    description = "Updates on the latest blog posts."

    def items(self):
        return Post.objects.order_by('-post_time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return reverse('post_detail', args=[item.slug])

class LatestCommentsFeed(Feed):
    title = "Latest Comments"
    link = "/rss/comments/"
    description = "Updates on the latest comments."

    def items(self):
        return Comment.objects.filter(active=True).order_by('-created_on')[:10]

    def item_title(self, item):
        return f"Comment by {item.name} on {item.post.title}"

    def item_description(self, item):
        return item.comment

    def item_link(self, item):
        return reverse('post_detail', args=[item.post.slug]) + f"#comment-{item.id}"
