from rest_apis.api.views import api_register_user,api_logout_user

from django.urls import path
from  rest_framework.authtoken.views import obtain_auth_token
from rest_apis.api.userinfo_views import api_create_userinfo,api_update_userinfo,api_get_userinfo
from rest_apis.api.profileimageview import api_createprofile,api_updateprofile,api_getprofile
from rest_apis.api.communication_view import api_addcommunication,api_updatecommunication,api_getcommunication
from rest_apis.api.hobby_view import api_addhobby,api_deletehobby,api_gethobby

app_name  = 'rest_apis'
urlpatterns = [

    path('registeruser',api_register_user,name="user_register"),
    path('login',obtain_auth_token,name="user_login"),
    path('logout',api_logout_user,name="user_logout"),

    path('adduserinfo',api_create_userinfo,name="user_create"),
    path('updateuserinfo',api_update_userinfo,name="user_update"),
    path('getuserinfo',api_get_userinfo,name="user_get"),

    path('addprofileimage',api_createprofile,name="profile_create"),
    path('updateprofileimage',api_updateprofile,name="profile_update"),
    path('getprofileimage',api_getprofile,name="profile_get"),

    path('addcommunication',api_addcommunication,name="communication_create"),
    path('updatecommunication',api_updatecommunication,name="communication_update"),
    path('getcommunication',api_getcommunication,name="communication_get"),

    path('addhobby',api_addhobby,name="hobby_create"),
    path('deletehobby',api_deletehobby,name="hobby_delete"),
    path('gethobby',api_gethobby,name="hobby_get"),


    
]