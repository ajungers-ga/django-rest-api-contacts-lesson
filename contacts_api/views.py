from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ContactSerializer
from .models import Contact

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all().order_by('id')
    serializer_class = ContactSerializer

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all().order_by('id')
    serializer_class = ContactSerializer    
    