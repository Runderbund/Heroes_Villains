from django.db import models

# Create your models here.
class SuperType(models.Model):
    super_type = models.CharField(max_length=255)
    # Directions are unclear, and "type" is a reserved keyword

#As a developer, I want to create a SuperType model in a “super_types” app. 
#Property names must be in snake_case and match the following exactly! 
#   type – CharField 
