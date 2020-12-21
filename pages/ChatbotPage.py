import time
from ConfigManager import ConfigManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class ChatbotPage:
    def __init__(self, driver) -> None:
        super().__init__()

        self.driver = driver


    def login_on_the_website(self):
        userNameField = self.driver.find_element_by_id('inputEmail')
        passwordField = self.driver.find_element_by_id('inputPassword')

        config = ConfigManager.get_config()
        login = config.login
        password = config.password

        userNameField.send_keys(login)
        passwordField.send_keys(password)

        signInButton = self.driver.find_element_by_class_name('btn-sign-in')
        signInButton.click()

    def close_product_tour(self):
        wait = WebDriverWait(self.driver, 10)
        productTour = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#trutours-popup div.popover-navigation [data-role="end"]')))
        productTour.click()

    def switch_to_widget(self):
        iframe_name = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to.frame(iframe_name)

    def close_widget(self):
        wait = WebDriverWait(self.driver, 10)
        closeWidgetButton = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1 > a:nth-child(4)')))
        closeWidgetButton.click()

    def go_to_list_of_chatbots(self):
        wait = WebDriverWait(self.driver, 10)
        chatbotList = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="#/chatbots"]')))
        chatbotList.click()

    def create_chat_bot(self):
        addChatbotButton = self.driver.find_element_by_css_selector('button.btn-success')
        addChatbotButton.click()
        wait = WebDriverWait(self.driver, 10)
        inputField = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.form-control.ng-tns-c252-5')))
        inputField.send_keys('Testing Chatbot')
        chatBotTypeSelect = self.driver.find_element_by_xpath('//div/div[3]/div/div[3]/div/ul/li[2]')
        chatBotTypeSelect.click()
        nextButton = self.driver.find_element_by_css_selector('.btn-action')
        nextButton.click()
        wait = WebDriverWait(self.driver, 10)
        templateChoose = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/div[3]/div/ul/li[2]')))
        templateChoose.click()
        chooseTemplateButton = self.driver.find_element_by_css_selector('.btn-action')
        chooseTemplateButton.click()
        wait = WebDriverWait(self.driver, 10)
        finishButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-action.ng-star-inserted')))
        finishButton.click()
        time.sleep(3)

    def сhoose_TommyLee_chatbot(self):
        wait = WebDriverWait(self.driver, 10)
        requiredChatbot = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="Tommy Lee"]')))
        requiredChatbot.click()

    def go_to_list_of_triggers(self):
        wait = WebDriverWait(self.driver, 10)
        elementDropDown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.responsive-tabs.d-print-none button.btn.dropdown-toggle')))
        elementDropDown.click()
        wait = WebDriverWait(self.driver, 10)
        triggerList = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="#/chatbots/99f61e2dcc7f4f9bb679ac9500863da9/triggers"]')))
        triggerList.click()

    def enable_clickOnHTMLtag_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(1) td.active-column label input')))
        checkbox.click()

    def enable_currentPageAddress_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(2) td.active-column label input')))
        checkbox.click()

    def enable_currentPageAddressFragment_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(3) td.active-column label input')))
        checkbox.click()

    def enable_currentPageAddressFragmentContains_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(4) td.active-column label input')))
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(4) td.active-column label input')
        checkbox.click()

    def enable_currentPageAddressSegment_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(5) td.active-column label input')))
        checkbox.click()

    def enable_CurrentPageTitle_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(6) td.active-column label input')))
        checkbox.click()

    def enable_MetaTagTruChat_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(7) td.active-column label input')))
        checkbox.click()

    def enable_PageAddressFragmentChange_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(8) td.active-column label input')))
        checkbox.click()

    def enable_PageLoaded_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(9) td.active-column label input')))
        checkbox.click()

    def enable_RefferingWebsiteAddress_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(10) td.active-column label input')))
        checkbox.click()

    def enable_TimeOnTheCurrentPageTitle_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(11) td.active-column label input')))
        checkbox.click()

    def enable_UserFisrtTimeVisitor_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(13) td.active-column label input')))
        checkbox.click()

    def enable_UserReturnedtoYourWebsite_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(14) td.active-column label input')))
        checkbox.click()

    def enable_FAQOnly_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(15) td.active-column label input')))
        checkbox.click()

    def enable_IntentsOnly_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(16) td.active-column label input')))
        checkbox.click()

    def enable_FirstFAQ_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(17) td.active-column label input')))
        checkbox.click()

    def enable_FirstIntents_trigger(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(18) td.active-column label input')))
        checkbox.click()

    def publish_chatbot(self):
        wait = WebDriverWait(self.driver, 10)
        publishButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-action.ng-star-inserted')))
        publishButton.click()
        wait = WebDriverWait(self.driver, 10)
        confirmButton = wait.until(EC.element_to_be_clickable((By.ID, 'alertify-ok')))
        confirmButton.click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.title.success-dialog-title.ng-star-inserted')))
        closeButton = self.driver.find_element_by_css_selector('.modal-footer.ng-star-inserted button')
        closeButton.click()

    def close_notification_window(self):
        closeNotificationButton = self.driver.find_element_by_css_selector('.modal-footer.success-footer-with-warnings.ng-star-inserted button')
        closeNotificationButton.click()

    def click_on_HTML_tag(self):
        HTMLtag = self.driver.find_element_by_css_selector('.html-container p span')
        HTMLtag.click()

    def wellcome_message(self):
        wait = WebDriverWait(self.driver, 20)
        wellcomeMessage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.msg-text-content p')))
        return wellcomeMessage.text
        print(wellcomeMessage.text)

    def go_to_page_one(self):
        page_one = self.driver.find_element_by_css_selector('[href="/home/page1"]')
        page_one.click()

    def go_to_page_two(self):
        wait = WebDriverWait(self.driver, 10)
        page_two = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="/home/page2"]')))
        page_two.click()

    def go_to_page_three(self):
        wait = WebDriverWait(self.driver, 10)
        page_three = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="/home/page3"]')))
        page_three.click()

    def click_sadbot_link(self):
        wait = WebDriverWait(self.driver, 10)
        sadbot_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="#sadbot"]')))
        sadbot_link.click()

    def click_demo_link(self):
        wait = WebDriverWait(self.driver, 10)
        demo_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="#demo"]')))
        demo_link.click()

    def sorting_triggers_by_name(self):
        wait = WebDriverWait(self.driver, 10)
        sorting_by_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.name-column[data-sortable="name"]')))
        sorting_by_name.click()

    def deactivate_all_triggers(self):
        wait = WebDriverWait(self.driver, 10)
        select_all_checkboxes = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'thead input')))
        select_all_checkboxes.click()
        bulkactions_menu = self.driver.find_element_by_css_selector('button.mass-action')
        bulkactions_menu.click()
        deactivate_all = self.driver.find_element_by_xpath('//chatbot-train-header/div/ul/li[2]')
        deactivate_all.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.alertify-message')))
        warning_message = self.driver.find_element_by_css_selector('p.alertify-message')
        confirmButton = self.driver.find_element_by_id('alertify-ok')
        time.sleep(3)
        if warning_message.text == 'Are you sure you want to deactivate the 22 trigger(s)?':
            confirmButton.click()
            time.sleep(2)
        else:
            print(warning_message.text)

    def review_message(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'chatbot-review-dialog h4')))
        return self.driver.find_element_by_css_selector('chatbot-review-dialog h4').text

    def review_popup_close(self):
        wait = WebDriverWait(self.driver, 10)
        review_popup_close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.close-btn.btn')))
        review_popup_close_button.click()

    def sending_search_message(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea#msg-box')))
        self.driver.find_element_by_css_selector('textarea#msg-box').send_keys('Шурик')
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#msg-submit')))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#msg-submit')))
        self.driver.find_element_by_css_selector('#msg-submit').click()

    def faq_response_message(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li:nth-child(1)')))
        return self.driver.find_element_by_css_selector('li:nth-child(1)').text

    def intent_response_message(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-content="Комедии Л.Гайдая"] p')))
        return self.driver.find_element_by_css_selector('[data-content="Комедии Л.Гайдая"] p').text

    def go_to_list_of_scripts(self):
        elementDropDown = self.driver.find_element_by_css_selector('.responsive-tabs.d-print-none button.btn.dropdown-toggle')
        elementDropDown.click()
        time.sleep(1)
        scriptList = self.driver.find_element_by_css_selector('chatbot-menu > div > div > ul > li:nth-child(3)')
        scriptList.click()

    def add_written_review(self):
        wait = WebDriverWait(self.driver, 10)
        reviewArea = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal-body textarea')))
        reviewArea.send_keys('Great template!')
        rateTemplate = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'stars span:nth-child(5)')))
        rateTemplate.click()
        submitReview = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.review-footer button.btn.btn-primary')))
        submitReview.click()




