from django import forms
from django.urls import reverse
from django.utils.safestring import mark_safe
from allauth.account.forms import LoginForm, SignupForm
from django.utils.translation import gettext_lazy as _

from app.models.user import CustomUser


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields["password"].help_text = mark_safe(
            _('<a href="{}">Forgot your password?</a>').format(
                reverse("account_reset_password")
            )
        )
        self.fields["remember"].label=_("RememberMe")


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = mark_safe(
            _('Already have an account? <a href="{}">Login</a>').format(
                reverse("account_login")
            )
        )


class UserProfileChangeForm(forms.ModelForm):
    """User change info form"""

    first_name = forms.CharField(
        max_length=55,
        required=True,
        label=_('FirstName')
    )

    last_name = forms.CharField(
        max_length=55,
        required=True,
        label=_('LastName')
    )

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name")
