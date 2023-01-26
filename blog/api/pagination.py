from rest_framework.pagination import PageNumberPagination

# for users
class OurPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "sehife"

