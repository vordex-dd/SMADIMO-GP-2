import json
import logging
import requests
from logger import LoggerSettings
from check_directory import check_directory


class StepikParser:

    def __init__(self):
        self.base_path = 'https://stepik.org/api/courses?page='

    def get_data(self):
        logging.info('Start fetching Stepik API')
        current_page = 1
        while True:
            url = f'{self.base_path}{current_page}'
            current_courses, has_next = self.fetch_url(url)
            logging.debug(f'Finish fetching {current_page} page')
            yield current_courses

            if has_next:
                current_page += 1
            else:
                logging.info('Finish fetching Stepik API')
                break

    @staticmethod
    def fetch_url(url: str):
        try:
            response = requests.get(url, timeout=120).json()
            return response['courses'], response['meta']['has_next']
        except ValueError as error:
            logging.error(error)
            return [], True


if __name__ == '__main__':
    LoggerSettings.set_up()
    file_path = check_directory('stepik_courses.json')

    parser = StepikParser()

    with open(file_path, 'a', encoding='utf-8') as file:
        for courses in parser.get_data():
            for course in courses:
                file.write(json.dumps(course, ensure_ascii=False) + '\n')
