from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserChangeForm


User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')


        if username and password:
            user = authenticate(username=username,password=password)

            if not user:
                raise forms.ValidationError("This user does not exist.")
            if not user.check_password(password):
                raise forms.ValidationError("Wrong Password.")
            if not user.is_active:
                raise forms.ValidationError("user is not active")

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterationForm(forms.ModelForm):
    email = forms.EmailField(label="Email Adress")

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput,label="Confirm Password")
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password', 'password2']



    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        email = self.cleaned_data.get('email')

        if password != password2:
            raise forms.ValidationError("Password did not matches.")

        email_qs = User.objects.filter(email=email)

        if email_qs.exists():
            raise forms.ValidationError("Email already exists.")

        return super(UserRegisterationForm, self).clean(*args, **kwargs)

class ProfileEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']