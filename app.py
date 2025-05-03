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
def clinics():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        query1 = "SELECT clinicId, address, city, state, postalCode, phoneNumber FROM Clinics;"
        clinics = db.query(dbConnection, query1).fetchall()

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

@app.route("/patients", methods=["GET"])
def patients():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        query1 = "SELECT patientId, firstName, lastName, email, dateOfBirth, gender, CONCAT('Capital Family Clinic in ', Clinics.city, ', ', Clinics.state) AS clinicName \
                FROM Patients \
                JOIN Clinics ON Patients.clinicId = Clinics.clinicId;"
        patients = db.query(dbConnection, query1).fetchall()

        # Render the patients.j2 file, and also send the renderer patients information
        return render_template(
            "patients.j2", patients=patients
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/statuses", methods=["GET"])
def statuses():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        query1 = "SELECT statusId, status FROM Statuses ORDER BY statusId;"
        statuses = db.query(dbConnection, query1).fetchall()

        # Render the statuses.j2 file, and also send the renderer statuses information
        return render_template(
            "statuses.j2", statuses=statuses
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