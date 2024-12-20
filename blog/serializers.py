from rest_framework import serializers
from .models import Blog ,Tag,Category
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=['name','blog']
    def create(self,validated_data):
        instance=self.Meta.model
        tag=instance.objects.create(**validated_data)
        return tag    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category 
        fields=['name']
    def create(self,validated_data):
        category=Category.objects.create(**validated_data)
        return category   


class BlogSerializer(serializers.ModelSerializer):
    Tags=TagSerializer(many=True,required=False)
    Category=CategorySerializer(many=False,required=False)
    class Meta:
        model= Blog
        fields = ['Title','Content','Author','Tags','Category']




    def create(self, validated_data):
        blog=Blog.objects.create(**validated_data)
        return blog
    

    def update(self,instance,validated_data):
        instance.Title=validated_data.get('Title',instance.Title)
        instance.Content=validated_data.get('Content',instance.Content)
        instance.Author=validated_data.get('Author',instance.Author)
        instance.save()
        return instance