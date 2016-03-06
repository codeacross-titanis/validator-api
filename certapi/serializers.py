from rest_framework import serializers

from .models import Student, Provider, Badge


class BadgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Badge
        fields = ('id', 'name', 'completed_date', 'student',
                  'is_validated', 'validated_at', 'validated_by',
                  'logo', 'description')


class StudentSerializer(serializers.ModelSerializer):
    badge_set = BadgeSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'email', 'badge_set')


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('id', 'name', 'email', 'logo', 'url')
