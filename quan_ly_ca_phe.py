#!/usr/bin/env python3
"""Quản lý kinh doanh cà phê: giá theo ngày, nhập hàng, bán hàng và tồn kho.

Dữ liệu được lưu cục bộ trong ca_phe_data.json. Giá thị trường không được tự
động lấy từ Internet; người dùng cập nhật theo nguồn giá đáng tin cậy.
"""
import json
from datetime import date, datetime
from pathlib import Path

DATA_FILE = Path(__file__).with_name("ca_phe_data.json")
DEFAULT_PRODUCTS = [
    {"id": 1, "name": "Cà phê Robusta nhân xanh", "unit": "kg"},
    {"id": 2, "name": "Cà phê Arabica nhân xanh", "unit": "kg"},
    {"id": 3, "name": "Cà phê rang hạt", "unit": "kg"},
    {"id": 4, "name": "Cà phê rang xay", "unit": "kg"},
    {"id": 5, "name": "Cà phê hòa tan", "unit": "kg"},
]


def initial_data():
    return {"products": DEFAULT_PRODUCTS.copy(), "price_history": [], "transactions": []}


def load_data():
    if not DATA_FILE.exists():
        data = initial_data()
        save_data(data)
        return data
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, dict):
            raise ValueError("Cấu trúc dữ liệu không hợp lệ")
        data.setdefault("products", DEFAULT_PRODUCTS.copy())
        data.setdefault("price_history", [])
        data.setdefault("transactions", [])
        return data
    except (json.JSONDecodeError, OSError, ValueError) as error:
        print(f"Không đọc được dữ liệu: {error}")
        print("Hãy sao lưu và kiểm tra file ca_phe_data.json trước khi chạy lại.")
        raise SystemExit(1)


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def money(value):
    return f"{value:,.0f} đ".replace(",", ".")


def number(prompt, allow_zero=False):
    while True:
        raw = input(prompt).strip().replace(".", "").replace(",", "")
        try:
            value = float(raw)
            if value > 0 or (allow_zero and value >= 0):
                return value
        except ValueError:
            pass
        print("Vui lòng nhập số hợp lệ.")


def ask_date(prompt="Ngày YYYY-MM-DD (Enter = hôm nay): "):
    raw = input(prompt).strip()
    if not raw:
        return date.today().isoformat()
    try:
        return datetime.strptime(raw, "%Y-%m-%d").date().isoformat()
    except ValueError:
        print("Ngày không hợp lệ; dùng ngày hôm nay.")
        return date.today().isoformat()


def get_product(data, prompt="Chọn mã sản phẩm: "):
    print("\n--- DANH MỤC CÀ PHÊ ---")
    for product in data["products"]:
        print(f'{product["id"]}. {product["name"]} ({product["unit"]})')
    while True:
        try:
            product_id = int(input(prompt).strip())
        except ValueError:
            product_id = -1
        product = next((p for p in data["products"] if p["id"] == product_id), None)
        if product:
            return product
        print("Mã sản phẩm không hợp lệ.")


def product_name(data, product_id):
    product = next((p for p in data["products"] if p["id"] == product_id), None)
    return product["name"] if product else f'Sản phẩm #{product_id}'


def price_for(data, product_id, day=None):
    day = day or date.today().isoformat()
    entries = [p for p in data["price_history"]
               if p["product_id"] == product_id and p["date"] <= day]
    if not entries:
        return None
    return max(entries, key=lambda p: (p["date"], p["id"]))["price"]


