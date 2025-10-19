def read_students():
    with open("students.txt", "r") as file:
        students = []
        for line in file:
            matric_no, name, dept, cgpa = line.strip().split(",")
            students.append({
                "matric_no": matric_no,
                "name": name,
                "department": dept,
                "cgpa": float(cgpa)
            })
        return students


def display_all(students):
    print("All Students:")
    for s in students:
        print(f"{s['matric_no']} - {s['name']} - {s['department']} - {s['cgpa']}")


def search_by_matric(students, matric_no):
    for s in students:
        if s["matric_no"] == matric_no:
            return s
    return None


def find_high_cgpa(students, threshold=3.5):
    return [s for s in students if s["cgpa"] > threshold]


if __name__ == "__main__":
    students = read_students()

    # Display all
    display_all(students)

    # Search by matric number
    matric = input("\nEnter Matric Number to search: ")
    result = search_by_matric(students, matric)
    if result:
        print(f"Found: {result['name']} - {result['department']} - {result['cgpa']}")
    else:
        print("Specified student not found")

    # Show students with CGPA > 3.5
    print("\nStudents with CGPA > 3.5:")
    for s in find_high_cgpa(students):
        print(f"{s['name']} ({s['cgpa']})")
