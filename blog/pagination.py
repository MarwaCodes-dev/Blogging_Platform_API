from rest_framework.pagination import LimitOffsetPagination

class BlogPagination(LimitOffsetPagination):
    default_limit=10

    def get_limit(self, request):
        limit=request.query_params.get('limit',None)
        if limit is not None:
            try :
                return int(limit)
            except ValueError:
                return self.default_limit
        return self.default_limit if limit is None else limit        