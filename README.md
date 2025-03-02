# SMADIMO-GP-2 ![progress_check](https://github.com/vordex-dd/SMADIMO-GP-2/actions/workflows/pylint.yml/badge.svg)
Групповой проект N2 по предмету СМАДИМО в рамках обучения в НИУ ВШЭ.

Состав команды:

| ФИ                  | Учебная группа | Github аккаунт                        |
|---------------------|----------------|---------------------------------------|
| Деларю Дмитрий      | ББИ227         | https://github.com/vordex-dd          |
| Либов Максим        | ББИ227         | https://github.com/mxlq1              |
| Черняев Аркадий     | ББИ227         | https://github.com/qKasha             |
| Матылев Савелий     | ББИ227         | https://github.com/sdmatylev          |
| Серебренников Данил | ББИ227         | https://github.com/SerebrennikovDanil |
| Перешивкина Мария   | ББИ227         | https://github.com/Mashunenok         |


## Оглавление

- [📜 Используемые скрипты](#используемые-скрипты)
- [📊 Данные](#данные)
- [📝 Логирование](#логирование)
- [📚 Используемые библиотеки](#используемые-библиотеки)
- [🔍 EDA анализ](#eda-анализ)
- [🔗 Merge Flow](#merge-flow)


## Используемые скрипты
Папка [library](./library) служит хранилищем для питоновских скриптов. На данный момент имеем скрипты:

[logger](./library/logger.py) - класс для настройки логера (задает необходимые конфиги, уровни логирования)

[stepik_parser](./library/stepik_parser.py) - класс для парсинга stepika

[practicum_parser](./library/practicum_parser.py) - класс для скрепинга яндекс практикума

[coursera_api_types](./library/coursera_api_types.py) - enum с типами api для запроса на coursera

[coursera_parser](./library/coursera_parser.py) - класс для парсинга coursera

[linkedin_parser](./library/linkedin_parser.py) - класс для парсинга linkedin (данный парсинг у нас так и не получился, но мы его оставили, так как там делается несколько интересных api запросов (за токеном и за данными))

[check_directory](./library/check_directory.py) - метод для определения директории сокранения данных

## Данные

Папка [parsed_data](./parsed_data) служит хранилищем для данных, которые мы запарсили с различных сайтов/api.

### Stepik

Данные самих курсов лежат [здесь](./parsed_data/stepik_courses.json). Имеют следуюущую структуру:

| Название                   | Описание                                              | Тип                |
|----------------------------|-------------------------------------------------------|--------------------|
| title                      | Название курса                                        | Строка             |
| title_en                   | Английское название курса                             | Строка             |
| workload                   | Длительность курса                                    | Строка             |
| difficulty                 | Сложность курса                                       | Строка             |
| target_audience            | Целевая аудитория                                     | Строка             |
| course_type                | Тип курса                                             | Строка             |
| requirements               | Требования к курсу                                    | Строка             |
| slug                       | slug формат названия курса                            | Строка             |
| summary                    | Описание курса                                        | Строка             |
| language                   | Язык курса                                            | Строка             |
| grading_policy             | Правила оценивания курса                              | Строка             |
| price                      | Цена курса                                            | Строка             |
| currency_code              | Код валюты                                            | Строка             |
| id                         | Уникальный ID курса                                   | Число              |
| total_units                | Количество разделов                                   | Число              |
| position                   | Позиция курса                                         | Число              |
| owner                      | ID владельца курса                                    | Число              |
| first_lesson               | ID первого занятия курса                              | Число              |
| first_unit                 | ID первого раздела                                    | Число              |
| certificates_count         | Количество сертификатов за курс                       | Число              |
| learners_count             | Количество учащихся                                   | Число              |
| lessons_count              | Количество занятий                                    | Число              |
| quizzes_count              | Количество викторин                                   | Число              |
| challenges_count           | Количество чэлленджей                                 | Число              |
| videos_duration            | Длина видео в курсе                                   | Число              |
| create_date                | Дата создания                                         | Дата               |
| update_date                | Дата обновления                                       | Дата               |
| became_published_at        | Дата публикации                                       | Дата               |
| is_public                  | Публичный ли курс                                     | Булевая переменная |
| is_archived                | Архивный ли курс                                      | Булевая переменная |
| is_censored                | Цензурированный ли курс                               | Булевая переменная |
| is_paid                    | Платный ли курс                                       | Булевая переменная |
| is_certificate_issued      | Дается ли сертификат по окончанию курса               | Булевая переменная |
| is_certificate_auto_issued | Автоматически ли дается сертификат по окончанию курса | Булевая переменная |
| has_tutors                 | Есть наставник                                        | Булевая переменная |
| is_adaptive                | Адаптивный ли курс                                    | Булевая переменная |
| is_contest                 | В формате контеста ли курс                            | Булевая переменная |
| is_in_wishlist             | Входит в список желаний                               | Булевая переменная |
| is_proctored               | С прокторингом ли курс                                | Булевая переменная |
| is_self_paced              | Курс в свободном формате                              | Булевая переменная |
| is_popular                 | Популярен ли курс                                     | Булевая переменная |
| instructors                | Список ID инструкторов курса                          | Массив чисел       |
| sections                   | Список ID разделов курса                              | Массив чисел       |
| authors                    | Список ID авторов курса                               | Массив чисел       |
| tags                       | Тэги курса                                            | Массив чисел       |

Также есть набор других полей, но мы описали среди них только основные, которые могут быть полезны для анализа.




### Coursera

Данные самих курсов лежат [здесь](./parsed_data/coursera_courses.json). Имеют следующую структуру:

| Название         | Описание                   | Тип          |
|------------------|----------------------------|--------------|
| name             | Название курса             | Строка       |
| courseType       | Тип курса                  | Строка       |
| description      | Описание курса             | Строка       |
| id               | ID курса                   | Строка       |
| slug             | slug формат названия курса | Строка       |
| workload         | Длительность курса         | Строка       |
| instructorIds    | Инстукторы курса (их ID)   | Массив строк |
| partnerIds       | Партнеры курса (их ID)     | Массив строк |
| primaryLanguages | Языки курса                | Массив строк |

Данные инстукторов курсов лежать [здесь](./parsed_data/coursera_instructors.json). Имеют следующую стуктуру:

| Название   | Описание                                      | Тип          |
|------------|-----------------------------------------------|--------------|
| fullName   | Полное имя                                    | Строка       |
| id         | ID инструктора                                | Строка       |
| partnerIds | Список к каким партнерам относится инструктор | Массив строк |

Данные партнеров курсов лежать [здесь](./parsed_data/coursera_partners.json). Имеют следующую структуру:

| Название      | Описание                         | Тип          |
|---------------|----------------------------------|--------------|
| name          | Название организации             | Строка       |
| shortName     | Сокращенное название организации | Строка       |
| id            | ID организации                   | Строка       |
| description   | Описание организации             | Строка       |
| instructorIds | Список инструкторов организации  | Массив строк |

### Practicum

Данные курсов лежать [здесь](./parsed_data/practicum_courses.json). Они имеют следующую структуру:

| Название   | Описание               | Тип          |
|------------|------------------------|--------------|
| title      | Название курса         | Строка       |
| card_price | Минимальная цена курса | Строка       |
| full_price | Полная стоимость курса | Строка       |
| tags       | Список тэгов курса     | Массив строк |


## Логирование
Для логирования испольуется питоновская библиотека logging. Настройки для нее задаются [здесь](./logging.conf).

Чтобы настройки применились, перед началом использования необходимо вызвать
```python
LoggerSettings.set_up()
```
После этого для логирования используеются привычные методы
```python
logging.debug(...)
logging.info(...)
logging.warning(...)
logging.error(...)
logging.critical(...)
```

## Используемые библиотеки

В проекте были использованы следующие библиотеки:

- Pylint: Инструмент для статического анализа и проверки стиля кода Python.

- Requests: Библиотека для выполнения HTTP запросов на Python.
  
- Beautiful Soup (bs4): Парсер HTML и XML для легкой навигации и поиска.

- lxml: Высокопроизводительный парсер для XML и HTML.

- Enum: Предоставляет поддержку для перечислений в Python.

- Logging: Встроенный модуль для логирования событий и сообщений.

- JSON: Модуль для работы с JSON-данными (сериализация и десериализация).

- Webbrowser: Модуль для открытия веб-страниц через браузер.

- Numpy: Библиотека для работы с многомерными массивами и матрицами.

- Pandas: Библиотека для анализа данных и работы с таблицами и структурированными данными.


## EDA анализ

## Merge Flow
На каждом pull request запускаются линты на трех версиях питона + нужен 1 апрув. После этого пр можно мержить.

Правила запуска линтов задаются [здесь](./.github/workflows/pylint.yml). Настройки линтера лежат [здесь](./.pylintrc).