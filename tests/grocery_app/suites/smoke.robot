*** Settings ***
Resource    ../resources/grocery_keywords.robot
Suite Teardown    Close All Browsers

*** Test Cases ***
Open Grocery Home Page
    Open Grocery App
    Title Should Be    Swag Labs
