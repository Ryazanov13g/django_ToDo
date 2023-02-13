from rest_framework import serializers, fields

from posts.models import Post
from users.models import User


class PostSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ('name', 'description', 'created_timestamp', 'updated_timestamp', 'actuality', 'user')
