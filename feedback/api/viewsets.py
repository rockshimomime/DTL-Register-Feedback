from rest_framework.viewsets import ModelViewSet

from feedback.api.serializers import RegistroSerializer
from feedback.models import Registro


class RegistroViewSet(ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
