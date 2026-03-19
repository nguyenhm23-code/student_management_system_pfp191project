from models.student import Student
from services.system_manager import SystemManager

def main():
    manager = SystemManager()

    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ SINH VIÊN ===")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách sinh viên")
        print("3. Nhập điểm cho sinh viên")
        print("4. Tìm kiếm sinh viên")
        print("5. Sắp xếp sinh viên")
        print("6. Lưu dữ liệu và Thoát")
        
        choice = input("Vui lòng chọn chức năng (1-6): ")

        if choice == '1':
            try:
                s_id = input("Nhập ID sinh viên: ")
                name = input("Nhập tên sinh viên: ")
                year = int(input("Nhập năm sinh: "))
                major = input("Nhập chuyên ngành: ")
                
                new_student = Student(s_id, name, year, major)
                manager.add_student(new_student)
            except ValueError:
                print("Lỗi: Năm sinh phải là một số nguyên hợp lệ!")

        elif choice == '2':
            if not manager.students:
                print("Danh sách trống.")
            else:
                for student in manager.students:
                    print(student)
                print(f"\n=> Điểm GPA trung bình của toàn hệ thống: {manager.calculate_overall_gpa():.2f}")

        elif choice == '3':
            s_id = input("Nhập ID sinh viên cần nhập điểm: ")
            student = manager.find_student_by_id(s_id)
            if student:
                subject = input("Nhập tên môn học: ")
                try:
                    score = float(input(f"Nhập điểm cho môn {subject}: "))
                    student.add_score(subject, score)
                    print("Cập nhật điểm thành công!")
                except ValueError:
                    print("Lỗi: Điểm số phải là một con số hợp lệ!")
            else:
                print("Không tìm thấy sinh viên với ID này.")

        elif choice == '4':
            keyword = input("Nhập tên hoặc ID cần tìm: ")
            results = manager.search_students(keyword)
            if results:
                print(f"Tìm thấy {len(results)} kết quả:")
                for s in results:
                    print(s)
            else:
                print("Không tìm thấy kết quả nào.")

        elif choice == '5':
            print("Tiêu chí sắp xếp: 1 (GPA), 2 (Tên), 3 (Năm sinh)")
            sort_choice = input("Chọn tiêu chí: ")
            if sort_choice == '1':
                manager.sort_students("gpa")
            elif sort_choice == '2':
                manager.sort_students("name")
            elif sort_choice == '3':
                manager.sort_students("birth_year")
            print("Đã sắp xếp danh sách!")

        elif choice == '6':
            manager.save_students()
            print("Đã thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()