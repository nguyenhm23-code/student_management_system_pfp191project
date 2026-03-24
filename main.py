from models.student import Student
from services.system_manager import SystemManager

def main():
    manager = SystemManager()

    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ SINH VIÊN ===")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách sinh viên")
        print("3. Nhập điểm cho sinh viên")
        print("4. Tìm kiếm sinh viên (theo Tên/ID)")
        print("5. Sắp xếp sinh viên")
        print("6. Xóa sinh viên")
        print("7. Xem bảng điểm của một sinh viên")
        print("8. Lưu dữ liệu")
        print("9. Thoát chương trình")
        
        choice = input("Vui lòng chọn chức năng (1-9): ").strip()

        if choice == '1':
            try:
                s_id = input("Nhập ID sinh viên: ").strip()
                if not s_id:
                    print("Lỗi: ID sinh viên không được để trống!")
                    continue
                
                if manager.find_student_by_id(s_id):
                    print(f"Lỗi: Sinh viên có ID '{s_id}' đã tồn tại trong hệ thống!")
                    continue

                name = input("Nhập tên sinh viên: ").strip()
                if not name:
                    print("Lỗi: Tên sinh viên không được để trống!")
                    continue

                year_str = input("Nhập năm sinh: ").strip()
                if not year_str:
                    print("Lỗi: Năm sinh không được để trống!")
                    continue
                year = int(year_str)

                major = input("Nhập chuyên ngành: ").strip()
                if not major:
                    print("Lỗi: Chuyên ngành không được để trống!")
                    continue
                
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
            s_id = input("Nhập ID sinh viên cần nhập điểm: ").strip()
            if not s_id:
                print("Lỗi: ID sinh viên không được để trống!")
                continue

            student = manager.find_student_by_id(s_id)
            if student:
                subject = input("Nhập tên môn học: ").strip()
                if not subject:
                    print("Lỗi: Tên môn học không được để trống!")
                    continue

                try:
                    score = float(input(f"Nhập điểm cho môn {subject}: ").strip())
                    if score < 0 or score > 10:
                        print("Lỗi: Điểm số phải nằm trong khoảng từ 0 đến 10!")
                        continue
                        
                    student.add_score(subject, score)
                    print("Cập nhật điểm thành công!")
                except ValueError:
                    print("Lỗi: Điểm số phải là một con số hợp lệ!")
            else:
                print("Không tìm thấy sinh viên với ID này.")

        elif choice == '4':
            keyword = input("Nhập tên hoặc ID cần tìm: ").strip()
            if not keyword:
                print("Lỗi: Từ khóa tìm kiếm không được để trống!")
                continue

            results = manager.search_students(keyword)
            if results:
                print(f"Tìm thấy {len(results)} kết quả:")
                for s in results:
                    print(s)
            else:
                print("Không tìm thấy kết quả nào.")

        elif choice == '5':
            print("Tiêu chí sắp xếp: 1 (GPA), 2 (Tên), 3 (Năm sinh)")
            sort_choice = input("Chọn tiêu chí: ").strip()
            if sort_choice == '1':
                manager.sort_students("gpa")
                print("Đã sắp xếp danh sách theo GPA!")
            elif sort_choice == '2':
                manager.sort_students("name")
                print("Đã sắp xếp danh sách theo Tên!")
            elif sort_choice == '3':
                manager.sort_students("birth_year")
                print("Đã sắp xếp danh sách theo Năm sinh!")
            else:
                print("Lỗi: Tiêu chí sắp xếp không hợp lệ!")

        elif choice == '6':
            s_id = input("Nhập ID sinh viên cần xóa: ").strip()
            if not s_id:
                print("Lỗi: ID sinh viên không được để trống!")
                continue
            
            if manager.delete_student(s_id):
                print(f"Thành công: Đã xóa sinh viên ID '{s_id}' và cập nhật lại file dữ liệu!")
            else:
                print(f"Lỗi: Không tìm thấy sinh viên nào mang ID '{s_id}'.")

        elif choice == '7':
            s_id = input("Nhập ID sinh viên cần xem bảng điểm: ").strip()
            if not s_id:
                print("Lỗi: ID sinh viên không được để trống!")
                continue

            student = manager.find_student_by_id(s_id)
            if student:
                print(f"\n--- BẢNG ĐIỂM CỦA SINH VIÊN: {student.name.upper()} [{student.student_id}] ---")
                if not student.scores:
                    print("=> Sinh viên này chưa có dữ liệu điểm môn nào.")
                else:
                    for subject, score in student.scores.items():
                        print(f"- Môn {subject}: {score}")
                    print(f"=> Điểm GPA hệ 10: {student.gpa:.2f}")
            else:
                print(f"Lỗi: Không tìm thấy sinh viên nào mang ID '{s_id}'.")

        elif choice == '8':
            manager.save_students()
            print("Đã lưu toàn bộ dữ liệu hiện tại vào file thành công!")

        elif choice == '9':
            print("Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()