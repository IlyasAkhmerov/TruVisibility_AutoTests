import time
from ConfigManager import ConfigManager
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
        self.driver.find_element_by_css_selector('#trutours-popup div.popover-navigation [data-role="end"]').click()

    def switch_to_widget(self):
        iframe_name = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to.frame(iframe_name)

    def close_widget(self):
        self.driver.find_element_by_css_selector('h1 > a:nth-child(4)').click()

    def go_to_list_of_chatbots(self):
        chatbotList = self.driver.find_element_by_css_selector('[href="#/chatbots"]')
        chatbotList.click()

    def create_chat_bot(self):
        addChatbotButton = self.driver.find_element_by_css_selector('button.btn-success')
        addChatbotButton.click()
        inputField = self.driver.find_element_by_css_selector('input.form-control.ng-tns-c252-5')
        time.sleep(1)
        inputField.send_keys('Testing Chatbot')
        time.sleep(1)
        chatBotTypeSelect = self.driver.find_element_by_xpath('//div/div[3]/div/div[3]/div/ul/li[2]')
        chatBotTypeSelect.click()
        time.sleep(1)
        nextButton = self.driver.find_element_by_css_selector('.btn-action')
        nextButton.click()
        time.sleep(2)
        templateChoose = self.driver.find_element_by_xpath('//div[3]/div[3]/div/ul/li[2]')
        templateChoose.click()
        time.sleep(1)
        chooseTemplateButton = self.driver.find_element_by_css_selector('.btn-action')
        chooseTemplateButton.click()
        time.sleep(4)
        finishButton = self.driver.find_element_by_css_selector('.btn.btn-action.ng-star-inserted')
        time.sleep(2)
        finishButton.click()
        time.sleep(2)

    def сhoose_TommyLee_chatbot(self):
        requiredChatbot = self.driver.find_element_by_css_selector('[title="Tommy Lee"]')
        requiredChatbot.click()

    def go_to_list_of_triggers(self):
        elementDropDown = self.driver.find_element_by_css_selector('.responsive-tabs.d-print-none button.btn.dropdown-toggle')
        elementDropDown.click()
        triggerList = self.driver.find_element_by_css_selector('[href="#/chatbots/99f61e2dcc7f4f9bb679ac9500863da9/triggers"]')
        triggerList.click()

    def enable_clickOnHTMLtag_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(1) td.active-column label input')
        checkbox.click()

    def enable_currentPageAddress_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(2) td.active-column label input')
        checkbox.click()

    def enable_currentPageAddressFragment_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(3) td.active-column label input')
        checkbox.click()

    def enable_currentPageAddressFragmentContains_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(4) td.active-column label input')
        checkbox.click()

    def enable_currentPageAddressSegment_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(5) td.active-column label input')
        checkbox.click()

    def enable_CurrentPageTitle_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(6) td.active-column label input')
        checkbox.click()

    def enable_MetaTagTruChat_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(7) td.active-column label input')
        checkbox.click()

    def enable_PageAddressFragmentChange_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(8) td.active-column label input')
        checkbox.click()

    def enable_PageLoaded_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(9) td.active-column label input')
        checkbox.click()


    def enable_RefferingWebsiteAddress_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(10) td.active-column label input')
        checkbox.click()

    def enable_TimeOnTheCurrentPageTitle_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(11) td.active-column label input')
        checkbox.click()

    def enable_UserFisrtTimeVisitor_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(13) td.active-column label input')
        checkbox.click()

    def enable_UserReturnedtoYourWebsite_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(14) td.active-column label input')
        checkbox.click()

    def enable_FAQOnly_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(15) td.active-column label input')
        checkbox.click()

    def enable_IntentsOnly_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(16) td.active-column label input')
        checkbox.click()

    def enable_FirstFAQ_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(17) td.active-column label input')
        checkbox.click()

    def enable_FirstIntents_trigger(self):
        checkbox = self.driver.find_element_by_css_selector('tr:nth-child(18) td.active-column label input')
        checkbox.click()

    def publish_chatbot(self):
        publishButton = self.driver.find_element_by_css_selector('.btn.btn-action.ng-star-inserted')
        publishButton.click()
        time.sleep(3)
        confirmButton = self.driver.find_element_by_id('alertify-ok')
        confirmButton.click()
        time.sleep(20)
        closeButton = self.driver.find_element_by_css_selector('.modal-footer.ng-star-inserted button')
        closeButton.click()

    def close_notification_window(self):
        closeNotificationButton = self.driver.find_element_by_css_selector('.modal-footer.success-footer-with-warnings.ng-star-inserted button')
        closeNotificationButton.click()

    def click_on_HTML_tag(self):
        HTMLtag = self.driver.find_element_by_css_selector('.html-container p span')
        HTMLtag.click()

    def wellcome_message(self):
        return self.driver.find_element_by_css_selector('.msg-text-content p').text

    def go_to_page_one(self):
        page_one = self.driver.find_element_by_css_selector('[href="/home/page1"]')
        page_one.click()

    def go_to_page_two(self):
        page_two = self.driver.find_element_by_css_selector('[href="/home/page2"]')
        page_two.click()

    def go_to_page_three(self):
        page_three = self.driver.find_element_by_css_selector('[href="/home/page3"]')
        page_three.click()

    def click_sadbot_link(self):
        sadbot_link = self.driver.find_element_by_css_selector('[href="#sadbot"]')
        sadbot_link.click()

    def click_demo_link(self):
        sadbot_link = self.driver.find_element_by_css_selector('[href="#demo"]')
        sadbot_link.click()

    def sorting_triggers_by_name(self):
        sorting_by_name = self.driver.find_element_by_css_selector('.name-column[data-sortable="name"]')
        sorting_by_name.click()

    def deactivate_all_triggers(self):
        select_all_checkboxes = self.driver.find_element_by_css_selector('thead input')
        select_all_checkboxes.click()
        time.sleep(1)
        bulkactions_menu = self.driver.find_element_by_css_selector('button.mass-action')
        bulkactions_menu.click()
        time.sleep(1)
        deactivate_all = self.driver.find_element_by_xpath('//chatbot-train-header/div/ul/li[2]')
        deactivate_all.click()
        time.sleep(2)
        warning_message = self.driver.find_element_by_css_selector('p.alertify-message')
        confirmButton = self.driver.find_element_by_id('alertify-ok')
        time.sleep(3)
        if warning_message.text == 'Are you sure you want to deactivate the 22 trigger(s)?':
            confirmButton.click()
            time.sleep(2)
        else:
            print(warning_message.text)

    def review_message(self):
        return self.driver.find_element_by_css_selector('chatbot-review-dialog h4').text

    def review_popup_close(self):
        review_popup_close_button = self.driver.find_element_by_css_selector('.close-btn.btn')
        review_popup_close_button.click()

    def sending_search_message(self):
        self.driver.find_element_by_css_selector('textarea#msg-box').send_keys('Шурик')
        self.driver.find_element_by_css_selector('#msg-submit').click()

    def faq_response_message(self):
        return self.driver.find_element_by_css_selector('li:nth-child(1)').text

    def intent_response_message(self):
        return self.driver.find_element_by_css_selector('[data-content="Комедии Л.Гайдая"] p').text

    def go_to_list_of_scripts(self):
        elementDropDown = self.driver.find_element_by_css_selector('.responsive-tabs.d-print-none button.btn.dropdown-toggle')
        elementDropDown.click()
        time.sleep(1)
        scriptList = self.driver.find_element_by_css_selector('chatbot-menu > div > div > ul > li:nth-child(3)')
        scriptList.click()

    def add_written_review(self):
        reviewArea = self.driver.find_element_by_css_selector('.modal-body textarea')
        reviewArea.send_keys('Great template!')
        rateTemplate = self.driver.find_element_by_css_selector('stars span:nth-child(5)')
        rateTemplate.click()
        submitReview = self.driver.find_element_by_css_selector('.review-footer button.btn.btn-primary')
        submitReview.click()




