from core.parsers import get_latest_from_trud, get_latest_from_vk
from core.models import Position, Tag

#TODO: прикрутить нейронку в момент создания вакансии
def update_database(parsed_data):
    for position in parsed_data:
        Position.objects.get_or_create(custom_position=position['custom_position'],
                                description=position['description'],
                                salary_from=position['salary_from'],
                                salary_to=position['salary_to'],
                                link=position['link'])

