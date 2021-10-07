from core.update_database import update_database
from core.parsers import get_latest_from_trud, get_latest_from_vk, get_last_vacancies_from_rabota_ru
from core.models import Position
from background_task import background


@background(schedule=1)
def update_database(parsed_data):
    for position in parsed_data:
        Position.objects.get_or_create(custom_position=position['custom_position'],
                                description=position['description'],
                                salary_from=position['salary_from'],
                                salary_to=position['salary_to'],
                                link=position['link'])

# update_database(schedule=1, repeat=300)
# update_database(get_latest_from_vk(20), schedule=1)
# update_database(get_last_vacancies_from_rabota_ru(10), schedule=1)
