import django_filters
from .models import view_room_db


class search_view_room_db(django_filters.FilterSet):
    class Meta:
        model = view_room_db
        fields = ['category', 'sub_category', 'location', ]