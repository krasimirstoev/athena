# Introduction

**Athena** is an kinda advanced Django-based Blog System designed to provide a seamless experience for creating, managing, and engaging with blog content. With this README i will try to provide a comprehensive guide to the system's features, setup, configuration, and usage.

Also **Athena** is a nostalgic glimpse to the days before WordPress became the pig we're using now. The days we just blogging to say the world what we think or share our eureka moments.

# Features

## Blog posts

**Title**: Every blog post features a prominent title.

**Subtitle**: An optional subtitle to provide additional context or a summary of the post.

**Content**: Rich text content supported by CKEditor 5, allowing for detailed and formatted posts.

**Post Time**: Automatically captured when a post is published.

**Category**: Posts can be categorized for better organization and navigation.

**Slug**: Custom URLs for every blog post for better SEO and user-friendly links.

## Comment System

- **Name**: The name of the commenter.
- **Email**: Commenter's email address, used for Gravatar integration and not publicly displayed.
- **Website**: An optional field for the commenter’s website.
- **Comment**: The main content of the comment.
- **IP Address**: Captured for administrative purposes and displayed only in the admin panel.
- **Gravatar Integration**: Automatically displays the Gravatar associated with the commenter’s email.

**Moderation**:
- Comments from new email addresses are held for moderation.
- Once a comment from an email is approved, future comments from the same email are published automatically.

## Pages

- **Dynamic Navigation**: New pages automatically appear in the navigation bar.
- **Management**: Add, edit, and delete pages via the admin interface.
- **Fields**: Title, Body (using CKEditor 5), Date, and Slug.

## RSS Feeds

- **Posts RSS Feed**: Users can subscribe to the latest blog posts.
- **Comments RSS Feed**: Users can subscribe to the latest comments on the blog.
- **Benefits**:
    - Keeps subscribers updated with the latest content.
    - Enhances SEO by allowing search engines to discover and index new content quickly.

# Setup and Configuration
## Prerequisites
```
Python 3.9 or later
Django 3.x or later
CKEditor 5
```
## Installation

**Clone the Repository:**

``git clone https://github.com/krasimirstoev/athena``
``cd athena``

**Create a Virtual Environment (optional):**

``python -m venv venv``
``source venv/bin/activate``  

**Install Dependencies:**

``pip install -r requirements.txt``

**Run Migrations:**

``python manage.py makemigrations``
``python manage.py migrate``

**Create a Superuser:**

``python manage.py createsuperuser``

Run the application/server depends on what system you are using.

## Configuration

- **Admin Interface**: Access the admin interface at /admin to manage posts, comments, categories, and pages.
- **Site Settings**: Configure site-wide settings such as blog name, subtitle, and posts per page through the admin interface.

# Detailed Features
## Blog Post Management

**Athena** allows you to create detailed posts with titles, optional subtitles, rich text content, and categorization. Each post automatically captures the posting time and generates a SEO-friendly slug for easy access and sharing.

## Comment System
Our comment system is designed to facilitate user engagement while maintaining control over the content:

**Moderation**: New commenters are subject to moderation to prevent spam. Once a commenter is approved, their future comments are published immediately.

**Gravatar Integration**: By connecting email addresses to Gravatar, commenter avatars are displayed.

## Dynamic Pages

**Pages** are a versatile feature of our system, allowing you to create static content that appears in the site's navigation automatically. This is ideal for about pages, contact information, and other static resources.

## RSS Feeds

RSS feeds are provided for both posts and comments, keeping your audience engaged with the latest content and discussions:

**Posts RSS Feed**: Keeps users updated with new blog entries.

**Comments RSS Feed**: Keeps users informed about the latest discussions.

## Navigation

The navigation bar dynamically updates to include links to new pages, ensuring that your audience can easily access all parts of your site. This dynamic update happens automatically, requiring no manual intervention after page creation.
Conclusion

Athena is a robust platform designed to cater to all your blogging needs. With its rich feature set, user-friendly interface, and advanced content management capabilities, it provides everything you need to run a successful blog. Whether you're a solo blogger or managing a multi-author site, this system is built to support and grow with you.
