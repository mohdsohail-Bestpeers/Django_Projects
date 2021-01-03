from django.shortcuts import render
from .models import User, Event, Address, event_photo
from . forms import user_form, event_form, address_form, event_photo_form
from django.urls import reverse

def registration(request):
    context = {
    'UserForm': user_form,
    'EventForm': event_form,
    'AddressForm': address_form,
    'EventPhotoForm': event_photo_form
}
    form=user_form()
    if form.is_valid():
        for Form in form:
            if Form.has_changed and not Form.empty_permitted:
                cd = Form.cleaned_data
                new_fieldName = cd.get('fname')
                old_fieldName = str(cd.get('id'))
                Form.save()
    return render(request, 'registration.html', context)


