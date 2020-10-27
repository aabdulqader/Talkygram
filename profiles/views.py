from django.shortcuts import render
from .models import Profile, Relationship
from .forms import ProfileModelForm
from django.views.generic import ListView
from django.contrib.auth.models import User

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




def invite_profiles_list_view(request):
    user = request.user
    queryset = Profile.objects.get_all_profiles_to_invite(user)


    context = {
        'queryset':queryset, 
    }

    return render (request, 'profiles/to_invite_list.html', context)


def profiles_list_view(request):
    user = request.user
    queryset = Profile.objects.get_all_profiles(user)


    context = {
        'queryset':queryset, 
    }

    return render (request, 'profiles/profile_list.html', context)


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    #context_object_name = 'queryset'


    def get_queryset(self):
        queryset = Profile.objects.get_all_profiles(self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        
        rel_rec = Relationship.objects.filter(sender=profile)
        rel_sen = Relationship.objects.filter(receiver=profile)

        rel_receiver = []
        rel_sender = []

        for item in rel_rec:
            rel_receiver.append(item.receiver.user)

        for item in rel_sen:
            rel_sender.append(item.sender.user)

        context["rel_receiver"] = rel_receiver
        context["rel_sender"] = rel_sender
        context["is_empty"] = False
        if len(self.get_queryset()) == 0:
            context['is_empty'] == True
        return context
    
