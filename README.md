#  Hands-On Web App Test Automation tutorial taught by Andrew "Pandy" Knight for PyCon 2020. 

 1.  pipenv install pytest
 2.  pipenv install selenium

## Section 1: Setting Up pytest With Our First Test

 1. created tests folder
 2. created test_search.py  
    
    RUN > pipenv run python -m pytest

## Section 2: Setting Up Selenium WebDriver
 
 1. created conftest.py
 2. here I didn't followed Andy's approach - used Webdriver Manager for Python instead:
 pipenv install webdriver-manager

    RUN > pipenv run python -m pytest

## Section 3: Defining Page Objects

 1.  created a new Python package > pages.
 2.  created __init__.py
 3.  created search page
 4.  created resullts page

    RUN > pipenv run python -m pytest

## Section 4: Finding Locators for Elements

1. add the search input locator to the search_page
2. import By class from the module selenium.webdriver.common.by
3. add the locators to the result page

    RUN > pipenv run python -m pytest

## Section 5: Making WebDriver Calls

 1.  implement all the page object methods  

    RUN > pipenv run python -m pytest
