"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from gamerraterapi.models import Player, Review, Game, Rating, Picture
from django.core.files.base import ContentFile
import uuid, base64


class PictureView(ViewSet):
    """Level up games"""

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized game instance
        """

        player = Player.objects.get(user=request.auth.user)
        game= Game.objects.get(pk=request.data['game_id'])
        game_pic = Picture()
        
        format, imgstr = request.data["url"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["game_id"]}-{uuid.uuid4()}.{ext}')

        game_pic.action_pic = data
        game_pic.game = game
        game_pic.player = player
        game_pic.save()

        try:
            
            serializer = PictureSerializer(game_pic, context={'request': request})

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        pictures = Picture.objects.all()

        serializer = PictureSerializer(
            pictures, many=True, context={'request': request})
        return Response(serializer.data)
        

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'player', 'game', 'action_pic')
        depth = 1