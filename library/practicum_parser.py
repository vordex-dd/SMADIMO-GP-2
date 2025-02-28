import json
import logging
import os
import requests
from bs4 import BeautifulSoup
from logger import LoggerSettings


class PracticumParser:
    def __init__(self):
        self.url = 'https://practicum.yandex.ru/catalog/?from=main_header-all-courses_button'

    def get_data(self):
        logging.info('Start fetching Yandex Practicum')
        try:
            response = requests.get(self.url, timeout=120)
        except ValueError as error:
            logging.error('Failed to scrap data from Yandex Practicum')
            logging.error(error)
            return []
        soup = BeautifulSoup(response.text, 'lxml')

        courses = soup.find_all('li', class_="prof-card prof-window-cards__item")
        if len(courses) > 0:
            logging.info(f'Fetched {len(courses)} from Yandex Practicum')
        else:
            logging.error('Failed to scrap data from Yandex Practicum')
        all_courses = []

        for i, course in enumerate(courses):
            tags_res = course.find_all('p', class_='prof-card__tag')
            tags = [tag.text.strip() for tag in tags_res if tag]

            title = course.find('h2', class_='prof-card__title')
            if title:
                title = title.text.strip()

            card_price = course.find('p', class_='prof-card__price')
            if card_price:
                card_price = ''.join(card_price.text.split('\xa0'))

            full_price = course.find('p', class_='prof-card__full-price')
            if full_price:
                full_price = ''.join(full_price.text.split('\xa0'))

            current_course = {
                'tags': tags,
                'title': title,
                'card_price': card_price,
                'full_price': full_price
            }

            all_courses.append(current_course)
            logging.debug(f'Finish fetching {i} course')

        return all_courses


if __name__ == '__main__':
    LoggerSettings.set_up()

    FOLDER_PATH = './../parsed_data'
    FILE_PATH = os.path.join(FOLDER_PATH, 'practicum_courses.json')

    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            pass

    parser = PracticumParser()

    with open(FILE_PATH, 'a', encoding='utf-8') as file:
        for course_dict in parser.get_data():
            file.write(json.dumps(course_dict, ensure_ascii=False) + '\n')
