from rest_framework import serializers

from .models import (
    BlogPost,
    BlogCategory,
    BlogPostComment,
    LifeEvent,
    Mail,
    Project,
    Resume,
    Service,
    Skill,
)


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = BlogPostComment
        fields = "__all__"

    def get_replies(self, obj):
        replies = obj.replies.all().order_by("creation_date")
        serializer = CommentSerializer(
            replies, many=True, read_only=True, context=self.context
        )
        return serializer.data


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    categories = BlogCategorySerializer(many=True)

    class Meta:
        model = BlogPost
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class LifeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeEvent
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    details = SkillSerializer(many=True)

    class Meta:
        model = Service
        fields = [
            "id",
            "description",
            "details",
            "image",
            "title",
        ]


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "short_description",
            "description",
            "skills",
            "url",
            "github",
        ]
