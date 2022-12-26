from django.db import models
from django.forms import ModelForm, TextInput, Textarea


# Create your models here.
class Setting(models.Model):
    STATUS ={
        ('True','Evet'),
        ('False','Hayır'),
    }
    title=models.CharField(max_length=150)
    keywords=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    company=models.CharField(max_length=50)
    adress=models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=15)
    smtpserver=models.CharField(blank=True,max_length=20)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon=models.ImageField(blank=True,upload_to='images/')
    facebook=models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    aboutus=models.TextField(blank=True)
    contact = models.TextField(blank=True)
    references = models.TextField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class ContactFormMessage(models.Model):
    STATUS = (
        ('New','New'),
        ('Read','Read'),
    )
    name = models.CharField(blank=True,max_length=20)
    emai = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=20)
    message = models.CharField(blank=True, max_length=255)
    status = models.CharField( max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields =['name','emai','subject','message']
        widgets = {
            'name'  : TextInput(attrs={'class':'input','placeholder':'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'emai': TextInput(attrs={'class': 'input', 'placeholder': 'Emai adress'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Your Message','rows':'5'}),
        }


