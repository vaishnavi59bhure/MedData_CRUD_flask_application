from __init__ import db
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setup SQLAlchemy base and session
Base = declarative_base()
engine = create_engine('mysql+pymysql://root:9766194467manU@localhost/pythonproject')
Session = sessionmaker(bind=engine)
session = Session()

class PatientModel(db.Model):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    blood_type = Column(String(5), nullable=True)
    medical_condition = Column(String(255), nullable=False)
    date_of_admission = Column(Date, default=date.today, nullable=False)
    doctor = Column(String(255), nullable=True)
    hospital = Column(String(255), nullable=True)
    insurance_provider = Column(String(255), nullable=True)
    billing_amount = Column(Float, nullable=True)
    admission_type = Column(String(50), nullable=True)
    discharge_date = Column(Date)
    medication = Column(String(255), nullable=True)
    test_results = Column(String(255), nullable=True)

    # def __repr__(self):
    #     return f"<Patient {self.name}>"


    @classmethod
    def get_all_patients(cls):
        """Fetches all patient records from the database."""
        return session.query(cls).all()

    @classmethod
    def insert_patient(cls, data):
        """Inserts a new patient record into the database."""
        patient = cls(
            name=data[0],
            age=data[1],
            gender=data[2],
            blood_type=data[3],
            medical_condition=data[4],
            date_of_admission=data[5],
            doctor=data[6],
            hospital=data[7],
            insurance_provider=data[8],
            billing_amount=data[9],
            admission_type=data[10],
            discharge_date=data[11],
            medication=data[12],
            test_results=data[13]
        )
        session.add(patient)
        session.commit()

    @classmethod
    def update_patient(cls, data):
        """Updates an existing patient record in the database."""
        patient_id = data[-1]  # The last element in 'data' is the patient ID
        patient = session.query(cls).filter_by(id=patient_id).first()

        if patient:
            patient.name = data[0]
            patient.age = data[1]
            patient.gender = data[2]
            patient.blood_type = data[3]
            patient.medical_condition = data[4]
            patient.date_of_admission = data[5]
            patient.doctor = data[6]
            patient.hospital = data[7]
            patient.insurance_provider = data[8]
            patient.billing_amount = data[9]
            patient.admission_type = data[10]
            patient.discharge_date = data[11]
            patient.medication = data[12]
            patient.test_results = data[13]

            session.commit()

    @classmethod
    def delete_patient(cls, patient_id):
        """Deletes a patient record from the database."""
        patient = session.query(cls).filter_by(id=patient_id).first()
        if patient:
            session.delete(patient)
            session.commit()


# Create the table if it doesn't exist
Base.metadata.create_all(engine)