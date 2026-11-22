# Phân tích và so sánh giấy phép phần mềm nguồn mở

**BTH04 – Yêu cầu 4: Bản quyền nội dung số (cá nhân)**  
Tác giả: Nguyễn Thanh An · Phiên bản: 1.0.0 · Ngày: 22/11/2026  
Giấy phép: [MIT](LICENSE)

## Giới thiệu và mục tiêu
Nghiên cứu ba dự án CNTT sử dụng ba giấy phép khác nhau: **GNU Bash – GPL-3.0-or-later**, **React – MIT**, **Apache Spark – Apache-2.0**. Mục tiêu là nhận diện quyền sử dụng, chỉnh sửa, phân phối, nghĩa vụ khi thương mại hóa và điều kiện tích hợp vào sản phẩm đóng.

## Phương pháp
Đối chiếu văn bản giấy phép và tài liệu chính thức; ghi nguồn, ngày truy cập; chuẩn hóa thành dữ liệu JSON; dùng Python tạo bảng so sánh và tóm tắt. Phân tích tác động cộng đồng là nhận định của tác giả, không phải kết quả đo lường nhân quả. Chỉ số sao/fork là số làm tròn hiển thị khi truy cập, không phải số người dùng.

## Chạy lại kết quả
Yêu cầu Python 3.10 trở lên; không cần thư viện ngoài và không cần mạng.
```bash
python3 src/analyze_licenses.py
python3 -m unittest discover -s tests -v
```
Trên Windows có thể dùng `py` thay cho `python3`.
Đầu ra: `results/comparison.md`, `results/comparison.csv`, `results/summary.json`.
Chương trình kiểm tra dữ liệu theo các trường khai báo, **không tự suy luận giấy phép từ mã nguồn**.

## Kết quả
Cả ba giấy phép cho phép sử dụng thương mại. GPL đặt điều kiện copyleft khi phân phối tác phẩm thuộc phạm vi điều chỉnh; MIT yêu cầu giữ thông báo bản quyền và giấy phép; Apache 2.0 bổ sung các điều kiện như ghi nhận thay đổi, NOTICE khi có và cấp quyền sáng chế trong phạm vi quy định. Không diễn giải GPL thành yêu cầu công khai mọi mã nguồn trong mọi tình huống.

## Cấu trúc
| Thư mục/tệp | Nội dung |
|---|---|
| `data/projects.json` | Ba dự án, thuộc tính giấy phép và nguồn |
| `src/analyze_licenses.py` | Kiểm tra dữ liệu, tạo kết quả |
| `results/` | CSV, Markdown và JSON tái lập được |
| `docs/overleaf/main.tex` | Báo cáo tiếng Việt, có trích dẫn và liên kết |
| `docs/SOURCES.md` | Danh mục nguồn và phạm vi sử dụng |
| `docs/SUBMISSION_CHECKLIST.md` | Đối chiếu với yêu cầu bài thực hành |
| `tests/` | Kiểm thử dữ liệu và xử lý lỗi |
| `LICENSE` | Toàn văn MIT |
| `CONTRIBUTING.md` | Hướng dẫn đóng góp |
| `CITATION.cff` | Thông tin trích dẫn máy đọc được |

## Báo cáo Overleaf
[Báo cáo đã tạo trên Overleaf](https://www.overleaf.com/project/6b02483f91315c2f0c5007a8) · [PDF báo cáo 7 trang](docs/BaoCao.pdf)

Project Overleaf thuộc tài khoản người thực hiện; truy cập cần quyền của chủ project.

Tải thư mục `docs/overleaf/` lên Overleaf, chọn **main.tex**, trình biên dịch **pdfLaTeX**. Chạy Recompile để tạo PDF. Không cần ảnh, font ngoài hoặc BibTeX; tài liệu tham khảo được tích hợp trong nguồn LaTeX.

## Bản quyền và ghi nhận
MIT áp dụng cho mã nguồn, dữ liệu tổng hợp và nội dung gốc của repository này. **Không tái cấp phép GNU Bash, React hay Apache Spark**. Repository không đóng gói mã nguồn của ba dự án. Văn bản giấy phép, nhãn hiệu và tài liệu được dẫn vẫn thuộc chủ thể tương ứng. Ghi nguồn học thuật không thay thế nghĩa vụ giấy phép.
Không chứa dữ liệu cá nhân ngoài tên tác giả và tên tài khoản GitHub công khai.

## Đóng góp và trích dẫn
Xem [CONTRIBUTING.md](CONTRIBUTING.md) và [CITATION.cff](CITATION.cff).
Nguồn chính thức: [GNU Bash](https://www.gnu.org/software/bash/), [React](https://github.com/react/react), [Apache Spark](https://github.com/apache/spark).
