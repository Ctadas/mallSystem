from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.timezone import now

# 用户校验
class UserAuthenticateBackend(ModelBackend):

	def authenticate(self, request=None, password=None, **credentials):

		try:

			credentials = dict((key, value) for key, value in credentials.items() if key in ('username', 'wx_open_id'))
			if len(credentials)==0:
				raise ValidationError(code='required', message='用户名/微信id为空')

			try:
				# 获取用户
				user = get_user_model().objects.get(**credentials)
			except ObjectDoesNotExist as e:
				raise ValidationError(code='not_existed', message='用户名/微信id不存在')

			# 如果是微信id登陆，无需密码
			if credentials.get('wx_open_id'):
				pass
			else:

				# 检查密码
				if not user.check_password(password):
					raise ValidationError(code='incorrect_password', message='密码错误')

			return user

		except ValidationError as e:
			raise e

		except Exception as e:
			raise e
			raise ValidationError(code='unexpected_error', message='未知错误')

