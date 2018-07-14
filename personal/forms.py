from django import forms

class ContactForm(forms.Form):

    contact_name = forms.CharField(
        label='Name',
        max_length=100,
        required=True,
        error_messages={'required': 'Please enter your name'},
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
        error_messages={'required': 'Please enter an email id', 'invalid': 'Please enter a proper email address'},
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'aria-describedby': 'emailHelp',
                'placeholder': 'Enter email',
            }
        ),
        help_text = """<small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>""",
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
        error_messages={'required': 'Please enter a message'},
        widget=forms.Textarea(
            attrs = {
                'class':'form-control',
                'aria-describedby': 'messageHelp',
                'placeholder': 'Enter your message',
                'rows':'4'
            }
        )
    )
    cc_myself = forms.BooleanField(
        label='Send a copy to me',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class':'form-check-input m-2',
            }
        ),
    )
