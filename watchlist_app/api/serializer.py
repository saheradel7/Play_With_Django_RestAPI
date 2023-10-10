from rest_framework import serializers
from watchlist_app.models import Movie

# # validators
# def name_length(value):
#     if len(value)<3:
#         raise serializers.ValidationError("Name must be at least 3 characters")
#     return value
#region serializer
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators = [name_length])
#     description =serializers.CharField()
#     active =serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     # field level validation
#     # def validate_name(self, value):
#     #     if len(value)<3:
#     #         raise serializers.ValidationError("Name must be at least 3 characters")
#     #     return value
    
    
#     # Object level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description must be different")
#         return data
    
    #endregion
    
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
    # field level validation
    def validate_name(self, value):
        if len(value)<3:
            raise serializers.ValidationError("Name must be at least 3 characters")
        return value
    
    
    # Object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and Description must be different")
        return data

