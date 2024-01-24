from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import Property, ListingStatus, Category, City
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def property_context(obj: dict = None):
    rent_status_id = ListingStatus.objects.get(name='Rent').id

    context = {
        'listing_statuses': ListingStatus.objects.all(),
        'categories': sorted(
            list(set([obj.category.name for obj in Property.objects.filter(listing_status_id=rent_status_id)]))),
        'min_price': min([obj.price for obj in Property.objects.filter(listing_status_id=rent_status_id)]),
        'max_price': max([obj.price for obj in Property.objects.filter(listing_status_id=rent_status_id)]),
        'number_of_bedrooms': sorted(
            list(set([obj.number_of_bedrooms for obj in
                      Property.objects.filter(listing_status_id=rent_status_id)]))),
        'number_of_bathrooms': sorted(
            list(set([obj.number_of_bathrooms for obj in
                      Property.objects.filter(listing_status_id=rent_status_id)]))),
        'cities': sorted(
            list(set(obj.city.name for obj in Property.objects.filter(listing_status_id=rent_status_id)))),
        'square_meters': sorted(
            list(
                set([int(obj.square_meters) for obj in Property.objects.filter(listing_status_id=rent_status_id)])))
    }

    if obj is None:
        return context

    else:
        context.update(obj)

        return context


def property_pagination(request, object_list, per_page):
    paginator = Paginator(object_list=object_list, per_page=per_page)
    page = request.GET.get('page')
    pages = paginator.get_page(number=page)

    if page is None:
        pages = paginator.get_page(number=1)

    else:
        if page not in list(str(i) for i in pages.paginator.page_range):
            return redirect(to='error')

    return pages


