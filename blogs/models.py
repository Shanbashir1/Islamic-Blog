from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Post (models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_posts",
                               null=True, blank=True)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class LikedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title + " liked by " + self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    body = models.TextField()
    blog_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(default=now)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User,
                                   related_name='blogcomments_like',
                                   blank=True)

    class Meta:
        ordering = ['-dateTime']

    def __str__(self):
        return self.user.username + " Comment: " + self.body

    def number_of_likes(self):
        return self.likes.count()
