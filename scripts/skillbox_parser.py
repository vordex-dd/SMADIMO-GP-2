import json
import logging

from check_directory import check_directory
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from logger import LoggerSettings


class SkillboxParser:
    def __init__(self):
        self.driver = webdriver.Safari()
        self.url = 'https://skillbox.ru/courses/'

    def fetch_page_source(self):
        logging.info('Start fetching Skillbox')
        try:
            self.driver.get(self.url)
        except ValueError as error:
            logging.error('Failed to scrap data from Skillbox')
            logging.error(error)
            self.driver.quit()
            return None

        return self.expand_courses_list()

    def expand_courses_list(self):
        logging.info('Start expanding the Skillbox courses list')
        more_button_xpath = '//*[@id="#app"]/main/div[1]/div[2]/div/div[2]/div/section[2]/button'
        button_press_counter = 0
        while True:
            try:
                WebDriverWait(self.driver, 20).until(
                    ec.presence_of_element_located((By.XPATH, more_button_xpath))
                )
                button = WebDriverWait(self.driver, 20).until(
                    ec.element_to_be_clickable((By.XPATH, more_button_xpath))
                )

                self.driver.execute_script("arguments[0].click();", button)
                button_press_counter += 1
                logging.debug(f'Press button "More" on Skillbox {button_press_counter} times')

            except (NoSuchElementException, TimeoutException):
                logging.info('Finish expanding the Skillbox courses list')
                html_content = self.driver.page_source
                self.driver.quit()
                return html_content

    def extract_courses(self, html_content):
        soup = BeautifulSoup(html_content, 'lxml')
        courses_container = soup.find_all('div', class_='card-list courses-block__list card-list--catalog')[1]

        courses = courses_container.find_all('article', class_='ui-product-card')
        if len(courses) > 0:
            logging.info(f'Fetched {len(courses)} courses from Skillbox')
        else:
            logging.error('Failed to scrap data from Skillbox')

        return self.parse_courses(courses)

    @staticmethod
    def parse_courses(courses):
        courses_data = []
        for i, course in enumerate(courses):
            logging.debug(f'Start fetching {i} course')

            title = course.find('h3', class_='ui-product-card-main__title t t--2')
            if title:
                title = title.text.replace('\u2028', '').replace('\u00ad', '').strip()

            duration_amount, duration_units = (
                course.find('span', class_='card__duration f f--12')
                .text.replace('\n', '')
                .strip().split()
            )

            is_popular = course.find('span', string='Популярное')
            if is_popular:
                is_popular = is_popular.text.strip() == "Популярное"
            else:
                is_popular = False

            current_course = {
                'title': title,
                'duration_amount': duration_amount,
                'duration_units': duration_units,
                'is_popular': is_popular
            }

            courses_data.append(current_course)
            logging.debug(f'Finish fetching {i} course')

        return courses_data

    def get_data(self):
        html_content = self.fetch_page_source()
        if html_content is None:
            return []
        return self.extract_courses(html_content)


if __name__ == '__main__':
    LoggerSettings.set_up()
    file_path = check_directory('skillbox_courses.json')

    parser = SkillboxParser()

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(parser.get_data(), ensure_ascii=False, indent=4) + '\n')
