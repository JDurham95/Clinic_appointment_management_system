# Clinic Appointment Management System App.py 
# Fidella Wu, Jacob Durham
# CS340 - Introduction to Databases Spring 2025

# Citations: 

# Citation for initilizing/ creating the base app.py
# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948
# Date: 5/2/2025

# Citation for environment variables
# Source URL: https://www.geeksforgeeks.org/using-python-environment-variables-with-python-dotenv/
# Date: 5/2/2025

# Citation for query parameters
# Source URL: https://www.geeksforgeeks.org/get-request-query-parameters-with-flask/
# Date: 5/4/2025

# Citation for Flask CUD routes
# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
# Date: 5/20/2025

# Citation for traceback.print_exc()
# Source URL: https://www.geeksforgeeks.org/traceback-in-python/
# Date: 5/20/2025

# Citation for upper function
# Source URL: https://www.w3schools.com/python/ref_string_upper.asp
# Date: 5/21/2025


import traceback
# ########################################
# ########## SETUP

from flask import Flask, render_template, request, redirect
import database.db_connector as db

PORT = 2000

app = Flask(__name__)

# ########################################
# ########## ROUTE HANDLERS

# READ ROUTES
@app.route("/", methods=["GET"])
def home():
    try:
        return render_template("home.j2")

    except Exception as e:
        print(f"Error rendering page: {e}")
        return "An error occurred while rendering the page.", 500

