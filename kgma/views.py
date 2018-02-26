from . models import Kgma
from . serializers import KgmaSerializer
from rest_framework import generics

class KgmaList(generics.ListCreateAPIView):
    queryset = Kgma.objects.all()
    serializer_class = KgmaSerializer

class AboutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kgma.objects.all()
    serializer_class = KgmaSerializer