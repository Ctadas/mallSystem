from django.shortcuts import render
from rest_framework import viewsets
from UserManagement.models import User
from django.contrib.auth import authenticate, login, get_user_model
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

import requests as httprequests
import os
import binascii

class WXLoginView(APIView):
	
	def get_WXopenid(self,code):
		url ='https://api.weixin.qq.com/sns/jscode2session'
		#code = json.loads(request.body.decode()).get('code')
		appid = ''
		secret = ''
		params = {
			'appid':appid,
			'secret':secret,
			'js_code':code,
			'grant_type':'authorization_code'
		}
		return_request = httprequests.get(url,params)

		openid = return_request.json()['openid']

		return openid

	def get_token(self,user):
		refresh = RefreshToken.for_user(user)
		return {
			'refresh': str(refresh),
			'access': str(refresh.access_token),
		}

	def get(self,request):

		openid = self.get_WXopenid(request.query_params.get('code', None))

		try:
			user = authenticate(**{'wx_open_id' : openid})
		except ValidationError as e:
			user = None

		if user != None:
			token = self.get_token(user)
			return Response({
				'token':token,
			})

		else:
			return Response({
				'return_type':'faile',
				'token':{}
			})

		
	def post(self,request):
		code = request.data.get('code', None)
		if code:
			openid = self.get_WXopenid(code)
		else:
			return Response({
					'msg':'没获取到用户的code'
				},status=status.HTTP_404_NOT_FOUND)

		try:
			user = authenticate(**{'wx_open_id' : openid})
		except ValidationError as e:
			user = None

		if user != None:
			token = self.get_token(user)
			return Response({
				'token':token,
			})

		else:
			random_user_name = 'user:%s'%binascii.hexlify(os.urandom(6)).decode()
			random_password = 'user:%s'%binascii.hexlify(os.urandom(6)).decode()
			try:
				user = User.objects.create_user(username = random_user_name,password = random_password,wx_open_id=openid )
				token = self.get_token(user)
				return Response({
					'token':token,
				})
			except Exception as e:
				return Response({
					'errmsg':e
				},status=status.HTTP_404_NOT_FOUND)
		

		