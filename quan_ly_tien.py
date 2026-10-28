#!/usr/bin/env python3
"""Trình quản lý thu chi cá nhân chạy bằng Python, lưu dữ liệu trong data_thu_chi.json."""
import json
from datetime import date, datetime
from pathlib import Path

DATA_FILE = Path(__file__).with_name("data_thu_chi.json")
CATEGORIES = {
    "1": "Ăn uống", "2": "Đi lại", "3": "Học tập", "4": "Mua sắm",
    "5": "Nhà ở/hoá đơn", "6": "Giải trí", "7": "Lương/tiền nhận",
    "8": "Khác",
}


def load_records():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Không đọc được dữ liệu. Hãy kiểm tra file data_thu_chi.json.")
        return []


def save_records(records):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)


def money(amount):
    return f"{amount:,.0f} đ".replace(",", ".")


def choose_category():
    print("\nDanh mục:")
    for key, value in CATEGORIES.items():
        print(f"  {key}. {value}")
    while True:
        choice = input("Chọn danh mục (1-8): ").strip()
        if choice in CATEGORIES:
            return CATEGORIES[choice]
        print("Lựa chọn chưa hợp lệ, hãy nhập số từ 1 đến 8.")


def add_record(records, kind):
    label = "thu nhập" if kind == "thu" else "chi tiêu"
    print(f"\n--- Thêm {label} ---")
    while True:
        raw = input("Số tiền (VNĐ, lớn hơn 0): ").strip().replace(".", "").replace(",", "")
        try:
            amount = float(raw)
            if amount > 0:
                break
        except ValueError:
            pass
        print("Số tiền không hợp lệ. Ví dụ: 50000")
    category = choose_category()
    note = input("Ghi chú (có thể bỏ trống): ").strip()
    day = input(f"Ngày YYYY-MM-DD (Enter = {date.today().isoformat()}): ").strip()
    if not day:
        day = date.today().isoformat()
    try:
        datetime.strptime(day, "%Y-%m-%d")
    except ValueError:
        print("Ngày không hợp lệ; dùng ngày hôm nay.")
        day = date.today().isoformat()
    next_id = max((r.get("id", 0) for r in records), default=0) + 1
    records.append({
        "id": next_id, "type": kind, "amount": round(amount, 2),
        "category": category, "note": note, "date": day
    })
    save_records(records)
    print(f"Đã lưu {label} #{next_id}: {money(amount)}.")


def filter_month(records, month):
    return [r for r in records if r.get("date", "").startswith(month)]


def totals(records):
    income = sum(r["amount"] for r in records if r["type"] == "thu")
    expense = sum(r["amount"] for r in records if r["type"] == "chi")
    return income, expense, income - expense


def show_summary(records):
    month = input(f"Xem tháng YYYY-MM (Enter = {date.today().strftime('%Y-%m')}): ").strip()
    if not month:
        month = date.today().strftime("%Y-%m")
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Định dạng tháng không hợp lệ.")
        return
    selected = filter_month(records, month)
    income, expense, balance = totals(selected)
    print(f"\n=== TỔNG KẾT THÁNG {month} ===")
    print(f"Số giao dịch: {len(selected)}")
    print(f"Tổng thu:    {money(income)}")
    print(f"Tổng chi:    {money(expense)}")
    print(f"Chênh lệch:  {money(balance)}")
    by_category = {}
    for item in selected:
        if item["type"] == "chi":
            by_category[item["category"]] = by_category.get(item["category"], 0) + item["amount"]
    if by_category:
        print("\nChi tiêu theo danh mục:")
        for category, amount in sorted(by_category.items(), key=lambda x: x[1], reverse=True):
            print(f"  - {category}: {money(amount)}")


def list_records(records):
    if not records:
        print("\nChưa có giao dịch nào.")
        return
    print("\n--- LỊCH SỬ GIAO DỊCH ---")
    for r in sorted(records, key=lambda x: (x.get("date", ""), x.get("id", 0)), reverse=True):
        sign = "+" if r["type"] == "thu" else "-"
        note = f" | {r['note']}" if r.get("note") else ""
        print(f"#{r['id']} | {r['date']} | {r['category']} | {sign}{money(r['amount'])}{note}")


def delete_record(records):
    list_records(records)
    if not records:
        return
    try:
        record_id = int(input("\nNhập mã giao dịch cần xoá: "))
    except ValueError:
        print("Mã giao dịch không hợp lệ.")
        return
    target = next((r for r in records if r.get("id") == record_id), None)
    if not target:
        print("Không tìm thấy giao dịch.")
        return
    confirm = input(f"Xoá giao dịch #{record_id} ({money(target['amount'])})? (y/N): ").strip().lower()
    if confirm == "y":
        records.remove(target)
        save_records(records)
        print("Đã xoá giao dịch.")
    else:
        print("Đã huỷ.")


def set_budget():
    print("\nTính năng ngân sách chưa lưu mức ngân sách tự động.")
    print("Bạn có thể dùng tổng kết tháng để theo dõi chi tiêu; phiên bản sau có thể bổ sung hạn mức.")


def main():
    records = load_records()
    while True:
        print("\n" + "=" * 38)
        print("      QUẢN LÝ THU CHI CÁ NHÂN")
        print("=" * 38)
        print("1. Thêm thu nhập")
        print("2. Thêm chi tiêu")
        print("3. Xem lịch sử giao dịch")
        print("4. Tổng kết theo tháng")
        print("5. Xoá giao dịch")
        print("0. Thoát")
        choice = input("Chọn chức năng: ").strip()
        if choice == "1":
            add_record(records, "thu")
        elif choice == "2":
            add_record(records, "chi")
        elif choice == "3":
            list_records(records)
        elif choice == "4":
            show_summary(records)
        elif choice == "5":
            delete_record(records)
        elif choice == "0":
            print("Dữ liệu đã được lưu. Tạm biệt!")
            break
        else:
            print("Không có lựa chọn này. Hãy nhập 0-5.")
        records = load_records()


if __name__ == "__main__":
    main()
