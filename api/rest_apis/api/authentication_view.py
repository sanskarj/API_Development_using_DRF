from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from rest_apis.api.serializers import  Registeruser
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def api_register_user(request):
    serial = Registeruser(data=request.data)
    data = {}
    new_list = []
    if serial.is_valid():
        new_user = serial.save()
        data['response'] = "user registered successfully"
        data['email'] = new_user.email
        data['username'] = new_user.username
        data['token'] = Token.objects.get(user=new_user).key
        new_list.append(data)
        
    else:
        data = serial.errors
        new_list.append(data)
    return Response(new_list)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def api_logout_user(request):
    logout(request)
    data  = {}
    data["success"] = "user logged out successfully"
    return Response(data=[data])

    








 



        


 
    



