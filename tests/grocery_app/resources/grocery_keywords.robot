*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://www.saucedemo.com
${BROWSER}    firefox
${USERNAME}   standard_user
${PASSWORD}   secret_sauce

*** Keywords ***
Open Grocery App
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Login To Grocery App
    Input Text    id:user-name    ${USERNAME}
    Input Text    id:password     ${PASSWORD}
    Click Button  id:login-button

Add Item To Cart
    Click Button    xpath://button[contains(text(),'Add to cart')]

Open Cart
    Click Element   class:shopping_cart_link

Verify Item In Cart
    Page Should Contain Element    class:cart_item

Close Grocery App
    Close All Browsers
