# Bộ ôn tập Reading Room

Mở **`on-tap-trac-nghiem.html`** bằng Chrome, Edge hoặc Firefox. Đây là một file độc lập, đã nhúng tất cả ảnh, có thể sao chép riêng sang máy khác. Trang hoạt động ngoại tuyến, không cần cài thư viện hay chạy máy chủ.

Bản mã nguồn dùng `index.html`. Khi dùng bản này, giữ `index.html`, `style.css`, `app.js`, `data.js` và thư mục `image` cạnh nhau. Sau khi sửa mã nguồn, chạy `python package_quiz.py` để tạo lại bản HTML độc lập.

- 54 câu gốc mang số 147–200, được sắp xếp tăng dần, giữ thứ tự A–D.
- 180 câu bổ sung mang số BS001–BS180, soạn từ thông tin trong các đoạn đọc. Tổng cộng 234 câu; không phải 234 câu nguyên bản trong ảnh.
- Chọn đáp án rồi dùng **Kiểm tra câu này** để xem lời giải, hoặc **Chấm bài đã làm** để tính kết quả trên những câu đã trả lời.
- Tiến độ lưu trong trình duyệt hiện tại. Chuyển trình duyệt hoặc xóa dữ liệu trình duyệt có thể mất tiến độ; có thể tải bản kết quả JSON.
- Bộ lọc câu sai chỉ bao gồm câu đã kiểm tra. Các bộ lọc không làm thay đổi thứ tự.
- **Đối chiếu ảnh tài liệu gốc** mở ảnh tương ứng. Một nhóm đọc có thể nằm trên hai ảnh liền nhau; các ảnh gốc đều ở thư mục `image`.

Các câu gốc 150, 161 có phương án được khôi phục vì mép ảnh cắt chữ. Câu 157, 181, 195 có điểm mơ hồ được ghi chú trên trang. Đáp án là lời giải suy luận từ đoạn đọc và ghi chú tay trong ảnh, không phải đáp án chính thức của nhà xuất bản. Ở câu 196, đáp án là A theo nội dung mục lục, dù ghi chú tay bên cạnh là D. Câu 197 chọn D theo mục đích thư mời. Câu 198 chọn C theo thông tin họp mỗi quý.

Đây là trang cục bộ, chưa được đưa lên dịch vụ hosting.

`build_quiz.py` là nguồn dữ liệu có thể chỉnh sửa. Chạy `python build_quiz.py` để tạo lại `data.js`; script kiểm tra đủ số gốc 147–200 và tối thiểu 201 câu.
