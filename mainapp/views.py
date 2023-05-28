from rest_framework import generics, permissions, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User, Content
from .serializers import CreateUserSerializer, ContentSerializer, LoginUserSerializer
from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from assignment_api.settings import AUTH_USER_MODEL
from .models import User
from .permissions import IsAuthorOrAdmin
from rest_framework.exceptions import PermissionDenied
from rest_framework import filters


# content    


class ContentViewSet(viewsets.ModelViewSet):

    serializer_class = ContentSerializer
    permission_classes = [IsAuthorOrAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields  = ['title', 'body', 'summary', 'categories']

    def get_queryset(self):
        queryset = Content.objects.all()
        
        if self.action == 'list':
            if not self.request.user.is_authenticated:
                return queryset
            if self.request.user.is_superuser or self.request.user.admin:
                return queryset
            queryset = queryset.filter(author=self.request.user)
        
        return queryset


    def perform_create(self, serializer):
        author_id = serializer.validated_data['author'].id
        if author_id != self.request.user.id:
            raise PermissionDenied("You can only create content for yourself.")
        serializer.save(author=self.request.user)




# Author
class AuthorRegistrationView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = serializer.instance
        user.author = True  # Set the 'author' field to True
        user.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class AuthorLoginView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(request, email=email, password=password)
        # if user is not None and user.role == 'author':
        if user:
            return Response({'message': 'Author login successful.'})
        else:
            return Response({'message': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)