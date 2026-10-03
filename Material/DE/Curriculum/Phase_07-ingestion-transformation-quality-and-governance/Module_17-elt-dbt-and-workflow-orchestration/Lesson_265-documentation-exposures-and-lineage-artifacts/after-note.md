# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 265: Documentation Exposures and Lineage Artifacts

## Thực hành

**Nhiệm vụ.** Khai báo bốn thứ cho mọi mô hình phục vụ và khai báo bên tiêu thụ cho từng cái. Sinh tài liệu và đồ thị dòng dõi. Viết phép kiểm chặn mô hình công khai thiếu tài liệu, thiếu chủ sở hữu, hoặc thiếu khai báo hạt. Tiêm ba vi phạm và xác nhận bị chặn. Dùng dòng dõi để trả lời câu một cột nguồn đổi thì bảng điều khiển nào ảnh hưởng.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn tự động có tiêu chí nghiệm thu bằng phép thử tiêm. Kiểm bằng ba vi phạm tiêm; đạt khi cả ba bị chặn và đồ thị dòng dõi phủ đủ bên tiêu thụ đã khai báo.

**Điều kiện đạt.** Ba vi phạm bị chặn ở cửa hợp nhất, và dòng dõi trả lời được câu hỏi ảnh hưởng từ một cột nguồn tới bảng điều khiển.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Viết tài liệu trong trang riêng ngoài kho mã · bỏ khai báo bên tiêu thụ nên không kiểm kê được · coi dòng dõi kỹ thuật là đủ · để mô hình công khai không tài liệu qua cửa hợp nhất.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/153-documentation-exposures-lineage-artifacts.md`
- Nội dung học thuật: `note.md` cùng thư mục.
