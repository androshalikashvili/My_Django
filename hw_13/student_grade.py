my_dict = {
  "students": [
    {"id": 20, "name": "giorgi", "age": 25},
    {"id": 25, "name": "giorgi", "age": 23},
    {"id": 100, "name": "nika", "age": 22},
    {"id": 56, "name": "nika", "age": 25},
    {"id": 1232, "name": "dato", "age": 22},
    {"id": 846723, "name": "archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
  ]
}


st_id_list = []

for student in my_dict.get('students'):
    st_id_list.append(student.get('id'))

print('studentebis ID: ', ", ".join(map(str, st_id_list)), '\n')
st_id = int(input('airchiet studentis ID: '))
print()
print('student information:')

found_student = None
for student in my_dict.get('students'):
    if st_id == student.get('id'):
        found_student = student
        break


if found_student:
    st_name_lower = found_student.get('name')
    st_age = found_student.get('age')
    st_name = st_name_lower.capitalize()
    
    print(f'ID: {st_id}, name: {st_name}, age: {st_age}')


    for subject in my_dict.get('subjects'):
        sagani = subject.get('name')
        st_grade = subject.get('grades').get(str(st_id), "shefasebis gareshe")
        print(f'subject: {sagani}, grade: {st_grade}')

else:
    print(f'Studenti ID {st_id} ver moidzebna')
