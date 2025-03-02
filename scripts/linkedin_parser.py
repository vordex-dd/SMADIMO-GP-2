import json
import logging
import webbrowser
from urllib.parse import urlencode
import requests
from logger import LoggerSettings
from check_directory import check_directory


class LinkedinParser:
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.authorization_url = "https://www.linkedin.com/oauth/v2/authorization"
        self.token_url = "https://www.linkedin.com/oauth/v2/accessToken"
        self.base_path = "https://api.linkedin.com/v2/learningAssets"

    def get_authorization_url(self):
        params = {
            'response_type': 'code',
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'scope': ' '.join(self.scope)
        }
        return f"{self.authorization_url}?{urlencode(params)}"

    def fetch_access_token(self, code):
        logging.info('Start fetching linkedin access token')
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        response = requests.post(self.token_url, data=data, timeout=120)
        try:
            token = response.json().get('access_token')
            logging.info('Finish fetching linkedin access token')
            return token
        except ValueError as error:
            logging.error(error)
            return ''

    def start_authorization(self):
        logging.info('Start linkedin authorization')
        url = self.get_authorization_url()
        print("Please go to this URL and authorize the application:", url)
        webbrowser.open(url)

    def get_data(self, token):
        logging.info('Start fetching Linkedin API')
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
        }
        params = {
            'assetType': 'COURSE',
            'q': 'localeAndType',
            'fields': 'title,description,author,category'
        }
        try:
            response = requests.get(self.base_path, params=params, headers=headers, timeout=120).json()
            elements = response['elements']
            logging.info('Finish fetching Linkedin API')
            return elements
        except ValueError as error:
            logging.error(error)
            return []


if __name__ == '__main__':
    LoggerSettings.set_up()
    linkedin = LinkedinParser(
        client_id='',
        client_secret='',
        redirect_uri='https://google.com',
        scope=['w_member_social', 'openid', 'profile']
    )
    linkedin.start_authorization()
    authorization_code = input("Enter the authorization code: ")
    access_token = linkedin.fetch_access_token(authorization_code)

    file_path = check_directory('linkedin_courses.json')

    with open(file_path, 'a', encoding='utf-8') as file:
        for courses in linkedin.get_data(access_token):
            for course in courses:
                file.write(json.dumps(course, ensure_ascii=False) + '\n')
