from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from rest_apis.api.serializers import  Registeruser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_apis.api.serializers import HobbySerializer
from rest_apis.models import hobby

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_add_hobbies(request):
    errors=[]
    for new_hob in request.data['hobbies']:
        serial  = HobbySerializer(data=new_hob)
        if serial.is_valid():
            serial.save(request.user)
        else:
            errors.append({new_hob['name']:serial.errors})
    if len(errors)==0:
        return Response([{"success" : "new hobbies are created successfully"}],status=status.HTTP_200_OK)
    else:
        return Response([{"failure":errors}],status=status.HTTP_206_PARTIAL_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_hobbies(request):
   hobby_list =[]
   try:
       hobbies = hobby.objects.filter(users=request.user)
       for h in list(hobbies):
           hobby_list.append({"name":h.name,"id":h.id})
       return Response(hobby_list,status=status.HTTP_200_OK)
   except:
       return Response([{"failure":"User with given id doesn't have any hobby. try adding one"}],status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_delete_hobbies(request):
    for id in request.data['ids']:
        h = hobby.objects.get(id=id)
        h.users.remove(request.user)
    return Response([{"success" : "User is removed from the hobbies with given ids"}],status=status.HTTP_200_OK)


    




    




        

    
  
            
       


        
        

    
    



  