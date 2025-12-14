*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${APP_URL}    http://localhost:8000/student_page.html

*** Keywords ***
Open Browser To App
    Open Browser
    ...    ${APP_URL}
    ...    chrome
    ...    options=add_argument=--headless,new;add_argument=--no-sandbox;add_argument=--disable-dev-shm-usage;add_argument=--window-size=1920,1080

Close Browser Session
    Close All Browsers