def show_prices(data):
    day = ask_date("Xem giá ngày YYYY-MM-DD (Enter = hôm nay): ")
    print(f"\n=== GIÁ CÀ PHÊ NGÀY {day} ===")
    found = False
    for product in data["products"]:
        current = price_for(data, product["id"], day)
        if current is None:
            print(f'{product["id"]}. {product["name"]}: chưa có dữ liệu giá')
            continue
        found = True
        previous_entries = [p for p in data["price_history"]
                            if p["product_id"] == product["id"] and p["date"] < day]
        previous = max(previous_entries, key=lambda p: (p["date"], p["id"])) if previous_entries else None
        change = ""
        if previous:
            difference = current - previous["price"]
            if difference > 0:
                change = f" | tăng {money(difference)} so với {previous['date']}"
            elif difference < 0:
                change = f" | giảm {money(-difference)} so với {previous['date']}"
            else:
                change = f" | không đổi so với {previous['date']}"
        print(f'{product["id"]}. {product["name"]}: {money(current)}/{product["unit"]}{change}')
    if not found:
        print("Chưa nhập giá nào. Hãy chọn chức năng cập nhật giá.")
    print("\nLưu ý: giá hiển thị là dữ liệu bạn đã nhập gần nhất tính đến ngày đã chọn.")


def update_prices(data):
    day = ask_date()
    print("\nNhập giá tham khảo/giá thị trường theo nguồn bạn đang theo dõi.")
    print("Nhập 0 để bỏ qua một sản phẩm.")
    for product in data["products"]:
        raw = input(f'Giá {product["name"]} (VNĐ/kg, 0 = bỏ qua): ').strip()
        try:
            price = float(raw.replace(".", "").replace(",", ""))
            if price == 0:
                continue
            if price < 0:
                raise ValueError
        except ValueError:
            print("Giá không hợp lệ, bỏ qua sản phẩm này.")
            continue
        next_id = max((p.get("id", 0) for p in data["price_history"]), default=0) + 1
        data["price_history"].append({
            "id": next_id, "product_id": product["id"], "date": day,
            "price": price, "source": "Người dùng nhập"
        })
    save_data(data)
    print("Đã lưu cập nhật giá. Xem mục giá theo ngày để so sánh thay đổi.")


def show_price_history(data):
    product = get_product(data)
    entries = sorted(
        [p for p in data["price_history"] if p["product_id"] == product["id"]],
        key=lambda p: (p["date"], p["id"])
    )
    print(f'\n=== LỊCH SỬ GIÁ: {product["name"]} ===')
    if not entries:
        print("Chưa có lịch sử giá.")
        return
    previous = None
    for entry in entries:
        delta = ""
        if previous is not None:
            difference = entry["price"] - previous["price"]
            delta = f" | {'+' if difference > 0 else ''}{money(difference)}"
        print(f'{entry["date"]}: {money(entry["price"])}/{product["unit"]}{delta}')
        previous = entry


def stock_quantity(data, product_id):
    bought = sum(t["quantity"] for t in data["transactions"]
                 if t["product_id"] == product_id and t["type"] == "nhap")
    sold = sum(t["quantity"] for t in data["transactions"]
               if t["product_id"] == product_id and t["type"] == "ban")
    return bought - sold


def average_cost(data, product_id):
    purchases = [t for t in data["transactions"]
                 if t["product_id"] == product_id and t["type"] == "nhap"]
    quantity = sum(t["quantity"] for t in purchases)
    if quantity <= 0:
        return 0
    return sum(t["quantity"] * t["unit_price"] for t in purchases) / quantity


def record_transaction(data, kind):
    product = get_product(data)
    available = stock_quantity(data, product["id"])
    if kind == "ban":
        print(f"Tồn kho hiện tại: {available:g} {product['unit']}")
        if available <= 0:
            print("Không thể bán vì sản phẩm chưa có hàng tồn kho.")
            return
    quantity = number(f'Số lượng ({product["unit"]}): ')
    if kind == "ban" and quantity > available:
        print(f"Không đủ hàng. Tồn kho hiện tại chỉ có {available:g} {product['unit']}.")
        return
    suggested = price_for(data, product["id"])
    hint = f" (giá đã lưu gần nhất: {money(suggested)})" if suggested is not None else ""
    unit_price = number(f"Đơn giá VNĐ/{product['unit']}{hint}: ")
    day = ask_date()
    note = input("Ghi chú/đối tác (không bắt buộc): ").strip()
    next_id = max((t.get("id", 0) for t in data["transactions"]), default=0) + 1
    transaction = {
        "id": next_id, "type": kind, "product_id": product["id"],
        "quantity": quantity, "unit_price": unit_price,
        "total": round(quantity * unit_price, 2), "date": day, "note": note
    }
    if kind == "ban":
        transaction["estimated_cost"] = round(quantity * average_cost(data, product["id"]), 2)
    data["transactions"].append(transaction)
    save_data(data)
    action = "nhập hàng" if kind == "nhap" else "bán hàng"
    print(f"Đã lưu giao dịch #{next_id}: {action} {quantity:g} {product['unit']}, "
          f"tổng {money(transaction['total'])}.")


