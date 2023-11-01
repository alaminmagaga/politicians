# members/views.py
from rest_framework import generics
from .models import President
from  rest_framework.generics import CreateAPIView,ListAPIView, RetrieveAPIView, UpdateAPIView,DestroyAPIView
from .serializers import PresidentListSerializer, PresidentSerializer
from .pagination import PostLimitOffsetPagination,PostPageNumberPagination
from django.db.models import Q



class PresidentList(ListAPIView):
    queryset=President.objects.all().order_by('id')
    serializer_class=PresidentListSerializer
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = President.objects.all() 
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(name__icontains=query)|
                    Q(email__icontains=query)
                    ).distinct()
        return queryset_list




class PresidentDetail(RetrieveAPIView):
    queryset = President.objects.all()
    serializer_class = PresidentSerializer

 
