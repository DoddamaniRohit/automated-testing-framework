*** Settings ***
Resource    ../resources/student_keywords.robot
Variables    ${EXECDIR}/tests/student_management/data/students_vars.py


*** Test Cases ***
Add Students From CSV
    [Documentation]    Reads all rows from students.csv and creates each student
    FOR    ${row}    IN    @{STUDENTS}
        ${name}=    Set Variable    ${row}[0]
        ${age}=     Set Variable    ${row}[1]
        ${course}=  Set Variable    ${row}[2]
        Open Browser To App
        Create Student    ${name}    ${age}    ${course}
        Student Should Appear In List    ${name}
        Close All Browsers
    END
