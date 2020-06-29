from rest_framework import viewsets
from .models import Account
from .serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    "Account API endpoint"
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
