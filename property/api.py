from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .forms import PropertyForm
from .models import Property
from django.http import JsonResponse

from .serializers import PropertiesListSerializer


class PropertiesListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        properties = Property.objects.all()
        serializer = PropertiesListSerializer(properties, many=True)
        return JsonResponse({'data': serializer.data})

class PropertyCreateView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.landlord = request.user
            property.save()
            return JsonResponse({'status': True}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'errors': form.errors.as_json()}, status=status.HTTP_400_BAD_REQUEST)