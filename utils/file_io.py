import json
import os

def save_data_to_file(filename: str, students_list: list):
    """Lưu danh sách sinh viên vào file txt."""
    try:
        data = [student.to_dict() for student in students_list]
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("Đã lưu dữ liệu thành công!")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

def load_data_from_file(filename: str) -> list:
    """Đọc dữ liệu sinh viên từ file txt."""
    if not os.path.exists(filename):
        return []
        
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data # Trả về list các dictionaries
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return []