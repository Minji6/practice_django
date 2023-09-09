from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    def form_valid(self, form): #form_vaild 함수를 통해서 로직을 수행하고 성공적으로 마치면 알아서 success_url에 정의한 페이지로 이동한다.
        temp_profile = form.save(commit=False) # 임시저장
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form) #슈퍼클래스, 즉 부모인 CreateView를 상속

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk}) #self.object가 가르키는 것은 Profile이다.


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk}) #self.object가 가르키는 것은 Profile이다.


