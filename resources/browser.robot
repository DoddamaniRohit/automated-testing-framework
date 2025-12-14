*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Browser To App
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method   ${options}    add_argument    --headless=new
    Call Method   ${options}    add_argument    --no-sandbox
    Call Method   ${options}    add_argument    --disable-dev-shm-usage
    Call Method   ${options}    add_argument    --disable-gpu
    Call Method   ${options}    add_argument    --window-size=1920,1080

    Create Webdriver    Chrome    options=${options}
    Go To    http://localhost:8000/student_page.html
