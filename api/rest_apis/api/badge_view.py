from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from rest_apis.api.serializers import  BadgeSerializer
from rest_framework.authtoken.models import Token
from rest_apis.models import badge

from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_add_badge(request):
    serial = BadgeSerializer(data=request.data)
    if(serial.is_valid()):
        serial.create(request.user)
        return Response([{"success" : "badge added"}],status=status.HTTP_200_OK)
    else:
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_delete_badge(request,title):
    try:
        medal = badge.objects.get(title=title)
        medal.delete()
        return Response([{"success":"Badge deleted"}])
    except:
        return Response({"failure":"Badge with given title doesn't exist"})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_badge(request):
    try:

        badges = badge.objects.filter(user=request.user)
        serial = BadgeSerializer(badges,many=True)
        return Response(serial.data)
    except:
        return Response([{"failure":"user doesn't have any badges yet"}],status=status.HTTP_400_BAD_REQUEST)









