from django.middleware.csrf import get_token
from properties.models import Property, Category, City
from itertools import chain


def generate_token(request) -> dict:
    """
    Generating CSRF middleware tokens for all forms in the project.

    return: dict
    """
    return {
        'csrf_token': get_token(request=request)
    }


def properties_types(request):
    """
    Returns all available property categories along with information such as category name,
    image source, URL address, and the number of properties in each category.

    return: dict
    """
    return {
        'get_category_properties_info': list(
            zip(
                [category.name for category in Category.objects.all().order_by('-name')],
                [category.image.url for category in Category.objects.all().order_by('-name')],
                [category.get_absolute_url() for category in Category.objects.all().order_by('-name')],
                [Property.objects.filter(category=category).count() for category in
                 Category.objects.all().order_by('-name')]
            )
        ),
    }


def explore_cities(request):
    """
    Returns all available property cities along with information such as city name,
    image source, URL address, and the number of properties in each city.

    return: dict
    """
    return {
        'get_cities_info': list(
            zip(
                [city.name for city in City.objects.all().order_by('-name')],
                [city.image.url for city in City.objects.all().order_by('-name')],
                [city.get_absolute_url() for city in City.objects.all().order_by('-name')],
                [Property.objects.filter(city=city).count() for city in
                 City.objects.all().order_by('-name')]
            )
        ),
    }


def discover_cities(request):
    """
    Returns the most frequently occurring cities in the database.

    return: dict
    """
    return {
        'discover_cities': [p.city for p in
                            list(chain(*[Property.objects.filter(city=c) for c in City.objects.all()]))][:8],
    }
