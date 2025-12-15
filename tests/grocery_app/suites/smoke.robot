*** Settings ***
Resource    ../resources/grocery_keywords.robot
Suite Teardown    Close Grocery App

*** Test Cases ***
Open Grocery Home Page
    Open Grocery App
    Title Should Be    Swag Labs
