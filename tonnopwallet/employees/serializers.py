from rest_framework import serializers
from .models import Employee

class GetEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"



class PostEmployeeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    reg_number = serializers.CharField(required=True)
    department = serializers.CharField(required=True)

    class Meta:
        model = Employee
        exclude = ['joined_at']

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name) 
        instance.last_name = validated_data.get('last_name', instance.last_name) 
        instance.email = validated_data.get('email', instance.email) 
        instance.department = validated_data.get('department', instance.department) 
        instance.department = validated_data.get('department', instance.department) 

        instance.save()
        return instance