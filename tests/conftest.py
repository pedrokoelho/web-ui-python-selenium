"""
This module contains shared fixtures.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():

  # Initialize the ChromeDriver instance
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

  # Make its calls wait up to 10 seconds for elements to appear
  driver.implicitly_wait(20)

  # Return the WebDriver instance for the setup
  yield driver

  # Quit the WebDriver instance for the cleanup
  driver.quit()