from rest_framework import serializers
from django.core.validators import MinLengthValidator
from .models import Employee
from .validators import validate_email


class GetEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"



class PostEmployeeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True,  validators=[MinLengthValidator(
                limit_value=3,
                message="First name must be longer than 3 characters"
            )
        ],)
    last_name = serializers.CharField(required=True,
        validators=[MinLengthValidator(
                    limit_value=3,
                    message="Last name must be longer than 3 characters"
                )
            ])
    email = serializers.EmailField(required=True, validators=[validate_email])
    reg_number = serializers.CharField(required=True, validators=[MinLengthValidator(
                limit_value=5,
                message="Registration keys must be longer than 5 characters"
            )
        ])
    department = serializers.CharField(required=True, 
    validators=[MinLengthValidator(
                limit_value=2,
                message="Department must be longer than 2 characters."
            )
        ])

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