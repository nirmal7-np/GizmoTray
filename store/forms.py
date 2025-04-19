from django import forms
from allauth.account.forms import LoginForm, SignupForm
from .models import Feedback

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-input rounded-md w-full px-4 py-2 border'
            })

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-input rounded-md w-full px-4 py-2 border'
            })

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['emoji', 'email', 'comment']
        widgets = {
            'emoji': forms.RadioSelect(choices=[
                ('😠', '😠'), ('😕', '😕'), ('😐', '😐'), ('😊', '😊'), ('😍', '😍')
            ]),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Your Feedback'}),
        }
