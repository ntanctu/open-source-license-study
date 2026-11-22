"""Generate reproducible comparison outputs. SPDX-License-Identifier: MIT."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"GNU Bash": "GPL-3.0-or-later", "React": "MIT", "Apache Spark": "Apache-2.0"}
COLUMNS = [
    ("project", "Dự án"), ("license", "Giấy phép"), ("category", "Nhóm"),
    ("commercial_use", "Cho phép thương mại"),
    ("modified_source_on_distribution", "Nghĩa vụ mã nguồn"),
    ("closed_derivative_distribution", "Phân phối sản phẩm đóng"),
    ("notices", "Thông báo"), ("patents", "Sáng chế"),
]

def validate(rows):
    if not isinstance(rows, list) or len(rows) != 3:
        raise ValueError("Cần đúng ba dự án.")
    if {r.get("project") for r in rows} != set(EXPECTED):
        raise ValueError("Tên dự án bị thiếu hoặc trùng.")
    for row in rows:
        if row.get("license") != EXPECTED[row["project"]]:
            raise ValueError("Giấy phép không khớp hồ sơ nghiên cứu.")
        for key, _ in COLUMNS:
            if key not in row or (key != "commercial_use" and not row[key]):
                raise ValueError("Thiếu dữ liệu: " + key)
        if not isinstance(row["commercial_use"], bool):
            raise ValueError("commercial_use phải là boolean.")
        if not row.get("sources") or not all(u.startswith("https://") for u in row["sources"]):
            raise ValueError("Thiếu URL nguồn HTTPS.")
        if not row.get("accessed"):
            raise ValueError("Thiếu ngày truy cập.")
    return rows

def display(value):
    return ("Có" if value else "Không") if isinstance(value, bool) else str(value)

def generate(rows, output_dir):
    validate(rows)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    headers = [label for _, label in COLUMNS]
    table = [[display(row[key]) for key, _ in COLUMNS] for row in rows]
    with (output_dir / "comparison.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(table)
    def md(values):
        return "| " + " | ".join(v.replace("|", "\\|").replace("\n", " ") for v in values) + " |"
    markdown = "# Bảng so sánh giấy phép\n\n" + md(headers) + "\n" + md(["---"] * len(headers)) + "\n"
    markdown += "\n".join(md(row) for row in table)
    markdown += "\n\nNguồn và ngày truy cập: [data/projects.json](../data/projects.json).\n"
    (output_dir / "comparison.md").write_text(markdown, encoding="utf-8")
    summary = {"project_count": len(rows), "distinct_licenses": sorted({r["license"] for r in rows}),
               "commercial_use_allowed_count": sum(r["commercial_use"] for r in rows),
               "source": "data/projects.json", "observation_date": "2026-11-22",
               "scope": "Mô tả ba trường hợp; không suy rộng thống kê."}
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary

if __name__ == "__main__":
    data = json.loads((ROOT / "data/projects.json").read_text(encoding="utf-8"))
    result = generate(data, ROOT / "results")
    print(json.dumps(result, ensure_ascii=False, indent=2))
