from flask import Blueprint, render_template, request, url_for, flash
from models.patient import PatientModel
from utils.validators import validate_patient_data

patient_bp = Blueprint('patient_bp', __name__)

@patient_bp.route('/')
def index():
    # Fetches all patients and displays them on the 'index2.html' template
    patients = PatientModel.get_all_patients()
    return render_template('index.html', patients=patients)

@patient_bp.route('/insert', methods=['POST'])
def insert():
    # Inserts a new patient into the database after validating data
    if request.method == 'POST':
        form_data = request.form.to_dict()
        if not validate_patient_data(form_data):
            flash("Invalid data. Please check the input.")
            return render_template("index.html")

        # Extracts patient data and inserts it into the database
        data = (
            form_data['name'],
            form_data['age'],
            form_data['gender'],
            form_data['blood_type'],
            form_data['medical_condition'],
            form_data['date_of_admission'],
            form_data['doctor'],
            form_data['hospital'],
            form_data['insurance_provider'],
            form_data['billing_amount'],
            form_data['admission_type'],
            form_data['discharge_date'],
            form_data['medication'],
            form_data['test_results']
        )
        PatientModel.insert_patient(data)
        flash("Data Inserted Successfully")
        return render_template("index.html")

@patient_bp.route('/delete/<int:id_data>', methods=['POST'])
def delete(id_data):
    # Deletes a patient record by ID
    PatientModel.delete_patient(id_data)
    flash("Record Has Been Deleted Successfully")
    return render_template("index.html")

@patient_bp.route('/update', methods=['POST'])
def update():
    # Updates a patient record with new data after validation
    form_data = request.form.to_dict()
    if not validate_patient_data(form_data, updating=True):
        print("Validation failed. Form data:", form_data)
        flash("Invalid data. Please check the input.")
        return render_template("index.html")

    # Extracts patient data and updates the record in the database
    data = (
        form_data['name'],
        form_data['age'],
        form_data['gender'],
        form_data['blood_type'],
        form_data['medical_condition'],
        form_data['date_of_admission'],
        form_data['doctor'],
        form_data['hospital'],
        form_data['insurance_provider'],
        form_data['billing_amount'],
        form_data['admission_type'],
        form_data['discharge_date'],
        form_data['medication'],
        form_data['test_results'],
        int(form_data['id'])
    )
    PatientModel.update_patient(data)
    flash("Data Updated Successfully")
    return render_template("index.html")