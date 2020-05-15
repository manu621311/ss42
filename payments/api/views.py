import stripe
from django.contrib.auth.models import User
from objects.models import Profile

from objects.api.serializers import ProfileSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from posts.api.permissions import IsAuthorOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY


class HomeView(APIView):

    permission_classes =[IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]
    authentication_classes =(TokenAuthentication,JSONWebTokenAuthentication)

    def get(self, request):
        key = settings.STRIPE_PUBLISHABLE_KEY
        print(request.user.id)
        return render(request, 'home.html', {'key': key, 'id': request.user.id})


class ChargeView(APIView):
    # permission_classes =[IsAuthenticatedOrReadOnly]
    permission_classes = [AllowAny]
    # authentication_classes =(TokenAuthentication,JSONWebTokenAuthentication)

    def post(self, request):
        user_id = request.POST['user_id']
        print(user_id)
        amount = int(request.POST['amount']) * 100
        user = User.objects.get(id=user_id)
        username = user.username
        user_profile = Profile.objects.filter(username=username)[0]

        charge = stripe.Charge.create(
            amount=amount,
            currency='inr',
            description='A Django charge',
            source=request.POST['stripeToken']
        )

        user_profile.Scrapcoins += int(request.POST['amount'])*3
        user_profile.save()

        serializer = ProfileSerializer(user_profile)

        return Response({
            'success': True,
            'profile': serializer.data
        })
