def validate_patient_data(data, updating=False):
    required_fields = [
        'name', 'age', 'gender', 'blood_type', 'medical_condition',
        'date_of_admission', 'doctor', 'hospital', 'insurance_provider',
        'billing_amount', 'admission_type', 'discharge_date', 'medication',
        'test_results'
    ]

    if updating:
        required_fields.append('id')

    missing_fields = []
    for field in required_fields:
        if field not in data or not data[field].strip():
            missing_fields.append(field)

    if missing_fields:
        print(f"Validation failed: Missing or empty fields - {missing_fields}")
        return False

    return True

