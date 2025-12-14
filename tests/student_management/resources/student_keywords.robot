*** Settings ***
Resource    ../../../resources/browser.robot
Library    SeleniumLibrary

*** Keywords ***
Go To Student Page
    Go To    ${BASE_URL}

Create Student
    [Arguments]    ${name}    ${age}    ${course}
    Click Element    id:add-student
    Input Text       id:name        ${name}
    Input Text       id:age         ${age}
    Select From List By Value    id:course    ${course}
    Click Button    id:submit

Student Should Appear In List
    [Arguments]    ${name}
    Wait Until Page Contains    ${name}    timeout=5s
