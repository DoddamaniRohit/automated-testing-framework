*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${APP_URL}    http://localhost:8000/student_page.html

*** Keywords ***
Open Browser To App
    Open Browser    ${APP_URL}    firefox
    Maximize Browser Window

Close Browser Session
    Close All Browsers

