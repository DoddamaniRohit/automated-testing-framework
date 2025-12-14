*** Settings ***
Resource    ../resources/student_keywords.robot
Resource    ../../../resources/browser.robot

*** Test Cases ***
Add Student - Happy Path
    Open Browser To App
    Create Student    John Doe    20    BCA
    Student Should Appear In List    John Doe


Check Add Student Form Appears
    Open Browser To App
    Click Element    id:add-student
    Wait Until Element Is Visible    id:submit    timeout=3s
