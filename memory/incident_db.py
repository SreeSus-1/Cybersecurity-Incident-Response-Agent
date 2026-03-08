from tinydb import TinyDB
from datetime import datetime

db = TinyDB("incident_sessions.json")

def save_incident(filename, parsed_output, threat_output, containment_output):
    db.insert({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "filename": filename,
        "parsed_output": parsed_output,
        "threat_output": threat_output,
        "containment_output": containment_output
    })

def get_all_incidents():
    return db.all()