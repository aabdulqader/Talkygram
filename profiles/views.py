from django.shortcuts import render
from .models import Profile, Relationship
from .forms import ProfileModelForm



def my_profile_view(request):

    profile = Profile.objects.get(user=request.user)

    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True
    else:
        form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    



    context =  {
        'profile': profile,
        'form': form,
        'confirm': confirm
    }

     
    return render (request, 'profiles/my_profile.html', context)



def invites_received_view(request):
    profile = Profile.objects.get(user=request.user)
    queryset = Relationship.objects.invitations_received(profile)


    context = {
        'queryset':queryset, 
    }

    return render (request, 'profiles/my_invites.html', context)




def profiles_list_view(request):
    user = request.user
    queryset = Profile.objects.get_all_profiles(user)


    context = {
        'queryset':queryset, 
    }

    return render (request, 'profiles/profile_list.html', context)



def invite_profiles_list_view(request):
    user = request.user
    queryset = Profile.objects.get_all_profiles_to_invite(user)


    context = {
        'queryset':queryset, 
    }

    return render (request, 'profiles/to_invite_list.html', context)


