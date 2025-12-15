*** Settings ***
Resource    ../resources/grocery_keywords.robot
Suite Teardown    Close Grocery App

*** Test Cases ***
Login And Add Item To Cart
    Open Grocery App
    Login To Grocery App
    Add Item To Cart
    Open Cart
    Verify Item In Cart
