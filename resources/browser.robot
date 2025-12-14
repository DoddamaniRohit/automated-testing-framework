*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    chrome
${BASE_URL}   http://localhost:8000/student_page.html

*** Keywords ***
Open Browser To App
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
