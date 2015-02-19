from django import forms
from django.forms import ModelForm
from photo.models import Photographer , Style
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _




class SexyModelForm(forms.ModelForm):
    error_css_class = 'class-error'
    required_css_class = 'class-required'
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        # adding css classes to widgets without define the fields:
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        	
    def as_div(self):
        return self._html_output(
            normal_row = u'<div%(html_class_attr)s>%(label)s %(field)s %(help_text)s %(errors)s</div>',
            error_row = u'<div class="error">%s</div>',
            row_ender = '</div>',
            help_text_html = u'<div class="hefp-text">%s</div>',
            errors_on_separate_row = False)

class AddStyleForm(SexyModelForm):

 
    class Meta:
        model = Style
        fields =('style_work',)

class UserCreationForm(SexyModelForm):
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
 
   
    first_name = forms.RegexField(label=_("first_name"), max_length=30,
        regex=r'^[\w.@+-]+$',
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},widget=forms.TextInput(attrs={'placeholder':'Имя'}))

    second_name = forms.RegexField(label=_("second_name"), max_length=30,
        regex=r'^[\w.@+-]+$',
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},widget=forms.TextInput(attrs={'placeholder':'Фамилия'}))
 

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':_(u'E-mail')}))
    
    sity = forms.RegexField(label=_("sity"), max_length=30,
        regex=r'^[\w.@+-]+$',
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},widget=forms.TextInput(attrs={'placeholder':'Город'}))
 
   
    password1 = forms.CharField(label=_(u'Password'),widget=forms.PasswordInput(attrs={'placeholder': _(u'Password')}))
    password2 = forms.CharField(label=_(u'Password confimation'),widget=forms.PasswordInput(attrs={'placeholder': _(u'Password confimation')}))
    class Meta:
        model = Photographer
        fields = ( 'email','first_name','second_name','sity')

   

    def clean_password(self):    
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1!=password2:
        	raise forms.ValidationError("Password don't match")
        return password2
    def save(self, commit = True):
        Photographer = super(UserCreationForm, self).save(commit=False)
        Photographer.set_password(self.cleaned_data["password1"])
        if commit:
            Photographer.save()
        return Photographer



class UserChangeForm(SexyModelForm):


    first_name = forms.RegexField(label=_("first_name"), max_length=30,
        regex=r'^[\w.@+-]+$',
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},widget=forms.TextInput(attrs={'placeholder':'Имя'}))

    second_name = forms.RegexField(label=_("second_name"), max_length=30,
        regex=r'^[\w.@+-]+$',
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},widget=forms.TextInput(attrs={'placeholder':'Фамилия'}))
 

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':_(u'E-mail')}))
    
    sity = forms.RegexField(label=_("sity"), max_length=30,
        regex=r'^[\w.@+-]+$',
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},widget=forms.TextInput(attrs={'placeholder':'Город'}))
 
   

    date_birth = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Дата Рождения'}),required=False)

   
    class Meta:
        model = Photographer
        fields = ( 'email','first_name','second_name','sity','about','date_birth')


    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        Photoger = self.fields.get('user_permissions', None)
        if Photoger is not None:
            Photoger.queryset = f.queryset.select_related('content_type')