def show_inventory(data):
    print("\n=== TỒN KHO CÀ PHÊ ===")
    for product in data["products"]:
        quantity = stock_quantity(data, product["id"])
        cost = average_cost(data, product["id"])
        print(f'{product["name"]}: {quantity:g} {product["unit"]} | '
              f'giá vốn bình quân tham khảo {money(cost)}/{product["unit"]} | '
              f'giá trị vốn ước tính {money(max(quantity, 0) * cost)}')
    print("Giá vốn bình quân là ước tính từ toàn bộ giao dịch nhập đã lưu, không phải FIFO.")


def show_transactions(data):
    transactions = sorted(data["transactions"], key=lambda t: (t["date"], t["id"]), reverse=True)
    print("\n=== LỊCH SỬ NHẬP / BÁN ===")
    if not transactions:
        print("Chưa có giao dịch.")
        return
    for t in transactions:
        action = "NHẬP" if t["type"] == "nhap" else "BÁN"
        note = f' | {t["note"]}' if t.get("note") else ""
        print(f'#{t["id"]} | {t["date"]} | {action} | {product_name(data, t["product_id"])} '
              f'| {t["quantity"]:g} kg x {money(t["unit_price"])} = {money(t["total"])}{note}')


def show_report(data):
    month = input(f"Xem báo cáo tháng YYYY-MM (Enter = {date.today():%Y-%m}): ").strip()
    if not month:
        month = date.today().strftime("%Y-%m")
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Định dạng tháng không hợp lệ.")
        return
    items = [t for t in data["transactions"] if t["date"].startswith(month)]
    purchases = sum(t["total"] for t in items if t["type"] == "nhap")
    sales = sum(t["total"] for t in items if t["type"] == "ban")
    estimated_cost = sum(t.get("estimated_cost", 0) for t in items if t["type"] == "ban")
    print(f"\n=== BÁO CÁO THÁNG {month} ===")
    print(f"Số giao dịch: {len(items)}")
    print(f"Tổng tiền nhập hàng: {money(purchases)}")
    print(f"Tổng doanh thu bán hàng: {money(sales)}")
    print(f"Lãi gộp ước tính: {money(sales - estimated_cost)}")
    print("Lãi gộp chỉ là ước tính theo giá vốn bình quân; chưa trừ vận chuyển, nhân công và chi phí khác.")


def main():
    data = load_data()
    actions = {
        "1": ("Xem giá cà phê theo ngày", lambda: show_prices(data)),
        "2": ("Cập nhật giá từng ngày", lambda: update_prices(data)),
        "3": ("Xem lịch sử biến động giá", lambda: show_price_history(data)),
        "4": ("Nhập hàng/mua cà phê", lambda: record_transaction(data, "nhap")),
        "5": ("Bán cà phê", lambda: record_transaction(data, "ban")),
        "6": ("Xem tồn kho", lambda: show_inventory(data)),
        "7": ("Lịch sử nhập và bán", lambda: show_transactions(data)),
        "8": ("Báo cáo doanh thu và lãi gộp", lambda: show_report(data)),
    }
    while True:
        print("\n" + "=" * 42)
        print(" QUẢN LÝ KINH DOANH CÀ PHÊ")
        print("=" * 42)
        for key, (label, _) in actions.items():
            print(f"{key}. {label}")
        print("0. Thoát")
        choice = input("Chọn chức năng: ").strip()
        if choice == "0":
            print("Đã thoát chương trình.")
            break
        if choice in actions:
            actions[choice][1]()
        else:
            print("Lựa chọn không hợp lệ. Hãy nhập từ 0 đến 8.")


if __name__ == "__main__":
    main()
