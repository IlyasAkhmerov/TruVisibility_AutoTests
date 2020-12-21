import unittest
import time
from selenium import webdriver

from ConfigManager import ConfigManager
from pages.ChatbotPage import ChatbotPage

# _________________________________________________________________________________
#
# Цель теста - проверить корректную работу Search компонента при поиске по условиям:
# 1.FAQ Only
# 2.Intents Only
# 3.First FAQ then Intents
# 4.First Intents then FAQ
#
# Сценарии тестов:
# 1.Пользователь аторизируется на сайте
# 2.Выбирает необходимого чатбота
# 3.Активизирует необходимый триггер
# 4.Публикует чатбота
# 5.Переходит на тестовую страницу
# 6.В виджете чатбота вводит данные для поиска
# 7.Убеждается, что найденные данные соответствуют условиям поиска

# Предварительные условия:
# 1.Чатбот активирован
# 2.Хотя бы один триггер активирован

# _________________________________________________________________________________

class SearchTestCases(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        config = ConfigManager.get_config()

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.driver = webdriver.Chrome(config.driver_path, options=options)
        self.driver.get(config.staging_url)

        self.page = ChatbotPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()

    def test_SearchBy_FAQOnly_SuccessfulSearch(self):  # Поиск только по FAQ

        self.page.login_on_the_website()

        self.page.close_product_tour()

        self.page.go_to_list_of_chatbots()

        self.page.switch_to_widget()
        self.page.close_widget()

        self.driver.switch_to.default_content()

        self.page.сhoose_TommyLee_chatbot()

        self.page.go_to_list_of_triggers()

        self.page.deactivate_all_triggers()

        self.page.sorting_triggers_by_name()

        self.page.enable_FAQOnly_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)

        self.page.switch_to_widget()

        self.page.sending_search_message()

        response_message = self.page.faq_response_message()

        self.assertEqual('Иван Васильевич меняет профессию', response_message)
        print('Поиск по условию FAQ Only успешно работает')

    def test_SearchBy_IntentsOnly_SuccessfulSearch(self):  # Поиск только по Intents

        self.page.login_on_the_website()

        self.page.close_product_tour()

        self.page.go_to_list_of_chatbots()

        self.page.switch_to_widget()
        self.page.close_widget()

        self.driver.switch_to.default_content()

        self.page.сhoose_TommyLee_chatbot()

        self.page.go_to_list_of_triggers()

        self.page.deactivate_all_triggers()

        self.page.sorting_triggers_by_name()

        self.page.enable_IntentsOnly_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)

        self.page.switch_to_widget()

        self.page.sending_search_message()

        response_message = self.page.intent_response_message()

        self.assertEqual('Комедии Л.Гайдая', response_message)
        print('Поиск по условию Intents Only успешно работает')

    def test_SearchBy_FirstFAQ_SuccessfulSearch(self):  # Поиск по условию First FAQ

        self.page.login_on_the_website()

        self.page.close_product_tour()

        self.page.go_to_list_of_chatbots()

        self.page.switch_to_widget()
        self.page.close_widget()

        self.driver.switch_to.default_content()

        self.page.сhoose_TommyLee_chatbot()

        self.page.go_to_list_of_triggers()

        self.page.deactivate_all_triggers()

        self.page.sorting_triggers_by_name()

        self.page.enable_FirstFAQ_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)

        self.page.switch_to_widget()

        self.page.sending_search_message()

        response_message = self.page.faq_response_message()

        self.assertEqual('Иван Васильевич меняет профессию', response_message)
        print('Поиск по условию First FAQ успешно работает')

    def test_SearchBy_FirstIntents_SuccessfulSearch(self):  # Поиск только по Intents

        self.page.login_on_the_website()

        self.page.close_product_tour()

        self.page.go_to_list_of_chatbots()

        self.page.switch_to_widget()
        self.page.close_widget()

        self.driver.switch_to.default_content()

        self.page.сhoose_TommyLee_chatbot()

        self.page.go_to_list_of_triggers()

        self.page.deactivate_all_triggers()

        self.page.sorting_triggers_by_name()

        self.page.enable_FirstIntents_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)

        self.page.switch_to_widget()

        self.page.sending_search_message()

        response_message = self.page.intent_response_message()

        self.assertEqual('Комедии Л.Гайдая', response_message)
        print('Поиск по условию First Intents успешно работает')