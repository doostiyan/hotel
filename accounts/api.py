from rest_framework.views import APIView
from .models import User
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .serializers import UserDetailSerializer


class LandlordView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserDetailSerializer(user, many=False)
        return JsonResponse(serializer.data, safe=False)


class ReservationsListView(APIView):

    def get(self, request):
        reservation = request.user.reservations.all()

        serializer = UserDetailSerializer(reservation, many=True)
        return JsonResponse(serializer.data, safe=False)