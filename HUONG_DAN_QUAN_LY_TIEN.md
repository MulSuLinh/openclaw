# Trình quản lý thu chi cá nhân

Chương trình Python chạy trên máy tính, giao diện menu tiếng Việt và lưu giao dịch vào file `data_thu_chi.json` cạnh chương trình. Không cần cài thư viện ngoài.

## Cách chạy trên Windows

1. Cài Python 3 nếu máy chưa có.
2. Tải file `quan_ly_tien.py` từ kho GitHub này về máy.
3. Mở thư mục chứa file, nhấp thanh địa chỉ của File Explorer, gõ `cmd` rồi nhấn Enter.
4. Chạy:
   ```powershell
   python quan_ly_tien.py
   ```
   Nếu lệnh trên không hoạt động, thử `py quan_ly_tien.py`.

## Chức năng đang hoạt động

1. **Thêm thu nhập**: nhập số tiền, danh mục, ghi chú và ngày.
2. **Thêm chi tiêu**: lưu khoản chi với danh mục và ngày.
3. **Xem lịch sử**: xem giao dịch mới nhất trước, kèm mã giao dịch.
4. **Tổng kết tháng**: tính tổng thu, tổng chi, chênh lệch và chi tiêu theo danh mục.
5. **Xoá giao dịch**: nhập mã giao dịch và xác nhận trước khi xoá.
6. **Lưu dữ liệu**: tự tạo/cập nhật `data_thu_chi.json`; đóng chương trình rồi mở lại vẫn còn dữ liệu.

## Ví dụ

- Thêm thu nhập: 2.000.000 VNĐ, danh mục “Lương/tiền nhận”.
- Thêm chi tiêu: 50.000 VNĐ, danh mục “Ăn uống”.
- Tổng kết sẽ hiển thị tổng thu 2.000.000 đ, tổng chi 50.000 đ, chênh lệch 1.950.000 đ (nếu cả hai giao dịch nằm trong cùng tháng).

## Lưu ý

- Dữ liệu được lưu cục bộ trên máy chạy chương trình, không tự đồng bộ lên mạng hoặc điện thoại.
- Đây là công cụ ghi chép thu chi cơ bản, không kết nối ngân hàng, không tự chuyển tiền và không phải ứng dụng tư vấn đầu tư.
- Nên sao lưu file `data_thu_chi.json` nếu dữ liệu quan trọng.