def properties(request):
    queryset = []
    context_1 = {}

    if request.GET:
        print('Request GET.')

        if 'properties-order' in request.GET:
            print('If properties Order in request GET.')

            if 'keyword' in request.session:
                print('If properties Order in request GET and then if keyword in request session.')

                if 'Newest Properties' in request.GET.get('properties-order'):
                    print('Newest Properties in Properties Order with Keyword in request session.')
                    request.session['sorted_type'] = 'Newest Properties'
                    queryset.extend(Property.objects.filter(title__icontains=request.session.get('keyword')).order_by(
                        '-date_posted'))

                elif 'Oldest Properties' in request.GET.get('properties-order'):
                    print('Oldest Properties in Properties Order with Keyword in request session.')
                    request.session['sorted_type'] = 'Oldest Properties'
                    queryset.extend(Property.objects.filter(title__icontains=request.session.get('keyword')).order_by(
                        'date_posted'))

                elif 'Alphabetically Ascending' in request.GET.get('properties-order'):
                    print('Alphabetically Ascending in Properties Order with Keyword in request session.')
                    request.session['sorted_type'] = 'Alphabetically Ascending'
                    queryset.extend(
                        Property.objects.filter(title__icontains=request.session.get('keyword')).order_by('title'))

                elif 'Alphabetically Descending' in request.GET.get('properties-order'):
                    print('Alphabetically Descending in Properties Order with Keyword in request session.')
                    request.session['sorted_type'] = 'Alphabetically Descending'
                    queryset.extend(
                        Property.objects.filter(title__icontains=request.session.get('keyword')).order_by('-title'))

            elif 'status' in request.session:
                print(request.GET)
                print('If properties order in request GET and then elif status in request session.')
                queryset.clear()
                queryset.extend(Property.objects.filter(
                    listing_status_id=ListingStatus.objects.get(name=request.session.get('status').capitalize())))

                if 'Newest Properties' in request.GET.get('properties-order'):
                    print('Newest Properties in Properties Order with Status in request session.')
                    queryset.clear()
                    request.session['sorted_type'] = 'Newest Properties'
                    queryset.extend(Property.objects.filter(
                        listing_status_id=ListingStatus.objects.get(
                            name=request.session.get('status').capitalize())).order_by('-date_posted'))

                elif 'Oldest Properties' in request.GET.get('properties-order'):
                    print('Oldest Properties in Properties Order with Status in request session.')
                    queryset.clear()
                    request.session['sorted_type'] = 'Oldest Properties'
                    queryset.extend(Property.objects.filter(
                        listing_status_id=ListingStatus.objects.get(
                            name=request.session.get('status').capitalize())).order_by('date_posted'))

                elif 'Alphabetically Ascending' in request.GET.get('properties-order'):
                    print('Alphabetically Ascending in Properties Order with Status in request session.')
                    queryset.clear()
                    request.session['sorted_type'] = 'Alphabetically Ascending'
                    queryset.extend(Property.objects.filter(
                        listing_status_id=ListingStatus.objects.get(
                            name=request.session.get('status').capitalize())).order_by('title'))

                elif 'Alphabetically Descending' in request.GET.get('properties-order'):
                    print('Alphabetically Descending in Properties Order with Status in request session.')
                    queryset.clear()
                    request.session['sorted_type'] = 'Alphabetically Descending'
                    queryset.extend(Property.objects.filter(
                        listing_status_id=ListingStatus.objects.get(
                            name=request.session.get('status').capitalize())).order_by('-title'))

            elif 'category' in request.session:
                print('If properties order in request GET and then elif category in request session.')
                queryset.clear()
                queryset.extend(Property.objects.filter(
                    listing_status_id=ListingStatus.objects.get(name=request.session.get('status').capitalize())))


            else:
                if 'Newest Properties' in request.GET.get('properties-order'):
                    request.session['sorted_type'] = request.GET.get('properties-order')
                    queryset.extend(Property.objects.all().order_by('-date_posted'))

                if 'Oldest Properties' in request.GET.get('properties-order'):
                    request.session['sorted_type'] = request.GET.get('properties-order')
                    queryset.extend(Property.objects.all().order_by('date_posted'))

                if 'Alphabetically Ascending' in request.GET.get('properties-order'):
                    print(request.session.items())
                    request.session['sorted_type'] = request.GET.get('properties-order')
                    queryset.extend(Property.objects.all().order_by('title'))

                if 'Alphabetically Descending' in request.GET.get('properties-order'):
                    request.session['sorted_type'] = request.GET.get('properties-order')
                    queryset.extend(Property.objects.all().order_by('-title'))

        elif 'keyword' in request.GET:
            print('Elif keyword in request GET.')
            request.session['sorted_type'] = 'Newest Properties'
            request.session['keyword'] = request.GET.get('keyword')
            keyword = request.GET.get('keyword')
            queryset.extend(
                Property.objects.filter(title__icontains=keyword).order_by('-date_posted'))

        elif 'status' in request.GET:
            print('Elif status in request GET.')
            request.session['sorted_type'] = 'Newest Properties'
            status = request.GET.get('status')
            request.session['status'] = request.GET.get('status')
            queryset.extend(
                Property.objects.filter(listing_status_id=ListingStatus.objects.get(name=status.capitalize())))

        elif 'category' in request.GET:
            print('Elif category in request GET.')
            category = request.GET.get('category')
            request.session['sorted_type'] = 'Newest Properties'

            request.session['category'] = [category]
            queryset.extend(Property.objects.filter(category_id=Category.objects.get(name=category.capitalize())))
            print(category)
            print(request.session.items())

            # context_1.update({
            #     'listing_statuses': [obj.listing_status.name for obj in
            #                          Property.objects.filter(category=Category.objects.get(name=category)).id],
            #     'categories': [obj.name for obj in Category.objects.all()],
            #     'min_price': min(list(set([obj.price for obj in Property.objects.all()]))),
            #     'max_price': max(list(set([obj.price for obj in Property.objects.all()]))),
            #     'number_of_bedrooms': sorted(set([obj.number_of_bedrooms for obj in Property.objects.all()])),
            #     'number_of_bathrooms': sorted(set([obj.number_of_bathrooms for obj in Property.objects.all()])),
            #     'cities': sorted(set([obj.name for obj in City.objects.all()])),
            #     'square_meters': sorted(set([obj.square_meters for obj in Property.objects.all()])),

        else:
            request.session['sorted_type'] = 'Newest Properties'
            queryset.extend(Property.objects.all().order_by('-date_posted'))

    else:
        print('No request GET.')
        if request.session.get('sorted_type'):
            request.session.pop('sorted_type')

        if request.session.get('keyword'):
            request.session.pop('keyword')

        if request.session.get('status'):
            request.session.pop('status')

        request.session['sorted_type'] = 'Newest Properties'
        queryset.extend(Property.objects.all().order_by('-date_posted'))

    context_2 = {
        'title': 'Properties',
        'properties': queryset,
        'sorted_type': request.session['sorted_type'],
        'pages': property_pagination(request=request, object_list=queryset, per_page=6),
        'listing_statuses': [obj.name for obj in ListingStatus.objects.all()],
        'categories': [obj.name for obj in Category.objects.all()],
        'min_price': min(list(set([obj.price for obj in Property.objects.all()]))),
        'max_price': max(list(set([obj.price for obj in Property.objects.all()]))),
        'number_of_bedrooms': sorted(set([obj.number_of_bedrooms for obj in Property.objects.all()])),
        'number_of_bathrooms': sorted(set([obj.number_of_bathrooms for obj in Property.objects.all()])),
        'cities': sorted(set([obj.name for obj in City.objects.all()])),
        'square_meters': sorted(set([obj.square_meters for obj in Property.objects.all()])),
    }

    return render(request=request, template_name='properties/properties.html', context=context_2)


@login_required(login_url='login')
def add_property(request):
    return render(request=request, template_name='properties/add-property.html', context={
        'title': 'Add Property',
    })


def add_to_favourites(request):
    """
    The function handles the form for adding a property to favorites.
    If the property was already added to favorites by the user, the liking is removed.
    However, if the user adds the property to favorites for the first time, the liking is saved.
    The function utilizes the PATCH method with Asynchronous JavaScript and XMLHttpRequest (AJAX).
    Upon successful form validation, the data is updated in the database.

    return: JsonResponse
    """
    if request.method == 'PATCH':
        property_id = int(json.loads(s=request.body.decode('utf-8'))['propertyId'])
        property_obj = Property.objects.get(id=property_id)

        if request.user in property_obj.favourites.all():
            property_obj.favourites.remove(request.user)

            return JsonResponse(data={
                "valid": True,
                "propertyId": property_id,
            })

        elif request.user not in property_obj.favourites.all():
            property_obj.favourites.add(request.user)
            property_obj.save()

            return JsonResponse(data={
                "valid": True,
                "propertyId": property_id,
            })

        else:
            return JsonResponse(data={
                "valid": False,
            })


def property_details(request, property_slug):
    property_obj = Property.objects.get(slug=property_slug)

    return render(request=request, template_name='properties/property-details.html', context={
        'title': property_obj.title,
    })
