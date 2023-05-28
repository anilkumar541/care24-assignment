from django.db import models
from django.contrib.auth.models import AbstractUser,Permission, Group
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password

# user manager

# class CustomUserManager(UserManager):
#     use_in_migrations = True

#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('Users require an email field')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, password, **extra_fields)

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
class User(AbstractUser):

    admin = models.BooleanField(default=False)
    author = models.BooleanField(default=False)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username= None
    password = models.CharField(max_length=128, validators=[
        MinLengthValidator(8),
        RegexValidator(
            regex=r'^(?=.*[a-z])(?=.*[A-Z]).+$',
            message="Password must contain at least one lowercase letter, one uppercase letter.")])
    phone_no = models.CharField(unique=True ,max_length=10, validators=[
        RegexValidator(
            regex=r'^[0-9]+$',
            message="Phone number must be numeric."),
        MinLengthValidator(10)])
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=6, validators=[
        RegexValidator(
            regex=r'^[0-9]+$',
            message="Pincode must be numeric."
        ),
        MinLengthValidator(6)
    ])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )


    def __str__(self):
        return self.email
    
    #encrypt password before saving in db
    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)



class Content(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    summary = models.CharField(max_length=60)
    document = models.FileField(upload_to='documents/', validators=[
        FileExtensionValidator(allowed_extensions=['pdf'])
    ])
    categories = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title