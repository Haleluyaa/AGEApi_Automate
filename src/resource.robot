*** Settings ***
Library    RequestsLibrary
*** Variables ***
${URL}    http://www.thetestingworldapi.com
${excel_path}    


*** Keywords ***
Test Post AGEApi
    [Tags]    AGEApi template
    Create Session    PostStudentDetails    ${URL}
    ${Data}=    Create Dictionary    first_name=Hello    middle_name=K.    last_name=Gorgeous   date_of_birth=12/12/1990
    ${Header}=    Create Dictionary    Content-Type=application/json
    ${Response}    Post Request    PostStudentDetails    /api/studentsDetails    data=${Data}    headers=${Header}
    Should Be Equal As Strings    ${Response.status_code}    201
    Log To Console    ${Response.text}

Import Test Data
    Open Excel    ${excel_path}
    ${row_count}    Get Row Count    Login_valid
    Log to console    ${row_count}
    :FOR    ${i}    IN RANGE    3    ${row_count}
    \    ${usr_temp} =    Read Cell Data    Login_valid    ${i}    2       
    \    Log to console    ${usr_temp} 
    \    Append To List    ${VALID USERNAME}    ${usr_temp}                    
    \    Log to console    ${VALID USERNAME}
    \    ${ps_temp} =    Read Cell Data    Login_valid    ${i}    3    
    \    Log to console    ${ps_temp}
    \    Append To List    ${VALID PASSWORD}    ${ps_temp}     
    \    Log to console    ${VALID PASSWORD}    

    