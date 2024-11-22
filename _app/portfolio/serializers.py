from rest_framework import serializers
from .models import (
    Blog,
    BlogCategory,
    Comment,
    Education,
    Language,
    Mail,
    Projet,
    Service,
    ServiceDetail,
    Skill,
    SoftSkill,
    Experience,
)


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
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
    category = BlogCategorySerializer(many=True)

    class Meta:
        model = Blog
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class SoftSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()

    class Meta:
        model = SoftSkill
        fields = ["id", "skill"]


class LanguageSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()

    class Meta:
        model = Language
        fields = ["id", "skill"]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class ServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDetail
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    details = ServiceDetailSerializer(many=True)

    class Meta:
        model = Service
        fields = [
            "id",
            "description",
            "details",
            "image",
            "title",
        ]


class ProjetSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)

    class Meta:
        model = Projet
        fields = [
            "id",
            "title",
            "short_description",
            "description",
            "skill",
            "url",
            "github",
        ]
