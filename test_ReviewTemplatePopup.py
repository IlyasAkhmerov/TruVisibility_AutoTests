import unittest
import time
from selenium import webdriver

from ConfigManager import ConfigManager
from pages.ChatbotPage import ChatbotPage

# _________________________________________________________________________________

# В тесте происходит проверка появления всплывающего окна, предлагающего пользователю оценить используемый шаблон чатбота и оставить комментарий
# Сценарии теста:
# Тест 1.
# 1.Пользователь авторизируется на сайте
# 2.Создает чатбота
# 3.Публикует его 3 раза подряд, после чего появляется всплывающее окно для ревью шаблона
# 4.Закрывает его и публикует чатбота ещё 6 раз подряд, после чего снова появляется всплывающее окно ревью
# 5.Далее происходит еще 12, а затем 24 публикации,  после которых также должно появиться всплывающее окно ревью
#
# Тест 2
# 1.Пользователь авторизируется на сайте
# 2.Создает чатбота
# 3.Публикует его 3 раза подряд, после чего появляется всплывающее окно для ревью шаблона
# 4.Пользователь оставляет комментарий и оценивает шаблон
# 5.Пользователь публикует чатбота еще 6 раз и убеждается, что всплывающее окно ревью больше не появляется

# -------------------------------------------------------------------------------------

class ReviewPopUpTestCases(unittest.TestCase):
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

    def test_ReviewPopUp_PublishChatbot_ReviewPopUpsAppearance(self):  # Появление Review popups после определенного количества публикаций

        self.page.login_on_the_website()

        self.page.close_product_tour()

        self.page.go_to_list_of_chatbots()

        self.page.switch_to_widget()
        self.page.close_widget()

        self.driver.switch_to.default_content()

        self.page.create_chat_bot()

        a = 0
        while a <= 2:
            self.page.publish_chatbot()
            a += 1

        find_review_message = self.page.review_message()
        time.sleep(2)

        self.assertEqual('Review This Template', find_review_message)

        self.page.review_popup_close()

        print('Review после 3 публикации успешно появилось')

        a = 0
        while a <= 5:
            self.page.publish_chatbot()
            a += 1

        find_review_message = self.page.review_message()
        time.sleep(2)

        self.assertEqual('Review This Template', find_review_message)

        self.page.review_popup_close()

        print('Review после 6 публикации успешно появилось')

        a = 0
        while a <= 11:
            self.page.publish_chatbot()
            a += 1

        time.sleep(5)

        find_review_message = self.page.review_message()

        self.assertEqual('Review This Template', find_review_message)

        self.page.review_popup_close()

        print('Review после 12 публикации успешно появилось')

        a = 0
        while a <= 23:
            self.page.publish_chatbot()
            a += 1

        find_review_message = self.page.review_message()
        time.sleep(2)

        self.assertEqual('Review This Template', find_review_message)

        self.page.review_popup_close()

        print('Review после 24 публикации успешно появилось')

        print('Congratulations!')

    def test_ReviewPopUp_SendReviewMessage_PopupReviewDoesNotAppear(self):  # Проверка появления попап для ревью после того, как шаблон был оценен

        self.page.login_on_the_website()

        self.page.close_product_tour()

        self.page.go_to_list_of_chatbots()

        self.page.switch_to_widget()
        self.page.close_widget()

        self.driver.switch_to.default_content()

        self.page.create_chat_bot()

        a = 0
        while a <= 2:
            self.page.publish_chatbot()
            a += 1

        find_review_message = self.page.review_message()
        time.sleep(2)

        self.assertEqual('Review This Template', find_review_message)

        self.page.add_written_review()

        print('Review после 3 публикации успешно появилось, отзыв оставлен')

        a = 0
        while a <= 6:
            self.page.publish_chatbot()
            time.sleep(1)
            a += 1

        time.sleep(5)

        print('Review больше не появляется')














