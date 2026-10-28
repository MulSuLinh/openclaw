# Hướng dẫn quản lý kinh doanh cà phê

## Chức năng
- Theo dõi giá của Robusta nhân xanh, Arabica nhân xanh, cà phê rang hạt, rang xay và hòa tan.
- Lưu giá theo ngày, xem lịch sử tăng/giảm.
- Ghi nhận mua/nhập hàng và bán hàng theo kg, đơn giá, ngày và ghi chú.
- Theo dõi tồn kho, lịch sử giao dịch và báo cáo tháng về tiền nhập, doanh thu, lãi gộp ước tính.

## Chạy chương trình
Cần Python 3.10 trở lên. Mở terminal tại thư mục chứa file rồi chạy:

```bash
python quan_ly_ca_phe.py
```

Trên một số máy Windows, dùng `py quan_ly_ca_phe.py`.

## Sử dụng hằng ngày
1. Chọn **2** để nhập giá thị trường từ nguồn bạn tin cậy.
2. Chọn **4** khi mua/nhập cà phê vào kho.
3. Chọn **5** khi bán hàng. Chương trình ngăn bán vượt lượng tồn kho đã ghi.
4. Chọn **6** để kiểm tra tồn kho.
5. Chọn **1** hoặc **3** để xem giá theo ngày và lịch sử biến động.
6. Chọn **8** để xem báo cáo tháng.

## Lưu ý
- Giá **không tự động lấy từ Internet** ở phiên bản này. Chương trình hiển thị giá đã nhập gần nhất tính đến ngày chọn; cần cập nhật hằng ngày để theo dõi biến động thật.
- Dữ liệu lưu cạnh chương trình trong file `ca_phe_data.json`. Hãy sao lưu file này định kỳ.
- Lãi gộp chỉ là ước tính theo giá vốn bình quân từ các lần nhập, chưa trừ vận chuyển, bao bì, nhân công, hao hụt và các chi phí khác.
- Nhập hàng trước khi ghi nhận bán để tồn kho chính xác.
- Đơn vị số lượng là kg và đơn giá là VNĐ/kg.
