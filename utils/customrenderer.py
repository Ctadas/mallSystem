from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



class customrenderer(JSONRenderer):
	# 重构render方法
	def render(self, data, accepted_media_type=None, renderer_context=None):
		if renderer_context:
			response = renderer_context['response']
			code = 0 if int(response.status_code / 100) == 2 else response.status_code
			msg = 'success'
			if isinstance(data, dict):
				msg = data.pop('msg', msg)
				code = data.pop('code', code)
				data = data.pop('data', data)
			if code != 0 and data:
				if response.data.get('non_field_errors'):
					msg = response.data.get('non_field_errors')
				else:
					msg = data.pop('msg', data)
				data = []
			response.status_code = 200
			res = {
				'code': code,
				'msg': msg,
				'data': data,
			}
			return super().render(res, accepted_media_type, renderer_context)
		else:
			return super().render(data, accepted_media_type, renderer_context)
