from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core.models import Tag, User

class GetTagsList(views.APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            data = []
            for tag in Tag.objects.all():
                data.append({
                    'id': tag.pk,
                    'name': tag.name
                })
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class GetTagsList(views.APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            user_id = request.data['user_id']
            selected_tags = request.data['selected_tags']

            user = User.objects.get(tg_id=user_id)

            for tag in selected_tags:
                user.tags.add(Tag.objects.get(name=tag))
            user.save()

            return Response({'status': 'OK'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)