from rest_framework import serializers
from .models import Super, SuperType

class SuperSerializer(serializers.ModelSerializer):
    super_type = serializers.SlugRelatedField(
        queryset=SuperType.objects.all(),
        slug_field='type'
     )

    class Meta:
        model = Super
        fields = ['name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type']
