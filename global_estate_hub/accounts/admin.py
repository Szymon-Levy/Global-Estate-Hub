from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, OneTimePassword, Private, Company

admin.site.unregister(Group)


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'image', 'password', 'is_company', 'is_private', 'is_verified', 'is_staff',
                    'is_active', 'is_superuser', 'date_joined']
    list_editable = ['email', 'is_company', 'is_private', 'is_verified', 'is_staff', 'is_active', 'is_superuser']
    list_filter = ['username', 'email', 'is_company', 'is_private', 'date_joined']
    list_display_links = ['username']


@admin.register(OneTimePassword)
class AdminOneTimePassword(admin.ModelAdmin):
    list_display = ['user', 'password', 'created_at', 'expires_in']


@admin.register(Private)
class AdminPrivateProfile(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'gender', 'country', 'province', 'city',
                    'street', 'postal_code', 'phone_number', 'website_url', 'facebook_url', 'instagram_url',
                    'linkedin_url']
    list_editable = ['first_name', 'last_name', 'gender', 'country', 'province', 'city',
                     'street', 'postal_code', 'phone_number', 'website_url', 'facebook_url', 'instagram_url',
                     'linkedin_url']
    list_filter = ['last_name', 'country', 'province', 'city', 'street', 'postal_code']
    list_display_links = ['user']


@admin.register(Company)
class AdminCompanyProfile(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'company_id', 'country', 'province', 'city',
                    'street', 'postal_code', 'phone_number', 'website_url', 'facebook_url', 'instagram_url',
                    'linkedin_url']
    list_editable = ['company_name', 'company_id', 'country', 'province', 'city',
                     'street', 'postal_code', 'phone_number', 'website_url', 'facebook_url', 'instagram_url',
                     'linkedin_url']
    list_filter = ['company_name', 'country', 'province', 'city', 'street', 'postal_code']
    list_display_links = ['user']
