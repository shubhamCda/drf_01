from rest_framework import serializers
from .models import Person


class PeopleSerializer(serializers.Serializer):
    
    class meta:
        model = Person
        fields = ['name', 'age']  #to include all fields in the model</s>

        # fields = [       # to sets the fields
        #     'name', 'age', 
        # ]
        #exclude  = ['name', 'age']   #to exclude a field
    def create(self, validated_data):
        return Person.objects.create(**validated_data)
        
    # def update(self, instance, validated_data):
    #     """
    #     Override the default `update()` method to support an additional parameter for password hashing.
    #     If the "password" key is present in the input data, hash the password and save it as "hashed_password".
    #     If the "password" key is present in the input data, hash the password and save it as the "password" attribute.
    #     If the "password" key is present in the input data, then we will hash and set it on the instance.
    #     """