# Hướng dẫn đóng góp

1. Mở Issue mô tả lỗi dữ liệu, lỗi chương trình hoặc điểm cần bổ sung.
2. Fork repository, tạo nhánh có tên rõ nghĩa (ví dụ `fix/apache-notice`).
3. Với thay đổi về giấy phép, cung cấp URL nguồn chính thức, điều khoản và ngày truy cập; phân biệt sự kiện với nhận định.
4. Sửa `data/projects.json` trước, chạy `python3 src/analyze_licenses.py` để cập nhật kết quả; không sửa tay đầu ra.
5. Chạy `python3 -m unittest discover -s tests -v`. Nếu sửa báo cáo, biên dịch `docs/overleaf/main.tex` bằng pdfLaTeX và kiểm tra bảng, dấu tiếng Việt, liên kết.
6. Gửi Pull Request nêu vấn đề, nội dung sửa và cách kiểm tra.

Chỉ đóng góp nội dung có quyền sử dụng; không đưa mật khẩu, token, dữ liệu cá nhân hoặc mã của bên thứ ba không rõ giấy phép vào repo. Nội dung gốc đóng góp vào dự án được cung cấp theo MIT. Tôn trọng người góp ý và thảo luận dựa trên bằng chứng.
