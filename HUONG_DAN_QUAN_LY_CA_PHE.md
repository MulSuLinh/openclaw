# Hướng dẫn quản lý kinh doanh cà phê

## Chức năng
- Theo dõi danh mục Robusta nhân xanh, Arabica nhân xanh, cà phê rang hạt, rang xay và hòa tan.
- Tự thử lấy giá tham khảo qua API Internet khi mở chương trình; có thể chọn mục **9** để cập nhật lại bất cứ lúc nào.
- Có thể gõ một số yêu cầu tiếng Việt ở dòng menu, chẳng hạn “cho tôi biết giá cà phê hôm nay”, “xem tồn kho”, “báo cáo doanh thu” hoặc “lấy giá mới từ Internet”.
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
1. Khi mở chương trình, ứng dụng thử lấy giá tham khảo mới từ Internet. Chọn **9** để cập nhật lại theo yêu cầu.
2. Chọn **2** nếu muốn tự nhập giá từ nguồn khác hoặc cập nhật loại cà phê chưa được API cung cấp.
3. Chọn **4** khi mua/nhập cà phê vào kho.
4. Chọn **5** khi bán hàng. Chương trình ngăn bán vượt lượng tồn kho đã ghi.
5. Chọn **6** để kiểm tra tồn kho.
6. Chọn **1** hoặc **3** để xem giá theo ngày và lịch sử biến động.
7. Chọn **8** để xem báo cáo tháng.

## Nhập yêu cầu bằng tiếng Việt
- Bộ nhận diện hiện tại dùng từ khóa và quy tắc trích xuất, chưa phải mô hình AI tổng quát.
- Khi câu nhập/bán có đủ loại giao dịch, tên cà phê, số lượng kg và đơn giá VNĐ/kg, chương trình tự lưu và in kết quả. Nếu thiếu trường hoặc không đủ tồn kho, chương trình sẽ báo và hỏi thêm thay vì đoán.
- Nếu chương trình không nhận ra câu, gõ `help` để xem ví dụ hoặc chọn số chức năng trên menu.

## Lưu ý
- API giá tham khảo: [Buon Ma Thuot Coffee Portal](https://buonmathuotcoffee.com/vietnam-coffee-data/api). Tài liệu API hiện ghi không cần API key; nếu nhà cung cấp thay đổi chính sách, hãy kiểm tra tài liệu trước khi sử dụng.
- Dữ liệu API bao gồm chỉ số thu mua nội địa tham khảo, Robusta/Arabica kỳ hạn và tỷ giá. Chương trình chỉ lưu chỉ số thu mua nội địa vào lịch sử cho Robusta nhân xanh; không tự gán giá đó cho Arabica, cà phê rang hoặc hòa tan.
- Mỗi bản ghi lưu ngày/thời điểm do nguồn cung cấp, thời điểm ứng dụng lấy dữ liệu, tên nguồn và liên kết nguồn. Nếu API lỗi hoặc không hợp lệ, chương trình báo lỗi và giữ nguyên dữ liệu đã lưu.
- Giá tham khảo không phải báo giá đảm bảo tại đại lý. Kiểm tra giá thực tế tại nơi mua/bán trước khi giao dịch.
- Dữ liệu lưu cạnh chương trình trong file `ca_phe_data.json`. Hãy sao lưu file này định kỳ.
- Lãi gộp chỉ là ước tính theo giá vốn bình quân từ các lần nhập, chưa trừ vận chuyển, bao bì, nhân công, hao hụt và các chi phí khác.
- Nhập hàng trước khi ghi nhận bán để tồn kho chính xác.
- Đơn vị số lượng là kg và đơn giá là VNĐ/kg.
