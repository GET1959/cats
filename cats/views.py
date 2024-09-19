from rest_framework.viewsets import ModelViewSet

from cats.models import Cat
from cats.serializers import CatSerializer
from users.permissions import IsOwner


class CatViewSet(ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def get_queryset(self):
        if not self.request.user.groups.filter(name='moderator').exists():
            return Cat.objects.filter(owner=self.request.user)
        return Cat.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "retrieve", "destroy"]:
            self.permission_classes = (IsOwner,)
        return super().get_permissions()
