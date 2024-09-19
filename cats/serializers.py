from rest_framework.serializers import ModelSerializer

from cats.models import Cat


class CatSerializer(ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'
