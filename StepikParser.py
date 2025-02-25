import requests
import json
import os


class StepikParser:

    def __init__(self):
        self.base_path = 'https://stepik.org/api/courses?page='


    def get_data(self):
        current_page = 1
        while True:
            url = f'{self.base_path}{current_page}'
            current_courses, has_next = self.fetch_url(url)

            yield current_courses

            if has_next:
                current_page += 1
            else:
                break


    @staticmethod
    def fetch_url(url: str):
        try:
            response = requests.get(url).json()
            return response['courses'], response['meta']['has_next']
        except Exception as error:
            return [], True


if __name__ == '__main__':
    folder_path = 'parsed_data'
    file_path = os.path.join(folder_path, 'stepik_courses.json')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass

    parser = StepikParser()
    result = []
    cnt = 0

    with open(file_path, 'a', encoding='utf-8') as file:
        for courses in parser.get_data():
            for course in courses:
                file.write(json.dumps(course, ensure_ascii=False) + '\n')
            result.extend(courses)
            cnt += 1

            if cnt % 100 == 0:
                print(f'i: {cnt}, courses length: {len(result)}')
                print()
