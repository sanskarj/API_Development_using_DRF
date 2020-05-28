from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from notifications.signals import notify
from rest_apis.api.serializers import  Registeruser
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout,login,authenticate
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
@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def api_login_user(request):
    cred = list(request.data.values())
    if len(cred) ==2:
    
        user  = authenticate(request,username=cred[0],password=cred[1])
        if user is not None:
            login(request,user)
            notify.send(user,recipient=user,verb="This is a notification")
            data = {}
            data['sucess']   = "User logged in successfully"
            data['Key']   = Token.objects.get(user=user).key
            return Response([data],status=status.HTTP_200_OK)
        else:
            return Response([{"failure" :"User with given login credentials does not exist"}],status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response([{"failure" : "Insufficeint or unwanted login credentials"}],status=status.HTTP_400_BAD_REQUEST)
        
 

    

    
    

    








 



        


 
    



