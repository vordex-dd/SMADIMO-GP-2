import json
import logging
import requests
from logger import LoggerSettings
from check_directory import check_directory


class CourseraParser:
    def __init__(self):
        self.base_path = 'https://api.coursera.org/api/courses.v1'

    def get_data(self):
        logging.info('Start fetching Coursera API')
        params = {
            'start': 0,
            'limit': 2000,
            'fields': 'name,description,partnerIds,instructorIds,\
            primaryLanguages,workload,duration,isTranslate' 
        }
        try:
            response = requests.get(self.base_path, params=params, timeout=120).json()
            logging.info('Finish fetching Coursera API')
            return response['elements']
        except ValueError as error:
            logging.error(error)
            return []


if __name__ == '__main__':
    LoggerSettings.set_up()
    file_path = check_directory('coursera_courses.json')

    parser = CourseraParser()

    with open(file_path, 'a', encoding='utf-8') as file:
        for courses in parser.get_data():
            for course in courses:
                file.write(json.dumps(course, ensure_ascii=False) + '\n')
