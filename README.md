# Clinic Appointment Management System README
# Fidella Wu, Jacob Durham
# CS340 - Introduction to Databases Spring 2025

# Clinic_appointment_managment_system
# Database with patient, test, appointment, and clinic entities for managing patient, appointment, and test information.

# Citations: 

# app.py:
    Citation for initilizing/creating the base app.py. The routes for home, clinics, appointments, patients, statuses, tests, results, and patients were adapted from this starter code.  
    Scope: Module
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948
    Date: 5/2/2025
    
    Citation for query parameters
    Scope: Line
    Originality: Adapted
    Source URL: https://www.geeksforgeeks.org/get-request-query-parameters-with-flask/
    Date: 5/4/2025
    
    Citation for url_for and request.referrer from Flask documentation
    Scope: Line
    Originality: Adapted
    Source URL: https://flask.palletsprojects.com/en/stable/api/#flask.url_for
    Source URL: https://flask.palletsprojects.com/en/stable/api/#flask.Request.referrer
    Date: 5/20/2025
    
    Citation for Flask CUD routes. All CUD routes for all entities were adapted from this starter code.
    Scope: Module
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
    Date: 5/20/2025
    
    Citation for traceback.print_exc() and traceback, used for debugging in cud routes
    Scope: Line
    Originality: Adapted
    Source URL: https://www.geeksforgeeks.org/traceback-in-python/
    Date: 5/20/2025
    
    Citation for upper function
    Scope: Line
    Originality: Adapted
    Source URL: https://www.w3schools.com/python/ref_string_upper.asp
    Date: 5/21/2025


# db_connector.py
    Citation for creating db_connector.py, this code was adapted from this starter code 
    Scope: Module
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948
    Date: 5/2/2025

    Citation for environment variables. We used personal .env files so each partner was able to use their own SQL database and no password sharing was necessary.  
    Scope: Line, 23, 27-29
    Originality: Adapted
    Source URL: https://www.geeksforgeeks.org/using-python-environment-variables-with-python-dotenv/
    Date: 5/2/2025


# script.js
    Citation for JS event listeners used for clicking on buttons 
    Scope: Function
    Originality: Adapted
    Source URL: https://www.w3schools.com/js/js_htmldom_eventlistener.asp
    Date: 5/3/2025

    Citation for JS window location
    Scope: Function
    Originality: Adapted
    Source URL: https://www.w3schools.com/js/js_window_location.asp
    Date: 5/4/2025

    Citation for JS Split and Slice
    Scope: Line, 38
    Originality: Adapted
    Source URL: https://www.w3schools.com/jsref/jsref_split.asp
    Source URL: https://www.w3schools.com/jsref/jsref_slice_string.asp
    Date: 5/4/2025 

# style.css
    Background linear-gradient CSS from Figma (designed a quick mock-up on Figma before starting)
    Scope: Line, 36
    Originality: Copied
    Scope: line
    Source URL: https://www.figma.com/design/WTIOoszjA8Vfy5YqaH8thE/Clinic-Appointment-Management-System?node-id=0-1&t=PDZH46iJw7UdrU8R-1
    Date: 5/1/2025

    citation for creating the popups for create, update, delete, and reset
    Scope: function
    Originality: Adapted
    Source URL: https://www.w3schools.com/howto/howto_css_modals.asp
    Date: 5/2/2025

    citation for base table styling
    Scope: function
    Originality: Adapted
    Source URL: https://www.w3schools.com/css/css_table.asp
    Date: 5/2/2025

    All other CSS styling and design is original. 

# appointments.j2
    citation for creating the base template page, most of the this page was adapted from this starter code
    scope: Module
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948
    Date: 5/2/2025

    citation for url_for from Flask documentation
    Scope: Line, 64
    Originality: Adapted
    Source URL: https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_for
    Date: 5/4/2025

    citation for creating, updating, and deleting from appointments
    Scope: Line,  89
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
    Date: 5/20/2025

    citation for html tooltips, used in our edit and delete buttons
    Scope: Line, 64, 67
    Originality: Adapted
    source URL: https://www.geeksforgeeks.org/what-is-a-tooltip-in-html/
    Date: 5/28/2025

