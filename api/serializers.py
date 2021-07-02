from rest_framework import serializers
from main.models import *
from users.models import *
from rest_framework.authtoken.models import Token


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style = {'input_type': 'password'}, write_only = True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'password', 'password2']
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }

    def save(self):
        account = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords didn\'t match'})

        account.set_password(password)
        account.save()
        Token.objects.create(user = account)
        return account


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        # name = serializers.ReadOnlyField()

        model = Facility
        fields = ['UserName', 'FullName', 'Password', 'FacilityCode', 'EmployerNo', 'TelephoneNo', 'EmailAddress']
