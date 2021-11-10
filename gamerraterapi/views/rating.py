"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from gamerraterapi.models import Player, Review, Game, Rating


class RatingView(ViewSet):
    """Level up games"""

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized game instance
        """

        player = Player.objects.get(user=request.auth.user)
        game= Game.objects.get(pk=request.data['game_id'])
        try:
            rating = Rating.objects.create(
                rating=request.data['rating'],
                player=player,
                game=game
            )
            serializer = RatingSerializer(rating, context={'request': request})
            return Response(serializer.data)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        ratings = Rating.objects.all()

        serializer = RatingSerializer(
            ratings, many=True, context={'request': request})
        return Response(serializer.data)
        

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'player', 'game', 'rating')
        depth = 1