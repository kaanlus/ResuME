
# Make a dictionary of majors as keys, with the values being fields within that major

# The next dictionary would use fields as keys, subfields as values

# Keep getting smaller and more specific


majors = {
    "Computer Science": {
        "Software Engineering":,
        "Cybersecurity":,
        "Data Science":,
    },
    "Mechanical Engineering": {
        "Design":,
        "Manufacturing":,
        "Mechanics":,
        "Thermodynamics":,
        "Materials":
    },
    "Chemical Engineering": {
        "Environmental":,
        "Design":,
        "Safety":,
        "Plant":,
        "Waste":
    },
    "Aerospace Engineering": {
        "Aircraft":,
        "Aerodynamics":,
        "Thermodynamics":,
        "Materials":,
        "Mechanics": {
            "Celestial":,
            "Flight":,
        }

    },
    "Electrical Engineering": {
        "Electronics":,
        "Computer":,
        "Robotics":,

    }


}



# Make some example functions that take in familiar keywords for different 

def match(major):
    key = major.lower()
    if key not in majors:
        majors[key] = ""

        
