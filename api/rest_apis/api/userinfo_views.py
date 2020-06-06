from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from rest_apis.api.serializers import  Registeruser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_apis.api.serializers import Userinfoserializer
from rest_apis.models import userinfo
from rest_framework.views import APIView

class Userinfo(APIView):
    permissions = [permissions.IsAuthenticated]
    def post(self,request):
        serial = Userinfoserializer(data=request.data)
        if serial.is_valid():
            new_user = serial.save(request.user)
            data = {}
            data["success"] = "User's information is saved successfully"
            return Response([data])
        return Response([serial.errors],status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        try:
            person  = userinfo.objects.get(user=request.user)
            person.delete()
            serial = Userinfoserializer(data=request.data)
            if serial.is_valid():
                d= serial.save(request.user)
                return Response([{"Success" : "UserInfo Updated Successfully"}])
            else:
                return Response([serial.errors],status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response([{"failure": "Info for that user is not yet created"}],status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        try:
        
            h = userinfo.objects.filter(user=request.user)
            serial = Userinfoserializer(h,many=True)
            return Response(serial.data)
        except Exception as e:
            print(e)
            data = {}
            data["failure"] = "Information for this user is not found, try creating it via POST"
            return Response([data],status=status.HTTP_404_NOT_FOUND)
        
    


    



    






    
    
    
    








