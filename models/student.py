class Student:
    def __init__(self, student_id: str, name: str, birth_year: int, major: str):
        self.student_id = student_id
        self.name = name
        self.birth_year = birth_year
        self.major = major
        self.scores = {}

    @property
    def gpa(self) -> float:
        if not self.scores:
            return 0.0
        return sum(self.scores.values()) / len(self.scores)

    def add_score(self, subject: str, score: float):
        self.scores[subject] = score

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "birth_year": self.birth_year,
            "major": self.major,
            "scores": self.scores
        }

    @classmethod
    def from_dict(cls, data: dict):
        student = cls(data["student_id"], data["name"], data["birth_year"], data["major"])
        student.scores = data.get("scores", {})
        return student

    def __str__(self):
        return f"[{self.student_id}] {self.name} | Năm sinh: {self.birth_year} | Ngành: {self.major} | GPA: {self.gpa:.2f}"