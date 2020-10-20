from rest_framework import serializers
from .models import Comment


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    reply_to = serializers.PrimaryKeyRelatedField(read_only=True)
    replies = RecursiveField(many=True)

    class Meta:
        model = Comment
        exclude = ['ip', 'browser_info']


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
