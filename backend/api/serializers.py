from rest_framework.serializers import ModelSerializer
from .models import *

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

        
class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"