# clinics.j2
    citation for creating the base template page, most of this page was adapted from this start code
    Scope: Module
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948
    Date: 5/2/2025

    citation for url_for from Flask documentation
    Scope: Line, 70
    Originality: Adapted
    Source URL: https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_for
    Date: 5/4/2025

    citation for creating, updating, and deleting from clinics
    Scope: Line, 95
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
    Date: 5/20/2025

    citation for html tooltips, used in our edit and delete buttons
    Scope: Line, 70, 73
    Originality: Adapted
    source URL: https://www.geeksforgeeks.org/what-is-a-tooltip-in-html/
    Date: 5/28/2025

    citation for html input size used on phone number input
    Scope: Line, 121
    Originality: Adapted
    Source URL: https://www.w3schools.com/tags/att_input_size.asp
    Date: 6/6/2025

# home.j2
    citation for creating the base home template page, this page was entirely adapted from the starter code 
    Scope: Module
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948
    Date: 5/2/2025

# main.j2
    citation for creating the base main template page, most of this page was adapted from the start code 
    Scope: Module
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948
    Date: 5/2/2025

    citation for Lato font
    Scope: Line, 32-34
    Source URL: https://fonts.google.com/specimen/Lato
    Date: 5/2/2025

    Citation for material symbols icons (close, delete, edit)
    Scope: Line, 38, Icons are implemented on each template page.  
    Source URL: https://fonts.google.com/icons
    Date: 5/2/2025

# patients.j2
    citation for creating the base template page, most of this page was adapted from this starter code 
    Scope: Module
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948
    Date: 5/2/2025

    citation for url_for from Flask documentation
    Scope: Line, 65
    Originality: Adapted
    Source URL: https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_for
    Date: 5/4/2025

    citation for creating, updating, and deleting from patients
    Scope: Line, 83
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
    Date: 5/20/2025

    citation for html tooltips, used in our edit and delete buttons
    Scope: Line, 65
    Originality: Adapted
    source URL: https://www.geeksforgeeks.org/what-is-a-tooltip-in-html/
    Date: 5/28/2025

# results.j2 
    citation for creating the base template page, most of this page was adapted from this starter code 
    Scope: Module
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948
    Date: 5/2/2025

    citation for url_for from Flask documentation
    Scope: Line, 64
    Originality: Adapted
    Source URL: https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_for
    Date: 5/4/2025

    citation for creating, updating, and deleting from results
    Scope: Line, 82
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
    Date: 5/20/2025

    citation for html tooltips, used in our edit and delete buttons
    Scope: Line, 64, 88
    Originality: Adapted
    source URL: https://www.geeksforgeeks.org/what-is-a-tooltip-in-html/
    Date: 5/28/2025

    citation for restrict the Result input in the edit form to only accept letters
    Scope: Line, 88
    Originality: Adapted
    Source URL: https://www.sololearn.com/en/Discuss/1479898/only-allow-letters-in-a-text-field
    Date: 5/28/2025

    citation for creating a custom message that appears when invalid characters are used for Result in the Results edit form
    Scope: Line, 88
    Source URL: https://stackoverflow.com/questions/19122886/how-can-i-create-a-custom-message-when-an-html5-required-input-pattern-does-not
    Date: 5/28/2025

# scheduledtests.j2
    citation for creating the base template page, most of this page was adapted from the starter code
    Scope: Module
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948
    Date: 5/2/2025

    citation for url_for from Flask documentation
    Scope: Line, 71 
    Originality: Adapted
    Source URL: https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_for
    Date: 5/4/2025

    citation for using OR in the table headers, to handle when certain values are Null. 
    Scope: Line, 65 - 70
    Originality: Adapted
    Source URL:https://stackoverflow.com/questions/19614027/jinja2-template-variable-if-none-object-set-a-default-value
    Date: 5/20/2025 

    citation for creating, updating, and deleting from appointmentstests
    Scope: Line, 90
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
    Date: 5/20/2025

    citation for html tooltips, used in our edit and delete buttons
    Scope: Line, 71
    Originality: Adapted
    source URL: https://www.geeksforgeeks.org/what-is-a-tooltip-in-html/
    Date: 5/28/2025

