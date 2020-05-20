from rest_framework import serializers

from django.contrib.auth.models import User
from rest_apis.models import userinfo,profileimage,communication,hobby,skills,chat

class Registeruser(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type' : 'password'})
    class Meta:
        model = User
        fields = ['username','email','password','password2']
    def save(self):
        new_user = User(username = self.validated_data['username'],
            email = self.validated_data['email'],
        )
        if self.validated_data['password'] !=self.validated_data['password2']:
            raise serializers.ValidationError({'password' : 'passwords must match'})
        else:
            new_user.set_password(self.validated_data['password'])
            new_user.save()
        return new_user
            

#Serializer for user info

class Userinfoserializer(serializers.ModelSerializer):
    class Meta:
        model = userinfo
        fields  = ['name','location','aboutme']
    
    def save(self):
        new_user = userinfo(name=self.validated_data["name"],location=self.validated_data["location"],aboutme=self.validated_data["aboutme"])
        new_user.save()
        return new_user
    def update(self,user):
        curr_user = userinfo.objects.get(user=user)
        data = self.validated_data
        curr_user.name = data["name"]
        curr_user.location   = data["location"]
        curr_user.aboutme = data["aboutme"]
        curr_user.save()
        return curr_user
#Serializer for profile image

class Profileimageserializer(serializers.ModelSerializer):
    class Meta:
        model = profileimage
        fields = ['profile_image_url']
    def save(self,user):
        image = profileimage(profile_image_url=self.validated_data['profile_image_url'],user=user)
        image.save()
        return image
    def update(self,user):
        image = profileimage.objects.get(user=user)
        image.profile_image_url = self.validated_data['profile_image_url']
        image.save()
        return image
#Serializer for communication
class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = communication
        fields = ['medium','medium_url']
    def save(self,user):
        commu_method = communication(medium=self.validated_data['medium'],medium_url=self.validated_data['medium_url'],user=user)
        commu_method.save()
        return commu_method
    def update(self,user):
        try:
            commu = communication.objects.get(medium=self.validated_data['medium'],user=user)
    
            commu.medium = self.validated_data['medium']
            commu.medium_url = self.validated_data['medium_url']
            commu.save()
            return commu
        except:
            raise serializers.ValidationError({self.validated_data['medium']:"User hasn't added this medium as one of its means of communication"})

#Serailizer for hobby
class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = hobby
        fields = ['name','hobby_image_url']
    def save(self,user):
        try:
            req_hobby = hobby.objects.get(name=self.validated_data['name'])
            req_hobby.users.add(user)
            req_hobby.save()
            return req_hobby
        except:
            new_hobby = hobby(name=self.validated_data['name'],hobby_image_url=self.validated_data['hobby_image_url'])
            new_hobby.save()
            new_hobby.users.add(user)
            new_hobby.save()
            return new_hobby
    def delete(self,user):
        try:
            req_hobby = hobby.objects.get(name=self.validated_data['name'])
            try:
                req_hobby.users.remove(user)
            except:
                raise serializers.ValidationError({self.validated_data['name']:'This hobby is either removed or never added by you'})
        except:
            raise serializers.ValidationError({self.validated_data['name']:'This hobby does not exist,(None of the users of this app saved this as one of their hobby)'})
        

            
       
    






    
       



