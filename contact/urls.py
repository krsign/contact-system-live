
from django.urls import path
from contact.views import index, add_contact_form, update_contact_form, delete_contact_form, about, contact_us_form

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('contact-us', contact_us_form, name='contact-us'),
    path('new-contact', add_contact_form, name='new-contact'),
    path('update/<int:id>', update_contact_form, name='update'),
     path('delete/<int:id>', delete_contact_form, name='delete'),
]
