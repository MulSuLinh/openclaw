# Mộc Coffee — Website bán cà phê demo

Website cửa hàng cà phê viết bằng **HTML, CSS và JavaScript thuần**. Không cần cài Node.js, Python hay thư viện bổ sung để chạy bản demo.

## Chạy trong Visual Studio Code (Windows)

### 1. Tải dự án về máy

Nếu đã cài Git, mở Terminal (PowerShell hoặc CMD) và chạy:

```bash
git clone https://github.com/MulSuLinh/openclaw.git
```

Sau đó trong VS Code chọn **File → Open Folder...** và mở thư mục:

```text
openclaw/website-ca-phe
```

Nếu chưa dùng Git, mở trang repository trên GitHub, chọn **Code → Download ZIP**, giải nén rồi mở thư mục `website-ca-phe` trong VS Code.

### 2. Mở website

**Cách khuyên dùng — Live Server**

1. Trong VS Code, mở mục **Extensions** (biểu tượng các ô vuông ở thanh bên).
2. Cài extension **Live Server** của Ritwick Dey nếu chưa có.
3. Trong Explorer, nhấp chuột phải vào `index.html`.
4. Chọn **Open with Live Server**. Trình duyệt sẽ mở website; khi lưu thay đổi, trang sẽ tự tải lại.

**Cách không cần extension:** mở thư mục `website-ca-phe` trong File Explorer rồi nhấp đúp `index.html` để mở bằng trình duyệt. Cách này phù hợp để xem giao diện cơ bản.

## Cấu trúc dự án

```text
website-ca-phe/
├── index.html
├── README.md
└── .vscode/
    └── extensions.json
```

CSS và JavaScript hiện nằm ngay trong `index.html`, nên không cần chạy lệnh `npm install` hay `npm run dev`.

## Tính năng

- Giao diện tiếng Việt, thích ứng với màn hình máy tính và điện thoại.
- Danh sách sản phẩm cà phê và dụng cụ pha chế.
- Lọc sản phẩm, giỏ hàng, thay đổi số lượng và tính tổng tiền.
- Form nhập thông tin đặt hàng mẫu.

## Lưu ý

Đây là bản demo giao diện: đơn hàng chưa được gửi hoặc lưu trên máy chủ và chưa có thanh toán trực tuyến. Hình ảnh sản phẩm tải từ Internet nên cần có kết nối mạng. Giá và hình ảnh chỉ mang tính minh họa; hãy cập nhật thông tin chính xác trước khi kinh doanh thật.

## Đăng lên GitHub Pages

Có thể cấu hình GitHub Pages để xuất bản website. Vì trang nằm trong thư mục `website-ca-phe`, hãy chọn cách triển khai đúng thư mục này làm thư mục xuất bản; bật Pages ở thư mục gốc không tự động dùng trang này.
