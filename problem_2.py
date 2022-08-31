# • Create an empty dictionary called dog
# • Add name, color, breed, legs, age to the dog dictionary
# • Create a student dictionary and add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
# • Get the length of the student dictionary
# • Get the value of skills and check the data type, it should be a list
# • Modify the skills values by adding one or two skills
# • Get the dictionary keys as a list
# • Get the dictionary values as a list


dog = {}
dog["name"] = "brix"
dog["color"] = "white"
dog["breed"] = "fill the breed that u like"
dog["legs"] = "I dont know what to keep here"
dog["age"] = "2 maybe?"
print(dog)

student = {}
student["first_name"] = "lahari"
student["last_name"] = "lahari"
student["gender"] = "female"
student["age"] = "22"
student["martial_status"] = "single...I think so. Dont get offended, if wrong. Xd. sorry!"
student["skills"] = ['cpp', 'c', 'python']
student["country"] = "India"
student["city"] = "lahari"
student["address"] = "lahari"

skills = student.get('skills')
print(f'length of student dictonary: {len(student)}')
print(f'skills in student dictonary: {skills}, type of skills: {type(skills)}')
student['skills'] += ['javascript', 'sql']
print(f"new skills added: {student['skills']}")
print(f"dictonary keys as list: {list(student.keys())}")
print(f"dictonary values as list: {list(student.values())}")
