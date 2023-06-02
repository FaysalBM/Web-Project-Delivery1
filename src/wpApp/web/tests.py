import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class EndToEndTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()  

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_create_company(self):
        # Log in on the login page
        self.selenium.get(self.live_server_url + '/login')
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('your_username')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('your_password')
        password_input.send_keys(Keys.ENTER)

        # Navigate to the create company page
        self.selenium.get(self.live_server_url + '/create-company')

        # Fill out the create company form
        name_input = self.selenium.find_element_by_name('name')
        name_input.send_keys('Test Company')
        email_input = self.selenium.find_element_by_name('email_com')
        email_input.send_keys('test@example.com')
        num_workers_input = self.selenium.find_element_by_name('num_workers')
        num_workers_input.send_keys('10')
        num_workers_input.send_keys(Keys.ENTER)

        # Verify that the company has been created
        success_message = self.selenium.find_element_by_css_selector('.messages .success')
        self.assertEqual(success_message.text, 'Test Company has been created.')
    
    def test_create_company2(self):
        # Log in on the login page
        self.selenium.get(self.live_server_url + '/login')
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('your_username')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('your_password')
        password_input.send_keys(Keys.ENTER)

        # Navigate to the create company page
        self.selenium.get(self.live_server_url + '/create-company')

        # Fill out the create company form
        name_input = self.selenium.find_element_by_name('name')
        name_input.send_keys('Test Company')
        email_input = self.selenium.find_element_by_name('email_com')
        email_input.send_keys('test@example.com')
        num_workers_input = self.selenium.find_element_by_name('num_workers')
        num_workers_input.send_keys('10')
        num_workers_input.send_keys(Keys.ENTER)

        # Verify that the company has been created
        success_message = self.selenium.find_element_by_css_selector('.messages .success')
        self.assertEqual(success_message.text, 'Test Company has been created.')

    def test_add_user_to_company(self):
        # Log in on the login page
        self.selenium.get(self.live_server_url + '/login')
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('your_username')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('your_password')
        password_input.send_keys(Keys.ENTER)

        # Navigate to the company detail page
        self.selenium.get(self.live_server_url + '/company/1')  # Replace '1' with the company ID

        # Add a user to the company
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('user123')
        username_input.send_keys(Keys.ENTER)

        # Verify that the user has been added successfully
        success_message = self.selenium.find_element_by_css_selector('.messages .success')
        self.assertEqual(success_message.text, 'user123 has been added to Test Company.')

    def test_create_project(self):
        # Log in on the login page
        self.selenium.get(self.live_server_url + '/login')
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('your_username')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('your_password')
        password_input.send_keys(Keys.ENTER)

        # Navigate to the department detail page
        self.selenium.get(self.live_server_url + '/department/1/company/1')  # Replace '1' with the department ID and company ID

        # Create a new project
        self.selenium.find_element_by_css_selector('.create-project-button').click()
        project_name_input = self.selenium.find_element_by_name('name')
        project_name_input.send_keys('Test Project')
        project_description_input = self.selenium.find_element_by_name('description')
        project_description_input.send_keys('This is a test project.')
        project_name_input.send_keys(Keys.ENTER)

        # Verify that the project has been created
        success_message = self.selenium.find_element_by_css_selector('.messages .success')
        self.assertEqual(success_message.text, 'Test Project has been created.')

    def test_complete_project(self):
        # Log in on the login page
        self.selenium.get(self.live_server_url + '/login')
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('your_username')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('your_password')
        password_input.send_keys(Keys.ENTER)

        # Navigate to the project detail page
        self.selenium.get(self.live_server_url + '/project/1/department/1/company/1')  # Replace '1' with the project ID, department ID, and company ID

        # Complete the project
        self.selenium.find_element_by_css_selector('.complete-project-button').click()

        # Verify that the project is marked as completed
        project_status = self.selenium.find_element_by_css_selector('.project-status')
        self.assertEqual(project_status.text, 'Completed')

    def test_delete_company(self):
        # Log in on the login page
        self.selenium.get(self.live_server_url + '/login')
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('your_username')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('your_password')
        password_input.send_keys(Keys.ENTER)

        # Navigate to the company detail page
        self.selenium.get(self.live_server_url + '/company/1')  # Replace '1' with the company ID

        # Delete the company
        self.selenium.find_element_by_css_selector('.delete-company-button').click()
        self.selenium.switch_to.alert.accept()

        # Verify that the company has been deleted
        success_message = self.selenium.find_element_by_css_selector('.messages .success')
        self.assertEqual(success_message.text, 'Test Company has been deleted.')





