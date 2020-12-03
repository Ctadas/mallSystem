from rest_framework import serializers
from UserManagement.models import User

class UserSerializers(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['id','nickname','phone']
