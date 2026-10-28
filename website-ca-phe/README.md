# Mộc Coffee — Website bán cà phê demo

Website giới thiệu và bán hàng mẫu cho thương hiệu **Mộc Coffee**, viết bằng HTML, CSS và JavaScript thuần. Dự án phù hợp để học và trình diễn website tĩnh; không cần cài thư viện hoặc framework để mở bản demo.

## Liên kết dự án

- **Mã nguồn trong repository này:** [website-ca-phe/index.html](./index.html)
- **Repository nguồn:** [MulSuLinh/openclaw](https://github.com/MulSuLinh/openclaw)
- **Bản sao trong repository học tập:** [MulSuLinh/python-journey/projects/moc-coffee](https://github.com/MulSuLinh/python-journey/tree/main/projects/moc-coffee)
- **README bản sao:** [Tài liệu Mộc Coffee trên python-journey](https://github.com/MulSuLinh/python-journey/blob/main/projects/moc-coffee/README.md)
- **Website GitHub Pages dự kiến của bản sao:** https://mulsulinh.github.io/python-journey/projects/moc-coffee/

> Đường dẫn GitHub Pages chỉ hoạt động sau khi bật Pages và GitHub triển khai thành công. Trạng thái triển khai chưa được xác nhận.

## Tính năng hiện có

### Giao diện
- Nội dung tiếng Việt và bố cục theo chủ đề cà phê, sử dụng tông màu nâu, kem và vàng.
- Thanh điều hướng đến sản phẩm, phần giới thiệu và đặt hàng.
- Khu vực mở đầu, giới thiệu cam kết thương hiệu và chân trang tự cập nhật năm hiện tại.
- Giao diện responsive cho máy tính, máy tính bảng và điện thoại.

### Sản phẩm
- **22 sản phẩm mẫu** thuộc 3 nhóm: cà phê hạt & bột, cà phê tiện lợi và dụng cụ pha chế.
- Lọc để xem tất cả sản phẩm hoặc từng danh mục.
- Dữ liệu sản phẩm (tên, mô tả, giá, hình ảnh) được khai báo trong JavaScript.

### Giỏ hàng
- Thêm sản phẩm và tăng số lượng khi thêm cùng một mặt hàng nhiều lần.
- Giảm số lượng hoặc loại sản phẩm khỏi giỏ.
- Tự cập nhật số lượng sản phẩm và tổng tiền.

### Tạo đơn hàng demo
- Form nhập tên người nhận, số điện thoại, địa chỉ và ghi chú.
- Kiểm tra giỏ hàng có sản phẩm trước khi tạo nội dung đơn hàng.
- Tổng hợp thông tin khách hàng, sản phẩm, số lượng và tổng tiền thành văn bản.
- Cho phép sao chép nội dung đơn hàng để người dùng tự gửi.

## Công nghệ

| Công nghệ | Vai trò |
| --- | --- |
| HTML5 | Cấu trúc trang, nội dung và biểu mẫu |
| CSS3 | Màu sắc, bố cục, thẻ sản phẩm và giao diện responsive |
| JavaScript | Lọc sản phẩm, giỏ hàng, tính tiền và tạo nội dung đơn |
| GitHub | Lưu trữ mã nguồn và lịch sử thay đổi |
| GitHub Pages | Có thể dùng để xuất bản website tĩnh |

CSS và JavaScript đang nằm bên trong file `index.html`, chưa được tách thành file riêng.

## Cấu trúc dự án

```text
website-ca-phe/
├── index.html
├── README.md
└── .vscode/
    └── extensions.json
```

## Nhật ký thay đổi và đồng bộ dự án

### 1. Website gốc trong repository OpenClaw
- Giữ website Mộc Coffee tại `website-ca-phe/index.html`.
- Kiểm tra nội dung HTML, CSS và JavaScript để ghi nhận các tính năng hiện có.
- Không có thay đổi chức năng HTML nào được xác nhận trong lần rà soát này.

### 2. Sao chép sang repository học tập
- Sao chép website sang `projects/moc-coffee/index.html` trong [MulSuLinh/python-journey](https://github.com/MulSuLinh/python-journey).
- Bản sao được kiểm tra có cùng nội dung với file nguồn tại thời điểm kiểm tra.
- Tạo README riêng cho bản sao, gồm mô tả tính năng, công nghệ, cách chạy, giới hạn và hướng phát triển.

Các commit đã ghi nhận ở repository bản sao:
- [Thêm website Mộc Coffee](https://github.com/MulSuLinh/python-journey/commit/7dfa3793cc233ae00a663ecdeff7daa656c86e65)
- [Thêm README cho website](https://github.com/MulSuLinh/python-journey/commit/48a27c5f74bbe54b50e3445ce4b8003820b11460)
- [Cập nhật README và nhật ký thay đổi](https://github.com/MulSuLinh/python-journey/commit/4917914b9b12d8c4ff0675191b3d2bb701fdbe5f)

### 3. Cập nhật tài liệu ở repository này
- Mở rộng README này để ghi rõ tính năng, công nghệ, cấu trúc, giới hạn và cách chạy.
- Thêm liên kết đến bản sao trên `python-journey` và các commit liên quan.
- Ghi rõ trạng thái GitHub Pages chưa được xác nhận.
- Đây là cập nhật tài liệu; không đồng nghĩa với việc website đã được bổ sung chức năng mới.

## Chạy website trên Windows

### Cách 1 — Dùng Visual Studio Code và Live Server
1. Clone repository:

   ```bash
   git clone https://github.com/MulSuLinh/openclaw.git
   ```

2. Trong VS Code, chọn **File → Open Folder...** và mở thư mục `openclaw/website-ca-phe`.
3. Mở **Extensions**, cài extension **Live Server** nếu chưa có.
4. Nhấp chuột phải vào `index.html`, chọn **Open with Live Server**.

### Cách 2 — Mở trực tiếp
Mở thư mục `website-ca-phe` trong File Explorer và nhấp đúp `index.html` để mở bằng trình duyệt.

## Giới hạn hiện tại

- Đây là website demo tĩnh, chưa phải cửa hàng trực tuyến hoàn chỉnh.
- Đơn hàng chỉ được tạo thành văn bản để sao chép; không tự gửi đến người bán và không lưu trên máy chủ.
- Chưa có backend, cơ sở dữ liệu, đăng nhập, quản lý kho, quản lý đơn hàng hoặc trang quản trị.
- Chưa tích hợp cổng thanh toán hay API vận chuyển.
- Giỏ hàng chỉ tồn tại trong bộ nhớ JavaScript; tải lại trang có thể làm mất giỏ hàng.
- Sản phẩm, giá và mô tả là dữ liệu mẫu, cần xác minh trước khi dùng cho kinh doanh thật.
- Ảnh tải từ Unsplash nên cần kết nối Internet.

## Hướng phát triển tiếp theo

- [ ] Tách CSS và JavaScript thành các file riêng.
- [ ] Lưu giỏ hàng bằng `localStorage`.
- [ ] Bổ sung kiểm tra dữ liệu biểu mẫu.
- [ ] Kết nối backend và cơ sở dữ liệu để lưu đơn hàng.
- [ ] Xây dựng trang quản trị sản phẩm và đơn hàng.
- [ ] Tích hợp liên hệ, vận chuyển và thanh toán an toàn.
- [ ] Bật và xác minh GitHub Pages nếu muốn xuất bản website.

## Lưu ý về GitHub Pages

Để xuất bản bản sao nằm trong `python-journey/projects/moc-coffee`, vào repository `python-journey` → **Settings → Pages**, chọn nguồn triển khai phù hợp, sau đó chờ GitHub hoàn tất và kiểm tra trạng thái xuất bản. Đường dẫn dự kiến là https://mulsulinh.github.io/python-journey/projects/moc-coffee/; không nên xem đây là website đang hoạt động cho đến khi triển khai được xác nhận.

## Trợ lý Mộc Coffee (bản demo)

Website có một khung chat nổi **“Hỏi Mộc AI”** ở góc dưới bên phải. Trợ lý có thể:
- Trả lời câu hỏi cơ bản về sản phẩm và giá mẫu.
- Gợi ý cà phê cho người mới dựa trên mô tả sản phẩm.
- Hướng dẫn thêm sản phẩm vào giỏ và tạo nội dung đơn hàng.
- Trả lời nhanh một số câu hỏi thường gặp về danh mục và giao hàng.

**Lưu ý kỹ thuật:** phiên bản hiện tại là trợ lý hỏi đáp theo từ khóa chạy ngay trong trình duyệt, không cần API key. Đây chưa phải mô hình AI tạo sinh; câu trả lời có giới hạn và không gửi đơn hàng đến cửa hàng. Muốn kết nối AI thật, cần xây dựng backend gọi nhà cung cấp mô hình và lưu khóa API ở phía máy chủ, không đặt khóa bí mật trực tiếp trong HTML/JavaScript công khai.

### Nhật ký cập nhật — Trợ lý chat
- Thêm nút chat nổi và cửa sổ trò chuyện có thể mở/đóng.
- Thêm câu hỏi gợi ý nhanh, ô nhập tin nhắn và phản hồi theo nhóm chủ đề.
- Bổ sung thông báo rõ ràng về giới hạn của bản demo.
- Đồng bộ phần giao diện trợ lý vào bản website-ca-phe trong openclaw và bản sao projects/moc-coffee trong python-journey.
