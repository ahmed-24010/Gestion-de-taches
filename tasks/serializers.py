from rest_framework import serializers
from .models import Category, Task
class CategoryAhmed(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["nom"]
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    category = CategoryAhmed()
    # category = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='nom'   # on affiche seulement le nom
    # )
    class Meta:
        model = Task
        # fields = '__all__'
        
        fields = ["id" , "titre", "description" , "statut", "date_creation", "category" ]

        