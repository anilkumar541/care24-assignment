# Generated by Django 4.2.1 on 2023-05-27 09:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('admin', models.BooleanField(default=False)),
                ('author', models.BooleanField(default=False)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.RegexValidator(message='Password must contain at least one lowercase letter, one uppercase letter.', regex='^(?=.*[a-z])(?=.*[A-Z]).+$')])),
                ('phone_no', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be numeric.', regex='^[0-9]+$'), django.core.validators.MinLengthValidator(10)])),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('county', models.CharField(blank=True, max_length=255, null=True)),
                ('pincode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Pincode must be numeric.', regex='^[0-9]+$'), django.core.validators.MinLengthValidator(6)])),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_set', related_query_name='custom_user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_set', related_query_name='custom_user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', mainapp.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.CharField(max_length=300)),
                ('summary', models.CharField(max_length=60)),
                ('document', models.FileField(upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('categories', models.CharField(blank=True, max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
