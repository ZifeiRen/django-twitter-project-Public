from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from newsfeeds.services import NewsFeedService
from newsfeeds.api.serializers import NewsFeedSerializer
from utils.paginations import EndlessPagination


class NewsFeedViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    pagination_class = EndlessPagination

    def list(self, request):
        queryset = NewsFeedService.get_cache_newsfeeds(request.user.id)
        page = self.paginate_queryset(queryset)
        serializer = NewsFeedSerializer(
            page,
            context={'request': request},
            many=True,
        )
        return self.get_paginated_response(serializer.data)
