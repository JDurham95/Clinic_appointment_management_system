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


@app.route("/clinics", methods=["GET"])
def bsg_people():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        query1 = "SELECT clinicId, address, city, state, postalCode, phoneNumber FROM Clinics;"
        clinics = db.query(dbConnection, query1).fetchall()

        query2 = "SELECT appointmentId, date, time, Appointments.clinicId, firstName, lastName, status FROM Appointments JOIN Patients ON Appointments.patientId = Patients.patientId JOIN Statuses ON Appointments.statusId = Statuses.statusId;"
        appointments = db.query(dbConnection, query2).fetchall()

        # Render the clinics.j2 file, and also send the renderer clinics information
        return render_template(
            "clinics.j2", clinics=clinics
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()
            
@app.route("/appointments", methods=["GET"])
def get_appointments():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        query2 = "SELECT appointmentId, date, time, Appointments.clinicId, firstName, lastName, status FROM Appointments JOIN Patients ON Appointments.patientId = Patients.patientId JOIN Statuses ON Appointments.statusId = Statuses.statusId;"
        appointments = db.query(dbConnection, query2).fetchall()

        # Render the appointments.j2 file, and also send the renderer appointments information
        return render_template(
            "appointments.j2", appointments=appointments
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