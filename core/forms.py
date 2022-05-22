from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['placeholder'] = field_name

