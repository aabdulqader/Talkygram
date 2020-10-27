
from django.urls import path
from .views import (
    my_profile_view, 
    invites_received_view, 
    profiles_list_view, 
    invite_profiles_list_view,
    ProfileListView,
    send_invitation,
    remove_from_friends,


)

app_name = 'profiles'

urlpatterns = [
    path('my-profile/', my_profile_view, name = 'my_profile'),
    path('my-invites/', invites_received_view, name = 'my_invites'),
    path('all-profiles/', ProfileListView.as_view(), name = 'all_profiles'),
    path('to-invite/', invite_profiles_list_view, name = 'invite_profiles'),
    path('send-invite/', send_invitation, name = 'send_invite'),
    path('remove-friend/', remove_from_friends, name = 'remove_friend'),

]

