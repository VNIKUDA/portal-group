from django.test import TestCase
from .models import Topic, Post
from django.contrib.auth import get_user_model

User = get_user_model()

class ForumTests(TestCase):
    def test_create_topic(self):
        topic = Topic.objects.create(title='Test Topic', description='Test Description')
        self.assertEqual(topic.title, 'Test Topic')

    def test_create_post(self):
        user = User.objects.create_user('testuser', 'test@example.com', 'password')
        topic = Topic.objects.create(title='Test Topic', description='Test Description')
        post = Post.objects.create(topic=topic, author=user, content='Test Content')
        self.assertEqual(post.content, 'Test Content')