@app.route("/reset")
def reset():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Create and execute our queries
        reset_query = "CALL sp_load_clinicdb();"
        cursor.execute(reset_query)

        return redirect(request.referrer)

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/clinics", methods=["GET", "POST"])
def clinics():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        get_clinics_query = "SELECT clinicId AS 'Clinic ID', \
                            address AS 'Address', \
                            city AS `City`, \
                            state AS `State`, \
                            postalCode AS `Postal Code`, \
                            phoneNumber AS `Phone Number` \
                            FROM Clinics;"
        clinics = db.query(dbConnection, get_clinics_query).fetchall()

        clinic_id = request.args.get('id')
        if clinic_id:
            action = "Update"
            select_clinic_query = f"SELECT clinicId, address, city, state, postalCode, phoneNumber \
                FROM Clinics \
                WHERE clinicId = {clinic_id};"
            clinic = db.query(dbConnection, select_clinic_query).fetchall()[0]
        else:
            action = "Add"
            clinic = ()

        # Render the clinics.j2 file, and also send the renderer clinics information
        return render_template(
            "clinics.j2", clinics=clinics, clinic=clinic, action=action
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# Create clinic
@app.route("/clinics/create", methods=["POST"])
def create_clinic():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get form data
        address = request.form["address"]
        city = request.form["city"]
        state = request.form["state"].upper()
        postal_code = request.form["postalCode"]
        phone_number = request.form["phoneNumber"]

        # Create and execute our queries
        # Using parameterized queries (Prevents SQL injection attacks)
        insert_clinic_query = "CALL sp_insert_clinic(%s, %s, %s, %s, %s, @new_id);"
        cursor.execute(insert_clinic_query, (address, city, state, postal_code, phone_number))

        # Store ID of last inserted row
        new_id = cursor.fetchone()[0]

        # Consume the result set (if any) before running the next query
        cursor.nextset()  # Move to the next result set (for CALL statements)

        dbConnection.commit()  # commit the transaction

        print(f"CREATE clinic. ID: {new_id}")

        # Redirect the user to the updated webpage
        return redirect("/clinics")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return (
            "An error occurred while executing the database queries.",
            500,
        )

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# Delete clinic
@app.route("/clinics/delete", methods=["POST"])
def delete_clinic():
        try:
            dbConnection = db.connectDB()  # Open our database connection
            cursor = dbConnection.cursor()

            # Get form data
            clinic_id = request.form["id_to_delete"]



            # Create and execute our queries
            # Using parameterized queries (Prevents SQL injection attacks)
            delete_clinic_query = "CALL sp_delete_clinic(%s);"
            cursor.execute(delete_clinic_query, (clinic_id,))

            dbConnection.commit()  # commit the transaction

            print(f"DELETE clinic. ID: {clinic_id}")

            # Redirect the user to the updated webpage
            return redirect("/clinics")

        except Exception as e:
            print(f"Error executing queries: {e}")
            return (
                "An error occurred while executing the database queries.",
                500,
            )

        finally:
            # Close the DB connection, if it exists
            if "dbConnection" in locals() and dbConnection:
                dbConnection.close()

# Update clinic
@app.route("/clinics/update", methods=["POST"])
def update_clinic():
        try:
            dbConnection = db.connectDB()
            cursor = dbConnection.cursor()
        
            #get form data
            clinic_id = request.form["clinicId"]
            print(f"clinicId: {clinic_id}")


            #cleanse data 
            try:
                clinic_address = str(request.form["address"])
            except ValueError:
                clinic_address = None
            
            print(f"address: {clinic_address}")

            try:
                clinic_city = str(request.form["city"])
            except ValueError:
                clinic_city = None

            print(f"city: {clinic_city}")
            
            try:
                clinic_state = str(request.form["state"])
                clinic_state = clinic_state.upper()
            except ValueError:
                clinic_state = None
            
            print(f"state: {clinic_state}")

            try:
                clinic_postal_code = str(request.form["postalCode"])
            except ValueError:
                clinic_postal_code = None

            print(f"postalCode: {clinic_postal_code}")
             
            try:
                clinic_phone_number = str(request.form["phoneNumber"])
            except ValueError:
                clinic_phone_number = None

            print(f"phoneNumber {clinic_phone_number}")
            
            # Create and execute our queries
            # Using parameterized queries (Prevents SQL injection attacks)
            update_clinic_query = "CALL sp_update_clinic(%s, %s, %s, %s, %s, %s);"
            cursor.execute(update_clinic_query, (clinic_id, 
                                                  clinic_address, 
                                                  clinic_city, 
                                                  clinic_state,
                                                  clinic_postal_code,
                                                  clinic_phone_number
                                                  ))

            
            # Consume the result set (if any) before running the next quer
            cursor.nextset()

            dbConnection.commit()
    
            print(f"Updated clinic. clinicid: {clinic_id} Address: {clinic_address}, {clinic_city}, {clinic_state}")

            #redirect back to the updated page
            return redirect("/clinics")
        
        except Exception as e:
            print(f"Error executing queries: {e}")
            traceback.print_exc()
            return(
                "An error occurred while executing the database queries.", 500
            )
        
        finally:
            # Close the db connection, if it exists
            if "dbConnection" in locals() and dbConnection:
                dbConnection.close()



@app.route("/appointments", methods=["GET", "POST"])
def appointments():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        get_appointments_query = "SELECT appointmentId AS `Appointment ID`, \
                                DATE_FORMAT(dateTime, '%%m/%%d/%%Y %%h:%%i %%p') AS `Appointment Date Time`, \
                                CONCAT('Capital Family Clinic at ', Clinics.address, ', ', Clinics.city, ', ', Clinics.state) AS `Clinic`, \
                                Patients.firstName AS `Patient First Name`, \
                                Patients.lastName AS `Patient Last Name`, \
                                Statuses.status AS `Appointment Status` \
                                FROM Appointments \
                                JOIN Patients ON Appointments.patientId = Patients.patientId \
                                JOIN Statuses ON Appointments.statusId = Statuses.statusId \
                                JOIN Clinics ON Appointments.clinicId = Clinics.clinicId \
                                ORDER BY appointmentId;"
        appointments = db.query(dbConnection, get_appointments_query).fetchall()

        get_clinics_query = "SELECT address, clinicId, city, state FROM Clinics ORDER BY clinicId;"
        clinics = db.query(dbConnection, get_clinics_query).fetchall()

        get_patients_query ="SELECT patientId, firstName, lastName, phoneNumber, email, dateOfBirth, gender, clinicId \
             FROM Patients \
             ORDER BY patientId;"
        patients = db.query(dbConnection, get_patients_query).fetchall()

        get_statuses_query = "SELECT statusId, status FROM Statuses ORDER BY statusId;"
        statuses = db.query(dbConnection, get_statuses_query).fetchall()

        appointment_id = request.args.get('id')
        if appointment_id:
            action = "Update"
            select_appointment_query = f"SELECT appointmentId, dateTime, clinicId, patientId, statusId \
                FROM Appointments \
                WHERE appointmentId = {appointment_id};"
            appointment = db.query(dbConnection, select_appointment_query).fetchall()[0]
        else:
            action = "Add"
            appointment = ()

        # Render the appointments.j2 file, and also send the renderer appointments information
        return render_template(
            "appointments.j2", appointments=appointments, clinics=clinics, patients=patients, statuses=statuses, appointment=appointment, action=action
        )
    
    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# Create appointment
@app.route("/appointments/create", methods=["POST"])
def create_appointment():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get form data
        date_time = request.form["dateTime"]
        clinic_id = request.form["clinicId"]
        patient_id = request.form["patientId"]
        status_id = request.form["statusId"]

        # Create and execute our queries
        # Using parameterized queries (Prevents SQL injection attacks)
        insert_appointment_query = "CALL sp_insert_appointment(%s, %s, %s, %s, @new_id);"
        cursor.execute(insert_appointment_query, (date_time, clinic_id, patient_id, status_id))

        # Store ID of last inserted row
        new_id = cursor.fetchone()[0]

        # Consume the result set (if any) before running the next query
        cursor.nextset()  # Move to the next result set (for CALL statements)

        dbConnection.commit()  # commit the transaction

        print(f"CREATE appointment. ID: {new_id}")

        # Redirect the user to the updated webpage
        return redirect("/appointments")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return (
            "An error occurred while executing the database queries.",
            500,
        )

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# Delete appointment
@app.route("/appointments/delete", methods=["POST"])
def delete_appointment():
        try:
            dbConnection = db.connectDB()  # Open our database connection
            cursor = dbConnection.cursor()

            # Get form data
            appointment_id = request.form["id_to_delete"]



            # Create and execute our queries
            # Using parameterized queries (Prevents SQL injection attacks)
            delete_appointment_query = "CALL sp_delete_appointment(%s);"
            cursor.execute(delete_appointment_query, (appointment_id,))

            dbConnection.commit()  # commit the transaction

            print(f"DELETE appointment. ID: {appointment_id}")

            # Redirect the user to the updated webpage
            return redirect("/appointments")

        except Exception as e:
            print(f"Error executing queries: {e}")
            return (
                "An error occurred while executing the database queries.",
                500,
            )

        finally:
            # Close the DB connection, if it exists
            if "dbConnection" in locals() and dbConnection:
                dbConnection.close()

# Update appointment
@app.route("/appointments/update", methods=["POST"])
def update_appointments():
        try:
            dbConnection = db.connectDB()
            cursor = dbConnection.cursor()
        
            #get form data
            appointment_Id = request.form["appointmentId"]
            print(f"appointmentId: {appointment_Id}")


            #cleanse data 
            appointment_date_time = request.form["dateTime"]
            if not appointment_date_time:
                appointment_date_time = None

            print(f"dateTime: {appointment_date_time}")

            try:
                clinic_id = int(request.form["clinicId"])
            except ValueError:
                clinic_id = None

            print(f"clinicId: {clinic_id}")
            
            try:
                patient_id = int(request.form["patientId"])
            except ValueError:
                patient_id = None
            
            print(f"patientId: {patient_id}")

            try:
                status_id = int(request.form["statusId"])
            except ValueError:
                status_id = None

            print(f"statusId: {status_id}")
            
            # Create and execute our queries
            # Using parameterized queries (Prevents SQL injection attacks)
            update_appointment_query = "CALL sp_update_appointment(%s, %s, %s, %s, %s);"
            cursor.execute(update_appointment_query, (appointment_Id, 
                                                  appointment_date_time, 
                                                  clinic_id, 
                                                  patient_id,
                                                  status_id
                                                  ))

            
            # Consume the result set (if any) before running the next quer
            cursor.nextset()

            dbConnection.commit()
    
            print(f"Updated appointment. appointmentId: {appointment_Id} dateTime: {appointment_date_time}")

            #redirect back to the updated page
            return redirect("/appointments")
        
        except Exception as e:
            print(f"Error executing queries: {e}")
            traceback.print_exc()
            return(
                "An error occurred while executing the database queries.", 500
            )
        
        finally:
            # Close the db connection, if it exists
            if "dbConnection" in locals() and dbConnection:
                dbConnection.close()


@app.route("/patients", methods=["GET", "POST"])
def patients():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        get_patients_query = "SELECT patientId AS `Patient ID`, \
                            firstName AS `First Name`, \
                            lastName AS `Last Name`, \
                            Patients.phoneNumber AS `Phone Number`, \
                            email AS `Email`, \
                            DATE_FORMAT(dateOfBirth, '%%m/%%d/%%Y') AS `Date Of Birth`, \
                            gender AS `Gender`, \
                            CONCAT('Capital Family Clinic at ', Clinics.address, ', ', Clinics.city, ', ', Clinics.state) AS `Primary Clinic` \
                            FROM Patients \
                            LEFT JOIN Clinics ON Patients.clinicId = Clinics.clinicId;"
        patients = db.query(dbConnection, get_patients_query).fetchall()

        get_clinics_query = "SELECT clinicId, \
                            CONCAT('Capital Family Clinic at ', Clinics.address, ', ', Clinics.city, ', ', Clinics.state) AS primaryClinic \
                            FROM Clinics;"
        clinics = db.query(dbConnection, get_clinics_query).fetchall()
        
        patient_id = request.args.get('id')
        if patient_id:
            action = "Update"
            select_patient_query = f"SELECT patientId, firstName, lastName, phoneNumber, email, dateOfBirth, gender, clinicId \
                FROM Patients \
                WHERE patientId = {patient_id};"
            patient = db.query(dbConnection, select_patient_query).fetchall()[0]
        else:
            action = "Add"
            patient = ()

        # Render the patients.j2 file, and also send the renderer patients information
        return render_template(
            "patients.j2", patients=patients, clinics=clinics, patient=patient, action=action
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# Create patient
@app.route("/patients/create", methods=["POST"])
def create_patient():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get form data
        first_name = request.form["firstName"]
        last_name = request.form["lastName"]
        phone_number = request.form["phoneNumber"]
        email = request.form["email"]
        date_of_birth = request.form["dateOfBirth"]
        gender = request.form["gender"]

        try:
            clinic_id = int(request.form["clinic"])
        except ValueError:
            clinic_id = None

        # Create and execute our queries
        # Using parameterized queries (Prevents SQL injection attacks)
        insert_patient_query = "CALL sp_insert_patient(%s, %s, %s, %s, %s, %s, %s, @new_id);"
        cursor.execute(insert_patient_query, (first_name, last_name, phone_number, email, date_of_birth, gender, clinic_id))

        # Store ID of last inserted row
        new_id = cursor.fetchone()[0]

        # Consume the result set (if any) before running the next query
        cursor.nextset()  # Move to the next result set (for CALL statements)

        dbConnection.commit()  # commit the transaction

        print(f"CREATE patient. ID: {new_id}")

        # Redirect the user to the updated webpage
        return redirect("/patients")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return (
            "An error occurred while executing the database queries.",
            500,
        )

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# Update patient
@app.route("/patients/update", methods=["POST"])
def update_patient():
        try:
            dbConnection = db.connectDB()
            cursor = dbConnection.cursor()
        
            #get form data
            patient_id = request.form["patientId"]
            print(f"patientId: {patient_id}")


            #cleanse data 
            try:
                patient_first_name = str(request.form["firstName"])
            except ValueError:
                patient_first_name = None
            
            print(f"patient fname: {patient_first_name}")

            try:
                patient_last_name = str(request.form["lastName"])
            except ValueError:
                patient_last_name = None

            print(f"patient lname: {patient_last_name}")
            
            try:
                patient_phone_number = str(request.form["phoneNumber"])
            except ValueError:
                patient_phone_number = None
            
            print(f"patient pn: {patient_phone_number}")

            try:
                patient_email = str(request.form["email"])
            except ValueError:
                patient_email = None

            print(f"patient email: {patient_email}")
             
            patient_date_of_birth = request.form["dateOfBirth"]
            if not patient_date_of_birth:
                patient_date_of_birth = None
            
            print(f"patient DOB: {patient_date_of_birth}")

            try:
                patient_gender = str(request.form["gender"])
            except ValueError:
                patient_gender = None

            print(f"patient gender: {patient_gender}")

            try:
                clinic_id = int(request.form["clinic"])
            except ValueError:
                clinic_id = None
            
            print(f"clinicId: {clinic_id}")
            # Create and execute our queries
            # Using parameterized queries (Prevents SQL injection attacks)
            update_patient_query = "CALL sp_update_patient(%s, %s, %s, %s, %s, %s, %s,%s);"
            cursor.execute(update_patient_query, (patient_id, 
                                                  patient_first_name, 
                                                  patient_last_name, 
                                                  patient_phone_number,
                                                  patient_email,
                                                  patient_date_of_birth,
                                                  patient_gender,
                                                  clinic_id))

            
            # Consume the result set (if any) before running the next quer
            cursor.nextset()

            dbConnection.commit()
    
            print(f"Updated patient. testId: {patient_id} name: {patient_first_name} {patient_last_name}")

            #redirect back to the updated page
            return redirect("/patients")
        
        except Exception as e:
            print(f"Error executing queries: {e}")
            traceback.print_exc()
            return(
                "An error occurred while executing the database queries.", 500
            )
        
        finally:
            # Close the db connection, if it exists
            if "dbConnection" in locals() and dbConnection:
                dbConnection.close()

@app.route("/statuses", methods=["GET", "POST"])
def statuses():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        get_status_query = "SELECT statusId AS `Status ID`, \
                        status AS `Status` \
                        FROM Statuses \
                        ORDER BY statusId;"
        statuses = db.query(dbConnection, get_status_query).fetchall()

        status_id = request.args.get('id')
        if status_id:
            action = "Update"
            select_status_query = f"SELECT statusId, status \
                FROM Statuses \
                WHERE statusId = {status_id};"
            status = db.query(dbConnection, select_status_query).fetchall()[0]
        else:
            action = "Add"
            status = ()

        # Render the statuses.j2 file, and also send the renderer statuses information
        return render_template(
            "statuses.j2", statuses=statuses, status=status, action=action
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# Update status
@app.route("/statuses/update", methods=["POST"])
def update_status():
        try:
            dbConnection = db.connectDB()
            cursor = dbConnection.cursor()
        
            #get form data
            status_id = request.form["statusId"]
            print(f"statusId: {status_id}")


            #cleanse data 
            try:
                status = str(request.form["status"])
            except ValueError:
                status = None
            

            # Create and execute our queries
            # Using parameterized queries (Prevents SQL injection attacks)
            update_status_query = "CALL sp_update_status(%s, %s);"
            cursor.execute(update_status_query, (status_id, status))

            
            # Consume the result set (if any) before running the next quer
            cursor.nextset()

            dbConnection.commit()
    
            print(f"Updated status statusId: {status_id} status: {status}")

            #redirect back to the updated page
            return redirect("/statuses")
        
        except Exception as e:
            print(f"Error executing queries: {e}")
            traceback.print_exc()
            return(
                "An error occurred while executing the database queries.", 500
            )
        
        finally:
            # Close the db connection, if it exists
            if "dbConnection" in locals() and dbConnection:
                dbConnection.close()

@app.route("/tests", methods=["GET", "POST"])
def tests():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        get_tests_query = "SELECT testId AS `Test ID`, name AS `Name` FROM Tests ORDER BY testId;"
        tests = db.query(dbConnection, get_tests_query).fetchall()

        test_Id = request.args.get('id')
        if test_Id:
            action = "Update"
            select_test_query =f"SELECT testId, name FROM Tests WHERE testId = {test_Id};"
            test= db.query(dbConnection,select_test_query).fetchall()[0]
        else:
            action= "Add"
            test=()

        # Render the tests.j2 file, and also send the renderer test information
        return render_template(
            "tests.j2", tests=tests, test=test, action =action
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# Create test
@app.route("/tests/create", methods=["POST"])
def create_test():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get form data
        name = request.form["name"]

        # Create and execute our queries
        # Using parameterized queries (Prevents SQL injection attacks)
        insert_test_query = "CALL sp_insert_test(%s, @new_id);"
        cursor.execute(insert_test_query, (name,))

        # Store ID of last inserted row
        new_id = cursor.fetchone()[0]

        # Consume the result set (if any) before running the next query
        cursor.nextset()  # Move to the next result set (for CALL statements)

        dbConnection.commit()  # commit the transaction

        print(f"CREATE test. ID: {new_id}")

        # Redirect the user to the updated webpage
        return redirect("/tests")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return (
            "An error occurred while executing the database queries.",
            500,
        )

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# Update test
@app.route("/tests/update", methods=["POST"])
def update_test():
        try:
            dbConnection = db.connectDB()
            cursor = dbConnection.cursor()
        
            #get form data
            test_id = request.form["testId"]
            print(f"testId: {test_id}")


            #cleanse data 
            try:
                test_name = str(request.form["name"])
            except ValueError:
                test_name = None
            

            # Create and execute our queries
            # Using parameterized queries (Prevents SQL injection attacks)
            update_test_query = "CALL sp_update_test(%s, %s);"
            cursor.execute(update_test_query, (test_id, test_name))

            
            # Consume the result set (if any) before running the next quer
            cursor.nextset()

            dbConnection.commit()
    
            print(f"Updated test. testId: {test_id} name: {test_name}")

            #redirect back to the updated page
            return redirect("/tests")
        
        except Exception as e:
            print(f"Error executing queries: {e}")
            traceback.print_exc()
            return(
                "An error occurred while executing the database queries.", 500
            )
        
        finally:
            # Close the db connection, if it exists
            if "dbConnection" in locals() and dbConnection:
                dbConnection.close()

# Delete test
@app.route("/tests/delete", methods=["POST"])
def delete_test():
        try:
            dbConnection = db.connectDB()  # Open our database connection
            cursor = dbConnection.cursor()

            # Get form data
            test_id = request.form["id_to_delete"]



            # Create and execute our queries
            # Using parameterized queries (Prevents SQL injection attacks)
            delete_test_query = "CALL sp_delete_test(%s);"
            cursor.execute(delete_test_query, (test_id,))

            dbConnection.commit()  # commit the transaction

            print(f"DELETE test. ID: {test_id}")

            # Redirect the user to the updated webpage
            return redirect("/tests")

        except Exception as e:
            print(f"Error executing queries: {e}")
            return (
                "An error occurred while executing the database queries.",
                500,
            )

        finally:
            # Close the DB connection, if it exists
            if "dbConnection" in locals() and dbConnection:
                dbConnection.close()


@app.route("/results", methods=["GET", "POST"])
def results():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        get_results_query = "SELECT Results.testResultId AS `Test Result ID`, Results.result AS `Result` FROM Results ORDER BY testResultId;"
        results = db.query(dbConnection, get_results_query).fetchall()

        result_id = request.args.get('id')
        if result_id:
            action = "Update"
            select_result_query = f"SELECT testResultId, result \
                                FROM Results \
                                WHERE testResultId = {result_id};"
            result = db.query(dbConnection, select_result_query).fetchall()[0]
        else:
            action = "Add"
            result = ()

        # Render the results.j2 file, and also send the renderer result information
        return render_template(
            "results.j2", results=results, result=result, action=action
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# Update result
@app.route("/results/update", methods=["POST"])
def update_result():
        try:
            dbConnection = db.connectDB()
            cursor = dbConnection.cursor()
        
            #get form data
            test_result_id = request.form["testResultId"]
            print(f"test result Id: {test_result_id}")


            #cleanse data 
            try:
                result = str(request.form["result"])
            except ValueError:
                result = None
            

            # Create and execute our queries
            # Using parameterized queries (Prevents SQL injection attacks)
            update_result_query = "CALL sp_update_result(%s, %s);"
            cursor.execute(update_result_query, (test_result_id, result))

            
            # Consume the result set (if any) before running the next quer
            cursor.nextset()

            dbConnection.commit()
    
            print(f"Updated result testResultId: {test_result_id} result: {result}")

            #redirect back to the updated page
            return redirect("/results")
        
        except Exception as e:
            print(f"Error executing queries: {e}")
            traceback.print_exc()
            return(
                "An error occurred while executing the database queries.", 500
            )
        
        finally:
            # Close the db connection, if it exists
            if "dbConnection" in locals() and dbConnection:
                dbConnection.close()

@app.route("/appointmentstests", methods=["GET", "POST"])
def appointmentstests():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        get_appointmentstests_info_query = "SELECT AppointmentsTests.appointmentTestId AS `Appointment Test ID`, \
                                            Patients.firstName AS `Patient First Name`, \
                                            Patients.lastName AS `Patient Last Name`, \
                                            CONCAT('Capital Family Clinic at ', Clinics.address, ', ', Clinics.city, ', ', Clinics.state) AS `Clinic`,\
                                            DATE_FORMAT(Appointments.dateTime, '%%m/%%d/%%Y %%h:%%i %%p') AS `Appointment Date Time`, \
                                            Tests.name AS `Test Name`, \
                                            Results.result AS `Test Result` \
                                            FROM AppointmentsTests \
                                            LEFT JOIN Appointments on AppointmentsTests.appointmentId = Appointments.appointmentId \
                                            LEFT JOIN Patients on Appointments.patientId = Patients.patientId \
                                            JOIN Tests on AppointmentsTests.testId = Tests.testId \
                                            JOIN Results on AppointmentsTests.testResultId = Results.testResultId \
                                            LEFT JOIN Clinics ON Appointments.clinicId = Clinics.clinicId \
                                            ORDER BY appointmentTestId;"
        appointmentstests_info = db.query(dbConnection, get_appointmentstests_info_query).fetchall()

        get_appointmentstests_query ="SELECT appointmentTestId, appointmentId, testId, testResultId FROM AppointmentsTests ORDER BY appointmentTestId;"
        appointmentstests = db.query(dbConnection,get_appointmentstests_query).fetchall()

        get_tests_query ="SELECT testId, name FROM Tests ORDER BY testId;"
        tests = db.query(dbConnection,get_tests_query).fetchall()

        get_appointments_query = "SELECT appointmentId, DATE_FORMAT(dateTime, '%%m/%%d/%%Y %%h:%%i %%p') AS dateTime, \
                                Appointments.clinicId, Patients.firstName, Patients.lastName, Statuses.status, \
                                CONCAT(Patients.firstName,' ', Patients.lastName,' - ', DATE_FORMAT(Appointments.dateTime, '%%m/%%d/%%Y %%h:%%i %%p'), ' at ', Clinics.address,' ', Clinics.city, ', ', Clinics.state) AS `dropDownInfo` \
                                FROM Appointments \
                                JOIN Patients ON Appointments.patientId = Patients.patientId \
                                JOIN Statuses ON Appointments.statusId = Statuses.statusId \
                                JOIN Clinics ON Appointments.clinicId = Clinics.clinicId \
                                ORDER BY appointmentId;"
        appointments = db.query(dbConnection, get_appointments_query).fetchall()

        get_results_query = "SELECT testResultId, result FROM Results ORDER BY testResultId;"
        results = db.query(dbConnection, get_results_query).fetchall()
    

        appointmenttest_id = request.args.get('id')
        if appointmenttest_id:
            action = "Update"
            select_appointmenttest_query = f"SELECT appointmentTestId, appointmentId, testId, testResultId \
                FROM AppointmentsTests \
                WHERE appointmentTestId = {appointmenttest_id};"
            appointmenttest = db.query(dbConnection, select_appointmenttest_query).fetchall()[0]
        else:
            action = "Add"
            appointmenttest = ()

        # Render the apppointmentstests.j2 file, and also send the renderer appointmentstests information
        return render_template(
            "appointmentstests.j2", appointmentstests=appointmentstests, appointmentstests_info=appointmentstests_info, tests=tests, appointments=appointments, results=results, appointmenttest=appointmenttest, action=action
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# Create appointmentstests
@app.route("/appointmentstests/create", methods=["POST"])
def create_appointmentstests():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get form data
        appointment_id = request.form["appointmentId"]
        test_id = request.form["testId"]
        test_result_id = request.form["testResultId"]

        # Create and execute our queries
        # Using parameterized queries (Prevents SQL injection attacks)
        insert_appointmenttest_query = "CALL sp_insert_appointmenttest(%s, %s, %s, @new_id);"
        cursor.execute(insert_appointmenttest_query, (appointment_id, test_id, test_result_id))

        # Store ID of last inserted row
        new_id = cursor.fetchone()[0]

        # Consume the result set (if any) before running the next query
        cursor.nextset()  # Move to the next result set (for CALL statements)

        dbConnection.commit()  # commit the transaction

        print(f"CREATE appointmenttest. ID: {new_id}")

        # Redirect the user to the updated webpage
        return redirect("/appointmentstests")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return (
            "An error occurred while executing the database queries.",
            500,
        )

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# Update appointmentstests
@app.route("/appointmentstests/update", methods=["POST"])
def update_appointmentstests():
        try:
            dbConnection = db.connectDB()
            cursor = dbConnection.cursor()
        
            #get form data
            appointmenttest_id = request.form["appointmentTestId"]
            print(f"appointmenttestId: {appointmenttest_id}")


            #cleanse data 
            try:
                appointment_id = int(request.form["appointmentId"])
            except ValueError:
                appointment_id = None

            print(f"appointmentId: {appointment_id}")
            
            try:
                test_id = int(request.form["testId"])
            except ValueError:
                test_id = None
            
            print(f"testId: {test_id}")

            try:
                test_result_id = int(request.form["testResultId"])
            except ValueError:
                test_result_id = None

            print(f"testResultId: {test_result_id}")
            
            # Create and execute our queries
            # Using parameterized queries (Prevents SQL injection attacks)
            update_appointmenttest_query = "CALL sp_update_appointmenttest(%s, %s, %s, %s);"
            cursor.execute(update_appointmenttest_query, (appointmenttest_id, 
                                                  appointment_id, 
                                                  test_id, 
                                                  test_result_id
                                                  ))

            
            # Consume the result set (if any) before running the next quer
            cursor.nextset()

            dbConnection.commit()
    
            print(f"Updated appointmenttest. appointmentTestId: {appointmenttest_id} appointmentId: {appointment_id}")

            #redirect back to the updated page
            return redirect("/appointmentstests")
        
        except Exception as e:
            print(f"Error executing queries: {e}")
            traceback.print_exc()
            return(
                "An error occurred while executing the database queries.", 500
            )
        
        finally:
            # Close the db connection, if it exists
            if "dbConnection" in locals() and dbConnection:
                dbConnection.close()

            
# ########################################
# ########## LISTENER

if __name__ == "__main__":
    app.run(
        port=PORT, debug=True
    )  # debug is an optional parameter. Behaves like nodemon in Node.