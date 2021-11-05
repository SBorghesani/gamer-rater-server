"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.contrib.auth import get_user_model
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from gamerraterapi.models import Category

class CategoryView(ViewSet):
    def list(self, request):
        """Handle GET requests to categories resource
        Returns:
            Response -- JSON serialized list of categories
        """
        categories = Category.objects.all()

        # Support filtering games by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games
        # game_type = self.request.query_params.get('type', None)
        # if game_type is not None:
        #     games = games.filter(game_type__id=game_type)

        serializer = CategorySerializer(
            categories, many=True, context={'request': request})
        return Response(serializer.data)

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    
    Arguments:
        serializer type
    """

    class Meta:
        model = Category
        fields = ('id', 'category')
        depth = 1