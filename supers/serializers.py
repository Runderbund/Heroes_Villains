from rest_framework import serializers
from .models import Super, SuperType

class SuperSerializer(serializers.ModelSerializer):
    super_type = serializers.SlugRelatedField(
        queryset=SuperType.objects.all(),
        slug_field='type'
     )
    # Allows for foreign key to be passed as a string instead of an id integer
    # (We didn't cover slug fields in the course, so there may be a different way to do this, but this does seem to work. I'm curious if there's a better way to do this.)

    class Meta:
        model = Super
        fields = ['name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type']