# statuses.j2
    citation for creating the base template page, most of this page was adapted from the start code 
    Scope: Module
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948
    Date: 5/2/2025

    citation for url_for from Flask documentation
    Scope: Line, 53
    Originality: Adapted
    Source URL: https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_for
    Date: 5/4/2025

    citation for creating, updating, and deleting from statuses
    Scope: Line, 71
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
    Date: 5/20/2025

    citation for html tooltips, used in our edit and delete buttons
    Scope: Line, 53
    Originality: Adapted
    source URL: https://www.geeksforgeeks.org/what-is-a-tooltip-in-html/
    Date: 5/28/2025

# tests.j2
    citation for creating the base template page, most of this page was adapted from this starter code 
    Scope: 
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948
    Date: 5/2/2025

    citation for url_for from Flask documentation
    Scope: Line, 60
    Originality: Adapted
    Source URL: https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_for
    Date: 5/4/2025

    citation for creating, updating, and deleting from tests
    Scope: Line, 85
    Originality: Adapted
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
    Date: 5/20/2025

    citation for html tooltips, used in our edit and delete buttons
    Scope: Line, 60, 63
    Originality: Adapted
    source URL: https://www.geeksforgeeks.org/what-is-a-tooltip-in-html/
    Date: 5/28/2025

# DDL.sql
    Citation for general query formats:
    Multiple weeks in CS340 were spent teaching us how to write SQL queries. All DDL queries were written based on that education. 
    Date: Learning was done over the course of the spring quarter, from 3/25 to 6/25
    Notable Explorations pages include:
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-sql-joins?module_item_id=25352923
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-intro-to-sql?module_item_id=25352908
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-design-patterns-part-2?module_item_id=25352922

    Citation for CASCADE operations:
    Scope: Line, 102, 165 - 167, 237, 239
    Originality: Adapted
    Date: 4/25/2025
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-mysql-cascade


    Citation for START TRANSACTION and COMMIT
    Scope: Line, 64,261
    Originality: Adapted
    Date: 4/25/2025
    Source URL: https://www.geeksforgeeks.org/mysql-transaction/


    Citation for stored procedures, all stored procedures were based on this starter code  
    Scope: Module 
    Originality: Adapted
    Date: 5/17/2025
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-pl-slash-sql-part-2-stored-procedures-for-cud?module_item_id=25352959

# DML.sql
    Citation for general query formats:
    Multiple weeks in CS340 were spent teaching us how to write SQL queries. All DML queries were written based on that education. 
    Date: Learning was done over the course of the spring quarter, from 3/25 to 6/25
    Notable Explorations pages include:
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-sql-joins?module_item_id=25352923
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-intro-to-sql?module_item_id=25352908
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-design-patterns-part-2?module_item_id=25352922


    Citation for CONCAT:
    Scope: Line, 71, 144 - 145, 178 -179
    Originality: Adapted
    Date: 5/3/2025
    Source URL: https://www.mysqltutorial.org/mysql-string-functions/mysql-concat/ 


    Citation for DATE_FORMAT
    Scope: Line, 69, 143, 180
    Originality: Adapted
    Date: 5/10/2025
    Source URL: https://www.mysqltutorial.org/mysql-date-functions/mysql-date_format/ 

# PL.sql
    Citation for Stored Procedures, All stored procedure were adapted from the starter code.  
    Scope: Module 
    Originality: Adapted
    Date: 5/17/2025
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-pl-slash-sql-part-2-stored-procedures-for-cud?module_item_id=25352959
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
