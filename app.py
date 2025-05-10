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


@app.route("/clinics", methods=["GET", "POST"])
def clinics():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        get_clinics_query = "SELECT clinicId, address, city, state, postalCode, phoneNumber FROM Clinics;"
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

@app.route("/appointments", methods=["GET", "POST"])
def appointments():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        get_appointments_query = "SELECT appointmentId, DATE_FORMAT(dateTime, '%%m/%%d/%%Y %%h:%%i %%p') AS dateTime, CONCAT('Capital Family Clinic in ', Clinics.city,' , ', Clinics.state  ) AS primaryClinic, Patients.firstName, Patients.lastName, Statuses.status \
                            FROM Appointments \
                            JOIN Patients ON Appointments.patientId = Patients.patientId \
                            JOIN Statuses ON Appointments.statusId = Statuses.statusId \
                            JOIN Clinics ON Appointments.clinicId = Clinics.clinicId \
                            ORDER BY appointmentId;"
        appointments = db.query(dbConnection, get_appointments_query).fetchall()

        get_clinics_query = "SELECT clinicId, city, state FROM Clinics ORDER BY clinicId;"
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

@app.route("/patients", methods=["GET", "POST"])
def patients():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        get_patients_query = "SELECT patientId, firstName, lastName, Patients.phoneNumber, email, dateOfBirth, gender, CONCAT('Capital Family Clinic in ', Clinics.city, ', ', Clinics.state) AS primaryClinic \
                FROM Patients \
                JOIN Clinics ON Patients.clinicId = Clinics.clinicId;"
        patients = db.query(dbConnection, get_patients_query).fetchall()

        get_clinics_query = "SELECT clinicId, city, state FROM Clinics ORDER BY clinicId;"
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

@app.route("/statuses", methods=["GET", "POST"])
def statuses():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        get_status_query = "SELECT statusId, status FROM Statuses ORDER BY statusId;"
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

@app.route("/tests", methods=["GET", "POST"])
def tests():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        get_tests_query = "SELECT testId, name FROM Tests ORDER BY testId;"
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

@app.route("/results", methods=["GET", "POST"])
def results():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        query1 = "SELECT Results.testResultId, Results.result FROM Results ORDER BY testResultId;"
        results = db.query(dbConnection, query1).fetchall()

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

@app.route("/appointmentstests", methods=["GET", "POST"])
def appointmentstests():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        get_appointmentstests_info_query = "SELECT AppointmentsTests.appointmentTestId, Patients.firstName, Patients.lastName, Appointments.clinicId, Appointments.dateTime, Tests.name, Results.result \
                FROM AppointmentsTests \
                JOIN Appointments on AppointmentsTests.appointmentId = Appointments.appointmentId \
                JOIN Patients on Appointments.patientId = Patients.patientId \
                JOIN Tests on AppointmentsTests.testId = Tests.testID \
                JOIN Results on AppointmentsTests.testResultId = Results.testResultId \
                ORDER BY lastName, dateTime;"
        appointmentstests_info = db.query(dbConnection, get_appointmentstests_info_query).fetchall()

        get_appointmentstests_query ="SELECT appointmentTestId, appointmentId, testId, testResultId FROM AppointmentsTests ORDER BY appointmentTestId;"
        appointmentstests = db.query(dbConnection,get_appointmentstests_query).fetchall()

        get_tests_query ="SELECT testId, name FROM Tests ORDER BY testId;"
        tests = db.query(dbConnection,get_tests_query).fetchall()

        get_appointments_query = "SELECT appointmentId, DATE_FORMAT(dateTime, '%%m/%%d/%%Y %%h:%%i %%p') AS dateTime, \
                            Appointments.clinicId, Patients.firstName, Patients.lastName, Statuses.status, \
                            CONCAT(Patients.firstName,' ', Patients.lastName,' at ', DATE_FORMAT(Appointments.dateTime, '%%m/%%d/%%Y %%h:%%i %%p'), ' in ', Clinics.city, ',', Clinics.state) AS `dropDownInfo` \
                            FROM appointments \
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
# ########################################
# ########## LISTENER

if __name__ == "__main__":
    app.run(
        port=PORT, debug=True
    )  # debug is an optional parameter. Behaves like nodemon in Node.