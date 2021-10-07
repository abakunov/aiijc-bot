from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core.models import Tag, User
import requests

def telegram_bot_sendtext(bot_message, bot_chatID):

   bot_token = '2040176965:AAHk1imMOdXlI_67w8fquf0MZjs5EkL7ujw'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)
   return response.json()


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


class SelectTags(views.APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            user_id = request.data['user_id']
            selected_tags = request.data['selected_tags']

            user = User.objects.get(tg_id=user_id)

            for tag in selected_tags:
                print(tag)
                user.tags.add(Tag.objects.get(pk=tag))
                user.save()
            
            telegram_bot_sendtext('Данные успешно сохранены.', str(user_id))
            
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)