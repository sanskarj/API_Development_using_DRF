from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from rest_apis.api.serializers import  Registeruser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_apis.api.serializers import AchievementSerializer
from rest_apis.models import achievements

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_create_achievement(request):
    serial = AchievementSerializer(data=request.data)
    if serial.is_valid():
        serial.save(request.user)
        return Response({"success" : "Achievement has been added"})
    else:
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_delete_achievement(request,title):
    try:
        achieve = achievements.objects.get(title=title,user=request.user)
        achieve.delete()
        return Response({"success":"Achievement deleted successfully"})
    except:
        return Response({"failure":"User doesn't have any achievement with the given title field"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_achievement(request):
    try:
        achieve= achievements.objects.filter(user=request.user)
        serial = AchievementSerializer(achieve,many=True)
        return Response(serial.data)
    except:
        Response({"failure":"User doesn't have any achievement yet. try adding one"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_update_achievement(request,title):
    try:
        achive  = achievements.objects.get(title=title,user=request.user)
        achive.delete()
        serial = AchievementSerializer(data=request.data)
        if serial.is_valid():
            serial.creating(request.user)
            return Response({"Success" : "Achievement Updated Successfully"})
        else:
            return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"failure": "Achievement with given title does not exist for this user"},status=status.HTTP_400_BAD_REQUEST)
        
    
   
    

    

    


    




