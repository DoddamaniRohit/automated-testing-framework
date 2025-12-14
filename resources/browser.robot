*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn

*** Variables ***
${APP_URL}    http://localhost:8000/student_page.html

*** Keywords ***
Open Browser To App
    Wait Until Keyword Succeeds    5x    2s    Open Browser    ${APP_URL}    firefox    headless=True
    Maximize Browser Window

Close Browser Session
    Close All Browsers
