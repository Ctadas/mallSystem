from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class PhoneValidator(RegexValidator):

	def __init__(self, code=None, message=None):
		if not code:
			code = 'invalid'
		if not message:
			message = '非法手机号'

		super().__init__(r'^(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7(?:[01356789]\d{2}|4(?:0\d|1[0-2]|9\d))|9[189]\d{2}|6[567]\d{2}|4[579]\d{2})\d{6}$', code, message)