
from django.urls import path
from .views import my_profile_view, invites_received_view, profiles_list_view, invite_profiles_list_view

app_name = 'profiles'

urlpatterns = [
    path('my-profile/', my_profile_view, name = 'my_profile'),
    path('my-invites/', invites_received_view, name = 'my_invites'),
    path('all-profiles/', profiles_list_view, name = 'all_profiles'),
    path('to-invite/', invite_profiles_list_view, name = 'invite_profiles'),



]

