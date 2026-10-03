# Phase 3: Software and Backend Engineering
# Module 7: Software Design and Delivery
# Lesson 93: The test pyramid and where to place a double

## Thực hành

**Nhiệm vụ.** Cho mười tình huống cần kiểm. Đặt mỗi cái vào một tầng và nêu có dùng bộ thay thế không, ở ranh giới nào. Cài đặt chúng. Sau đó tái cấu trúc nội bộ một mô đun mà giữ nguyên hành vi, và chứng minh không phép kiểm nào phải sửa.

#### Bằng chứng cho DE-L093

Nộp:

1. bảng mười tình huống, tầng và quyết định double;
2. sơ đồ scope cho mỗi nhóm test;
3. command và thời gian chạy theo tầng;
4. refactor diff;
5. checksum test files trước/sau;
6. kết quả tất cả tầng;
7. failure example chứng minh integration test bắt lỗi fake bỏ sót;
8. danh sách E2E còn lại và rủi ro mỗi test bảo vệ.

## Kiểm tra cuối bài

#### Câu hỏi tự kiểm tra

1. Scope nhỏ nhất cho SQL timezone conversion là gì?
2. Stub và mock khác ở quan sát nào?
3. Vì sao fake repository không chứng minh unique constraint?
4. Test double nên nằm ở boundary nào?
5. Khi nào interaction assertion là behavior thật?
6. Vì sao pipeline dữ liệu cần integration layer dày?
7. Characterization test có chứng minh behavior đúng không?
8. E2E giữ lại để bảo vệ rủi ro nào?
9. Checksum test trước/sau refactor chứng minh gì?
10. Flaky test phải được xử lý như thế nào?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi phán đoán về vị trí và phạm vi phép kiểm, chỗ hay làm sai theo hướng tốn kém. Kiểm bằng phép thử tái cấu trúc; đạt khi bộ kiểm vẫn xanh sau khi đổi cấu trúc nội bộ mà không sửa phép kiểm nào.

**Điều kiện đạt.** Mười phép kiểm đặt đúng tầng, và sau khi tái cấu trúc nội bộ thì bộ kiểm xanh mà không sửa phép kiểm nào.

#### Ma trận đánh giá

| Tiêu chí | Đạt | Không đạt |
|---|---|---|
| Scope | nhỏ nhất nhưng giữ đúng rủi ro | E2E cho mọi thứ hoặc unit hóa boundary thật |
| Double | ở port/protocol ngoài scope | mock private collaborator |
| Integration | DB/file/protocol thật khi cần | fake rồi kết luận integration đúng |
| Refactor resilience | test không đổi, vẫn xanh | sửa mock expectation |
| Diagnosis | failure chỉ vùng lỗi hẹp | lỗi E2E mơ hồ |
| Evidence | thời gian, command, checksum, diff | chỉ ảnh CI xanh |

## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Làm lại lab từ đầu, không nhìn hướng dẫn, rồi làm phần mở rộng; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Thay thế thành phần bên trong · viết phép kiểm đầu cuối cho mọi thứ vì thấy chắc chắn hơn · bỏ tầng tích hợp vì chậm · tái cấu trúc mã cũ mà không có phép kiểm đặc tả.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và một đoạn giải thích ngắn cho mỗi quyết định kỹ thuật. Không chấp nhận ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/05-test-strategy-double-boundary.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
