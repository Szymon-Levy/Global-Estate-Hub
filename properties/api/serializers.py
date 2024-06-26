from rest_framework import serializers
from properties.models import (
    ListingStatus,
    Category,
    Amenities,
    Education,
    Shopping,
    HealthAndMedical,
    Transportation,
    City,
    Property,
    TourSchedule,
    Review,
)
from accounts.api.serializers import UserSerializer, UserUsernameSerializer


class ListingStatusSerializer(serializers.Serializer):
    """
    ListingStatus Model Serializer.
    """

    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    slug = serializers.SlugField()

    class Meta:
        model = ListingStatus


class CategorySerializer(serializers.Serializer):
    """
    Category Model Serializer.
    """

    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    slug = serializers.SlugField()

    class Meta:
        model = Category


class AmenitiesSerializer(serializers.Serializer):
    """
    Amenities Model Serializer.
    """

    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    slug = serializers.CharField()

    class Meta:
        model = Amenities


class EducationSerializer(serializers.Serializer):
    """
    Education Model Serializer.
    """

    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    distance = serializers.FloatField()
    rate = serializers.FloatField()

    class Meta:
        model = Education


class ShoppingSerializer(serializers.Serializer):
    """
    Shopping Model Serializer.
    """

    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    distance = serializers.FloatField()
    rate = serializers.FloatField()

    class Meta:
        model = Shopping


class HealthAndMedicalSerializer(serializers.Serializer):
    """
    HealthAndMedical Model Serializer.
    """

    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    distance = serializers.FloatField()
    rate = serializers.FloatField()

    class Meta:
        model = HealthAndMedical


class TransportationSerializer(serializers.Serializer):
    """
    Transportation Model Serializer.
    """

    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    distance = serializers.FloatField()
    rate = serializers.FloatField()

    class Meta:
        model = Transportation


class CitySerializer(serializers.Serializer):
    """
    City Model Serializer.
    """

    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    slug = serializers.SlugField()

    class Meta:
        model = City


class PropertySerializer(serializers.Serializer):
    """
    Property Model Serializer.
    """

    id = serializers.ReadOnlyField()
    user = UserSerializer()
    title = serializers.CharField()
    date_posted = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    thumbnail = serializers.ImageField()
    year_of_built = serializers.IntegerField()
    price = serializers.FloatField()
    number_of_bedrooms = serializers.IntegerField()
    number_of_bathrooms = serializers.IntegerField()
    square_meters = serializers.FloatField()
    parking_space = serializers.IntegerField()
    postal_code = serializers.CharField()
    city = CitySerializer()
    province = serializers.CharField()
    country = serializers.CharField()
    country_code = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    is_featured = serializers.BooleanField()
    favourites = UserSerializer(read_only=True, many=True)
    slug = serializers.SlugField()
    listing_status = ListingStatusSerializer()
    category = CategorySerializer()
    amenities = AmenitiesSerializer(read_only=True, many=True)
    education = EducationSerializer(read_only=True, many=True)
    health_and_medical = HealthAndMedicalSerializer(read_only=True, many=True)
    transportation = TransportationSerializer(read_only=True, many=True)
    shopping = ShoppingSerializer(read_only=True, many=True)
    purchasing_user = UserSerializer()

    class Meta:
        model = Property


class PropertyTitleSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()

    class Meta:
        model = Property


class TourScheduleSerializer(serializers.Serializer):
    """
    TourSchedule Model Serializer.
    """

    id = serializers.ReadOnlyField()
    customer = UserUsernameSerializer()
    property = PropertyTitleSerializer()
    date_sent = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    date = serializers.CharField()
    time = serializers.CharField()
    name = serializers.CharField()
    phone_number = serializers.EmailField()
    message = serializers.CharField()

    class Meta:
        model = TourSchedule


class ReviewSerializer(serializers.Serializer):
    """
    Review Model Serializer.
    """

    id = serializers.ReadOnlyField()
    date_posted = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    user = UserUsernameSerializer()
    property = PropertyTitleSerializer()
    rate = serializers.IntegerField()
    content = serializers.CharField()
    active = serializers.BooleanField()

    class Meta:
        model = Review
