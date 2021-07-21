from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label='',max_length=200)
    #check = forms.BooleanField(required=False)



class HispitalForm(forms.Form):
    hospital_name = forms.CharField(label='Hospital name', max_length=100)
    tags = forms.CharField(label='Tags (Enter with #)', max_length=100)
    numSeats = forms.IntegerField(label='Seats Available')
    doctorName = forms.CharField(label='Doctors Available', max_length=1000)