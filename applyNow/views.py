from . models import Apply
from . serializers import ApplySerializer
from rest_framework import generics

class ApplyList(generics.ListCreateAPIView):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer

class ApplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer