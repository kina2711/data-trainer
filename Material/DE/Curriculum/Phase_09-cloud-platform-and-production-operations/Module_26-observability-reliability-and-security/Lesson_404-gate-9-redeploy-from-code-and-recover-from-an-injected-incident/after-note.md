# Phase 9: Cloud Platform and Production Operations
# Module 26: Observability, Reliability and Security
# Lesson 404: Gate 9 - redeploy from code and recover from an injected incident

## Thực hành

**Nhiệm vụ.** Buổi 180 phút: 135 phút làm bài độc lập, 45 phút chữa bài. Bài chấm sáu phần: A (20đ) dựng lại một lát cắt hệ trong môi trường sạch chỉ từ mã, kho ảnh và bản sao lưu, không thao tác tay · B (15đ) chẩn đoán ba khối lượng công việc hỏng theo đúng thứ tự bằng chứng · C (20đ) một sự cố được tiêm; chạy vòng đời sự cố, xác định phạm vi ảnh hưởng bằng bằng chứng và phục hồi · D (15đ) định nghĩa một chỉ số phục vụ từ sự kiện thô đủ bốn phần và dẫn ra một quyết định phát hành từ ngân sách sai sót · E (15đ) trình mô hình mối đe doạ và chỉ ra chốt kiểm soát cho ba rủi ro lớn nhất, đủ ít nhất hai nhóm · F (15đ) trình bảng chi phí trên mỗi đơn vị và một phương án cho cú sốc chi phí gấp mười.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Cổng đo năng lực vận hành đầu cuối, nên hình thức là thực hành tại chỗ cộng bảo vệ.

**Điều kiện đạt.** Đạt ≥ 70/100, phần A và C đều ≥ 60%. Dùng thao tác tay để hoàn thành phần A thì phần đó bằng không; phục hồi ở phần C mà không đối soát dữ liệu thì phần đó bằng không.

## Bài làm sau buổi học

**Nhiệm vụ.** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Lỗi cần chủ động loại trừ.** Sửa trực tiếp trên cụm thay vì qua mã · gọi người trực vì một số đo không hành động được · phục hồi mà không đối soát dữ liệu · trình mô hình mối đe doạ chỉ có chốt ngăn chặn.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/292-gate-9-redeploy-from-code-and-recover-from-an-injected-incident.md`
- Nội dung học thuật: `note.md` cùng thư mục.
