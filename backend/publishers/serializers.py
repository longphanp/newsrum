from rest_framework import serializers
from .models import Publisher, Feed


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'url', 'name', 'logo']

    def create(self, validated_data):
        publisher = Publisher.objects.create(**validated_data)
        publisher.save()
        return publisher

    def update(self, instance, validated_data):
        instance.url = validated_data.get('url', instance.url)
        instance.name = validated_data.get('name', instance.name)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.save()
        return instance


class FeedSerializer(serializers.ModelSerializer):
    publisher_id = serializers.IntegerField()

    class Meta:
        model = Feed
        fields = ['id', 'publisher_id', 'url']
