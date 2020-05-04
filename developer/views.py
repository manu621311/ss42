from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Developers
from django.core.mail import send_mail
from .jwt_functions import jwt_payload_handler, jwt_encode_handler

def get_jwt(user):
    payload = jwt_payload_handler(user)
    return jwt_encode_handler(payload)

class SaveToken(View):
    def get(self, request):
        return render(request, 'developer/test.html')

    def post(self, request):
        ss_email = request.POST.get("scrapshutEmail")
        user = None
        try:
            user = User.objects.get(email=ss_email)
        except:
            return HttpResponse("Email not registered on Scrapshut")
        isTokenGen = 1
        dev = None
        try:
            dev = Developers.objects.get(ssEmail=ss_email)
        except:
            isTokenGen = 0
        
        if isTokenGen:
            dev.token = get_jwt(user)
            dev.save()
            return HttpResponse(f'<h2> Token Updated Successfully </h2>  {dev.token} <br> <h2> Token sent to your registered email. Please check it. </h2>')

        dev = Developers.objects.create(
            dev_name = request.POST.get("name"),
            email = request.POST.get("email"),
            ssEmail = request.POST.get("scrapshutEmail"),
            company = request.POST.get("company"),
            city = request.POST.get("city"),
            country = request.POST.get("country"),
            description = request.POST.get("description"),
            token = get_jwt(user)
        )
        # subject = f'Scrapshut Developer Token Generated Successfully'
        # message = f'Hello, {dev.dev_name}, your Developer Token has been successfully generated: {dev.token}.'
        # sender = %%%%Enter your email%%%%
        # receiver = [dev.email, dev.ssEmail]
        # send_mail(subject, message, sender, receiver, fail_silently=False)
        return HttpResponse(f'<h2> Token Generated Successfully: </h2> {dev.token}   <br> <h2> And sent to your email </h2>')