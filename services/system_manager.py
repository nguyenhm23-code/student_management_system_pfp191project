from models.student import Student
from utils.file_io import save_data_to_file, load_data_from_file

class SystemManager:
    def __init__(self, data_file="students_data.txt"):
        self.students = []
        self.data_file = data_file
        self.load_students()

    def load_students(self):
        data = load_data_from_file(self.data_file)
        self.students = [Student.from_dict(item) for item in data]

    def save_students(self):
        save_data_to_file(self.data_file, self.students)

    def add_student(self, student: Student):
        self.students.append(student)
        print("Thêm sinh viên thành công.")

    def find_student_by_id(self, student_id: str):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_students(self, keyword: str):
        keyword = keyword.lower()
        return [s for s in self.students if keyword in s.name.lower() or keyword in s.student_id.lower()]

    def sort_students(self, criteria: str):
        """Sắp xếp danh sách sinh viên."""
        if criteria == "gpa":
            self.students.sort(key=lambda s: s.gpa, reverse=True)
        elif criteria == "name":
            self.students.sort(key=lambda s: s.name)
        elif criteria == "birth_year":
            self.students.sort(key=lambda s: s.birth_year)

    def calculate_overall_gpa(self) -> float:
        if not self.students:
            return 0.0
        total_gpa = sum(s.gpa for s in self.students)
        return total_gpa / len(self.students)