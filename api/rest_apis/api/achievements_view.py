from rest_framework import status,permissions
from rest_framework.response import Response


from rest_apis.api.serializers import  Registeruser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout

from rest_apis.api.serializers import AchievementSerializer
from rest_apis.models import achievements
from rest_framework.views import APIView

class Achievements(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        achievement_list =[]
        try:
            achievements1 = achievements.objects.filter(user=request.user)
            for h in list(achievements1):
                achievement_list.append({"date":h.date,"title":h.title,"description":h.description})
            return Response(achievement_list,status=status.HTTP_200_OK)
        except:
            return Response([{"failure":"User with given id doesn't have any achievement. try adding one"}],status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        serial = AchievementSerializer(data=request.data)
        if serial.is_valid():
            serial.creating(request.user)
            return Response([{"success" : "Achievement has been added"}])
        else:
            return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,title):
        try:
            achieve = achievements.objects.get(title=title,user=request.user)
            achieve.delete()
            return Response([{"success":"Achievement deleted successfully"}])
        except:
            return Response([{"failure":"User doesn't have any achievement with the given title field"}],status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,title):
        try:
            achive  = achievements.objects.get(title=title,user=request.user)
            achive.delete()
            serial = AchievementSerializer(data=request.data)
            if serial.is_valid():
                serial.creating(request.user)
                return Response([{"Success" : "Achievement Updated Successfully"}])
            else:
                return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response([{"failure": "Achievement with given title does not exist for this user"}],status=status.HTTP_400_BAD_REQUEST)


    
        
    
   
    

    

    


    




