from rest_framework import serializers

from django.contrib.auth.models import User

from django.contrib.auth import login,authenticate

from rest_apis.models import userinfo,profileimage,communication,hobby,skills,chat,projects,achievements

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
#Serializer for profile image

class Profileimageserializer(serializers.ModelSerializer):
    class Meta:
        model = profileimage
        fields = ['profile_image_url']
    def save(self,user):
        image = profileimage(profile_image_url=self.validated_data['profile_image_url'],user=user)
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
        

#Serializers for Projects
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model =  projects
        fields= ['info','starts','ends','status','description']
    def creating(self,user):
        new_project = projects(info=self.validated_data['info'],starts=self.validated_data['starts'],ends=self.validated_data['ends'],status=self.validated_data['status'],description=self.validated_data['description'],user=user)
        new_project.save()
    
        
        
#Serializers for achievements
class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model =  achievements
        fields= ['date','title']
    def creating(self,user):
        new_achieve = achievements(date=self.validated_data['date'],title=self.validated_data['title'],user=user)
        new_achieve.save()
  
#Serializers for Skills
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = skills
        fields = ['name','proficiency']
    def creating(self,user):
        new_skill = skills(name=self.validated_data['name'],proficiency=self.validated_data['proficiency'])
        new_skill.save()
        new_skill.users.add(user)
        new_skill.save()
    def add(self,user):
        try:
            skill = skills.objects.get(name=self.validated_data['name'],proficiency=self.validated_data['proficiency'])
            skill.users.add(user)
            skill.save()
        except Exception as e:
            print(e)
            self.creating(user)
    def delete(self,user):
        try:

            skill = skills.objects.get(name=self.validated_data['name'],proficiency =self.validated_data['proficiency'])
            try:
                skill.users.remove(user)
            except Exception as e:
                print(e)
                raise serializers.ValidationError({"failure":"skill not found for this user"})
        except Exception as e:
            raise serializers.ValidationError({"failure":"skill with given credentials does not exist"})
    def update(self,user,name,proficiency):
        try:

            skill = skills.objects.get(name=name,proficiency =proficiency)
            try:
                skill.users.remove(user)
                try:
                    new_skill= skill.objects.get(name=self.validated_data['name'],proficiency=self.validated_data['proficiency'])
                    new_skill.users.add(user)
                except Exception as e:
                    print(e)
                    self.creating(user)
            except Exception as e:
                print(e)
                raise serializers.ValidationError({"failure":"skill not found for this user"})
        except Exception as e:
            print(e)
            raise serializers.ValidationError({"failure":"skill with given credentials does not exist"})
        


#Serialisers for login


        










            

        
        
    

    






    
       



