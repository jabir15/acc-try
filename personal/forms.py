from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(
        label='Name',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'aria-describedby': 'nameHelp',
                'placeholder': 'Enter your name',
            }
        )
    )
    contact_email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'aria-describedby': 'emailHelp',
                'placeholder': 'Enter email',
            }
        )
    )
    content_subject = forms.CharField(
        label='Subject',
        required=False,
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'aria-describedby': 'subjectHelp',
                'placeholder': 'Enter subject',
            }
        )
    )
    content = forms.CharField(
        label='Message',
        required=True,
        widget=forms.Textarea(
            attrs = {
                'class':'form-control',
                'aria-describedby': 'messageHelp',
                'placeholder': 'Enter your message',
                'rows':'4'
            }
        )
    )
