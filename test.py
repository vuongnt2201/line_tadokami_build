import random
import json

NUM_TRIALS = 1000  # Giảm xuống 1000 để không tạo file quá lớn khi test
a_variants = ['A1', 'A2', 'A3', 'A4', 'A5', 'A30']
a_variant_weights = [14, 14, 14, 14, 14, 30]

all_lists = []

for _ in range(NUM_TRIALS):
    # 1. Chọn 5 biến thể A khác nhau theo tỉ lệ
    selected_a = random.choices(
        population=a_variants,
        weights=a_variant_weights,
        k=100
    )
    selected_a_unique = list(dict.fromkeys(selected_a))[:5]

    # Nếu không có A30 thì bỏ qua
    if 'A30' not in selected_a_unique:
        continue

    # 2. Tạo list gồm 5 A, 3 B, 2 C
    sections = selected_a_unique + ['B'] * 3 + ['C'] * 2

    # 3. Shuffle cho tới khi 2 C không liền nhau
    for _ in range(100):
        random.shuffle(sections)
        c_indexes = [i for i, s in enumerate(sections) if s == 'C']
        if abs(c_indexes[0] - c_indexes[1]) > 1:
            break
    else:
        continue

    # 4. Lưu list vào kết quả
    all_lists.append(sections)

# 5. Xuất ra file JSON
with open("section_lists.json", "w", encoding="utf-8") as f:
    json.dump(all_lists, f, ensure_ascii=False, indent=2)

print(f"Đã ghi {len(all_lists)} list vào file 'section_lists.json'")
 