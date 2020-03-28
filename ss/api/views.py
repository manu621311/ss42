from rest_framework import generics
# from permissions import IsAuthenticatedOrCreate
# from .serializers import
from .serializers import SocialSerializer
from django.http import JsonResponse
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from requests.exceptions import HTTPError

from social_django.utils import load_strategy, load_backend
from social_core.backends.oauth import BaseOAuth2
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings

# google log in imports
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from social_core.exceptions import MissingBackend, AuthTokenError, AuthForbidden
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
# class SignUp(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = SignUpSerializer
#     permission_classes = (IsAuthenticatedOrCreate,)
@method_decorator(csrf_exempt, name='dispatch')
class SocialLoginView(generics.GenericAPIView):
    """Log in using facebook"""
    serializer_class = SocialSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Authenticate user through the provider and access_token"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        provider = serializer.data.get('provider', None)
        strategy = load_strategy(request)

        try:
            backend = load_backend(strategy=strategy, name=provider,
            redirect_uri=None)

        except MissingBackend:
            return Response({'error': 'Please provide a valid provider'},
            status=status.HTTP_400_BAD_REQUEST)
        try:
            if isinstance(backend, BaseOAuth2):
                access_token = serializer.data.get('access_token')
            user = backend.do_auth(access_token)
        except HTTPError as error:
            return Response({
                "error": {
                    "access_token": "Invalid token",
                    "details": str(error)
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        except AuthTokenError as error:
            return Response({
                "error": "Invalid credentials",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            authenticated_user = backend.do_auth(access_token, user=user)

        except HTTPError as error:
            return Response({
                "error":"invalid token",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)

        except AuthForbidden as error:
            return Response({
                "error":"invalid token",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)

        if authenticated_user and authenticated_user.is_active:
            #generate JWT token
            login(request, authenticated_user)
            data={
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )}

            curr_user = User.objects.filter(email=authenticated_user.email)[0]
            index = authenticated_user.email.index('@')
            curr_user.username = authenticated_user.email[:index]
            curr_user.save()
            #customize the response to your needs
            response = {
                "email": authenticated_user.email,
                "username":curr_user.username,
                "token": data.get('token')
            }
            return Response(status=status.HTTP_200_OK, data=response)

class GoogleView(APIView):
    def post(self, request):
        payload = {'access_token': request.data.get("token")}  # validate the token
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)

        # create user if not exist
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            user = User()
            user.username = data['email']
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.save()

        # token = RefreshToken.for_user(user)  # generate token without username & password

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        response = {}
        response['username'] = user.username
        response['access_token'] = str(token)
        # response['refresh_token'] = str(token)
        return Response(response)
