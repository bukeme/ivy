from django import forms
from .models import Company, CompanyReview,JobApplication
from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests
from django_select2 import forms as s2forms
class CompanyReviewForm(forms.ModelForm):
    class Meta:
        model = CompanyReview
        fields = '__all__'
        #fields = ['notes']
    
    


class JobApplicationCompanyWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontains",
    ]



class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        #fields = '__all__'
        fields = ['company','stage','date_applied']
        widgets = {
            "company": JobApplicationCompanyWidget,
        }

    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.none()

        if 'company' in self.data:
            self.fields['company'].queryset = Company.objects.all()
        elif self.instance.pk:
            self.fields['company'].queryset = Company.objects.all().filter(pk=self.instance.company.pk)
    '''






'''
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name','url']
        widgets = {
            'url': forms.HiddenInput,
        }
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not ' \
                                        'match valid image extensions.')
        return url
    

    def save(self, force_insert=False,force_update=False,commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'

        response = requests.get(image_url)
        image.image.save(image_name,ContentFile(response.content),save=False)
        if commit:
            image.save()
        return image
'''



