from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _

from app.forms.account import UserProfileChangeForm


class UserProfileChangeView(LoginRequiredMixin, View):
    """User profile change view"""

    def get(self, request):
        user = request.user
        form = UserProfileChangeForm(instance=user)
        context = {"form": form}
        return render(request, 'account/profile_settings.html', context)

    def post(self, request):
        form = UserProfileChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(
                self.request,
                messages.INFO,
                _('User profile changed successfully!'),
                extra_tags='info'
            )
            return redirect('profile')
        else:
            context = {
                "form": form,
            }
            return render(request, 'account/profile_settings.html', context)
