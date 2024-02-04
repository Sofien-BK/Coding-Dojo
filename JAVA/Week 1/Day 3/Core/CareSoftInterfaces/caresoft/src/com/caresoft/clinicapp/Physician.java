package com.caresoft.clinicapp;

import java.util.ArrayList;
import java.util.Date;

public class Physician extends User implements HIPAACompliantUser {
	private ArrayList<String> patientNotes;
	
	
	
	 
	
	public Physician(Integer idcopy) {
		this.id = idcopy;
	}

	public boolean assignPin(int pin) {
		String pinString = Integer.toString(pin); 
		if (pinString.length() == 4 ) {
			return true;
		}else {
			return false;
		}
	}
	
	public boolean accessAuthorized(Integer confirmedAuthID) {
		if(getId()==confirmedAuthID) {
			return true;
		}else {
			return false;
		}
	}
	
	// TO DO: Constructor that takes an IDcopy
    // TO DO: Implement HIPAACompliantUser!
	
	public void newPatientNotes(String notes, String patientName, Date date) {
        String report = String.format(
            "Datetime Submitted: %s \n", date);
        report += String.format("Reported By ID: %s\n", this.id);
        report += String.format("Patient Name: %s\n", patientName);
        report += String.format("Notes: %s \n", notes);
        this.patientNotes.add(report);
    }

	public ArrayList<String> getPatientNotes() {
		return patientNotes;
	}

	public void setPatientNotes(ArrayList<String> patientNotes) {
		this.patientNotes = patientNotes;
	}
	
    // TO DO: Setters & Getters
	
}
