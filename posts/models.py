from django.db import models

from users.models import User


class Post(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    actuality = models.BooleanField(default=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-actuality', '-created_timestamp')

    def __str__(self):
        return self.name

    @classmethod
    def post_not_actuality(self, user):
        posts = Post.objects.filter(user=user)
        post = posts.first()
        post.actuality = False
        post.save()
        return post
