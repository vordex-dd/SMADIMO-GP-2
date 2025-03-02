import json
import logging
import requests
from coursera_api_types import CourseraApiTypes
from logger import LoggerSettings
from check_directory import check_directory


class CourseraParser:
    def __init__(self):
        self.base_path = 'https://api.coursera.org/api/'

    def get_data(self, request_api_type: CourseraApiTypes):
        request_path = self.get_path(request_api_type)
        logging.info(f'Start fetching Coursera API: {request_api_type}')
        params = {
            'start': 0,
            'limit': 2000,
            'fields': 'name,description,partnerIds,instructorIds,\
            primaryLanguages,workload,duration,isTranslate'
        }
        try:
            response = requests.get(request_path, params=params, timeout=120).json()
            elements = response['elements']
            logging.info(f'Finish fetching Coursera API: {request_api_type}')
            return elements
        except ValueError as error:
            logging.error(error)
            return []

    def get_path(self, api_type: CourseraApiTypes):
        if api_type == CourseraApiTypes.COURSE:
            return self.base_path + 'courses.v1'
        elif api_type == CourseraApiTypes.PARTNERS:
            return self.base_path + 'partners.v1'
        else:
            return self.base_path + 'instructors.v1'


if __name__ == '__main__':
    LoggerSettings.set_up()

    request_params = [
        ('coursera_courses.json', CourseraApiTypes.COURSE),
        ('coursera_partners.json', CourseraApiTypes.PARTNERS),
        ('coursera_instructors.json', CourseraApiTypes.INSTRUCTORS)
    ]

    parser = CourseraParser()

    for file_name, request_type in request_params:
        path = check_directory(file_name)
        with open(path, 'a', encoding='utf-8') as file:
            file.write(json.dumps(parser.get_data(request_type), ensure_ascii=False, indent=4) + '\n')
