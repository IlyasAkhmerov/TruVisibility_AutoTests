import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ConfigManager import ConfigManager
from pages.ChatbotPage import ChatbotPage

# _________________________________________________________________________________
# В тесте проверяется старт чатбота на тестовой странице при соблюдении определенных условий.
# Сценарий теста:
# 1.Пользователь авторизируется на сайте
# 2.Выбирает необходимого чатбота
# 3.Активирует один из его триггеров
# 4.Публикует чатбота
# 5.Переходит на тестовую страницу
# 6.Выполняет условия для срабатывания триггера
# 7.Проверяет, что чат запускается

# Предварительные условия:
# 1.Чатбот активирован
# 2.Все триггеры отключены
# _________________________________________________________________________________

class StartChatbotTestCases(unittest.TestCase):
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

    def test_StartChatbotTrigger_ClickOnHTML_ChatIsStarting(self):  # Старт чатбота по триггеру Click on HTMl tag

        self.page.login_on_the_website()

        self.page.close_product_tour()


        self.page.go_to_list_of_chatbots()

        self.page.switch_to_widget()
        self.page.close_widget()

        self.driver.switch_to.default_content()

        self.page.сhoose_TommyLee_chatbot()

        self.page.go_to_list_of_triggers()

        self.page.sorting_triggers_by_name()

        self.page.enable_clickOnHTMLtag_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)
        time.sleep(5)

        self.page.click_on_HTML_tag()

        self.page.switch_to_widget()

        find_wellcome_message = self.page.wellcome_message()

        self.assertEqual('Поздравляю! Тест запуска сеанса чата по стартовому условию "Click on HTML Tag" прошел успешно!', find_wellcome_message)

    def test_StartChatbotTrigger_CurrentPageAddress_ChatIsStarting(self): # Старт чатбота по триггеру Current Page Address

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

        self.page.enable_currentPageAddress_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)

        self.page.go_to_page_two()
        time.sleep(5)

        self.page.switch_to_widget()

        find_wellcome_message = self.page.wellcome_message()

        self.assertEqual('Поздравляю! Тест запуска сеанса чата по стартовому условию "Current page address" прошел успешно!', find_wellcome_message)

    def test_StartChatbotTrigger_CurrentPageAddressFragment_ChatIsStarting(self): # Старт чатбота по триггеру Current Page Address Fragment

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

        self.page.enable_currentPageAddressFragment_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)
        time.sleep(5)

        self.page.click_sadbot_link()
        time.sleep(5)

        self.page.switch_to_widget()

        find_wellcome_message = self.page.wellcome_message()

        self.assertEqual('Поздравляю! Тест запуска сеанса чата по стартовому условию "Current page address fragment" прошел успешно!', find_wellcome_message)

    def test_StartChatbotTrigger_CurrentPageAddressFragmentContains_ChatIsStarting(self): # Старт чатбота по триггеру Current Page Address Fragment Contains

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

        self.page.enable_currentPageAddressFragmentContains_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)
        time.sleep(5)

        self.page.click_demo_link()

        self.page.switch_to_widget()

        find_wellcome_message = self.page.wellcome_message()

        self.assertEqual('Поздравляю! Тест запуска сеанса чата по стартовому условию "Current page address fragment contains" прошел успешно!', find_wellcome_message)

    def test_StartChatbotTrigger_CurrentPageAddressSegment_ChatIsStarting(self): # Старт чатбота по триггеру Current Page Address Segment

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

        self.page.enable_currentPageAddressSegment_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)

        self.page.go_to_page_two()

        self.page.switch_to_widget()

        find_wellcome_message = self.page.wellcome_message()

        self.assertEqual('Поздравляю! Тест запуска сеанса чата по стартовому условию "Current page address segment" прошел успешно!', find_wellcome_message)

    def test_StartChatbotTrigger_CurrentPageTitle_ChatIsStarting(self): # Старт чатбота по триггеру Current page title

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

        self.page.enable_CurrentPageTitle_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)

        self.page.go_to_page_three()

        self.page.switch_to_widget()

        find_wellcome_message = self.page.wellcome_message()

        self.assertEqual('Поздравляю! Тест запуска сеанса чата по стартовому условию "Current page title" прошел успешно!', find_wellcome_message)

    def test_StartChatbotTrigger_MetaTagTruChat_ChatIsStarting(self): # Старт чатбота по триггеру Meta tag TruChat

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

        self.page.enable_MetaTagTruChat_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)

        self.page.switch_to_widget()

        find_wellcome_message = self.page.wellcome_message()

        self.assertEqual('Поздравляю! Тест запуска сеанса чата по стартовому условию "Meta tag TruCHAT" прошел успешно!', find_wellcome_message)

    def test_StartChatbotTrigger_CurrentPageAddressFragmentChange_ChatIsStarting(self): # Старт чатбота по триггеру Page Address Fragment Change

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

        self.page.enable_PageAddressFragmentChange_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)

        self.page.click_demo_link()
        time.sleep(3)

        self.page.click_sadbot_link()
        time.sleep(3)

        self.page.switch_to_widget()

        find_wellcome_message = self.page.wellcome_message()

        self.assertEqual('Поздравляю! Тест запуска сеанса чата по стартовому условию "Page address fragment change" прошел успешно!', find_wellcome_message)

    def test_StartChatbotTrigger_PageLoaded_ChatIsStarting(self): # Старт чатбота по триггеру Page Loaded

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

        self.page.enable_PageLoaded_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)
        time.sleep(5)

        self.page.switch_to_widget()

        find_wellcome_message = self.page.wellcome_message()

        self.assertEqual('Поздравляю! Тест запуска сеанса чата по стартовому условию "Page loaded" прошел успешно!', find_wellcome_message)

    def test_StartChatbotTrigger_RefferingWebsiteAddress_ChatIsStarting(self): # Старт чатбота по триггеру Reffering Website Address

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

        self.page.enable_RefferingWebsiteAddress_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)

        self.page.go_to_page_two()

        self.page.go_to_page_one()

        self.page.switch_to_widget()

        find_wellcome_message = self.page.wellcome_message()

        self.assertEqual('Поздравляю! Тест запуска сеанса чата по стартовому условию "Referring website address" прошел успешно!', find_wellcome_message)

    def test_StartChatbotTrigger_TimeOnTheCurrentPage_ChatIsStarting(self): # Старт чатбота по триггеру Time On The Current Page

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

        self.page.enable_TimeOnTheCurrentPageTitle_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)

        self.page.switch_to_widget()

        find_wellcome_message = self.page.wellcome_message()

        self.assertEqual('Поздравляю! Тест запуска сеанса чата по стартовому условию "Time on the current page" прошел успешно!', find_wellcome_message)

    def test_StartChatbotTrigger_UserFisrtTimeVisitor_ChatIsStarting(self): # Старт чатбота по триггеру User Is A First-time Visitor

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

        self.page.enable_UserFisrtTimeVisitor_trigger()

        self.page.publish_chatbot()

        config = ConfigManager.get_config()

        self.driver.get(config.testpage_url)

        self.page.switch_to_widget()

        find_wellcome_message = self.page.wellcome_message()

        self.assertEqual('Поздравляю! Тест запуска сеанса чата по стартовому условию "User is a first-time visitor" прошел успешно!', find_wellcome_message)
