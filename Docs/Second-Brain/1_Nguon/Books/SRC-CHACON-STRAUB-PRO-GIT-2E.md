---
source_id: src.book.chacon-straub-pro-git.2e
source_type: book
title: Pro Git
authors:
  - Scott Chacon
  - Ben Straub
publisher: Apress
edition: second-edition
published: 2014
captured: 2026-10-02
status: active-private-source
rights: copyrighted-private-owner-provided
sensitivity: private
authority: practitioner-primary-reference
sha256: fe6c23508d76a5e31a2022dd34bbb21005e194f168a4608f273099f3c3b4b3ab
canonical_path: /home/kina2711/PROJECT/data-trainer/Material/Reference_temp/Pro_Git_-_Scott_Chacon.pdf
extraction_method: pdftotext-layout-bounded-page-range
tags: [source/book, git, version-control, object-database]
aliases: [Pro Git Second Edition]
---

# Pro Git Second Edition — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn được dùng cho mô hình ba vùng của Git, object database, references, branching, three-way merge, conflict, rebase, reset và commit identity.

## Provenance

- PDF do chủ dự án cung cấp trong `Material/Reference_temp`.
- SHA-256 được tính trực tiếp; tệp có 906 trang, không mã hóa và có text layer.
- Trang bản quyền ghi Scott Chacon và Ben Straub, Apress, Second Edition, 2014, ISBN 978-1-4842-0077-3.
- Metadata cho biết tệp được tạo lại bằng Calibre; chưa xác minh chữ ký số hoặc provenance của bản phân phối.
- Không sao chép PDF vào vault và không tái phân phối nội dung sách.

## Phạm vi đã đọc

- Chapter 1, *The Three States*: working directory, staging area/index và Git directory; PDF 42–43.
- Chapter 3, *Basic Branching and Merging*: branch pointer, `HEAD`, fast-forward, three-way merge và conflict; PDF 129–144.
- Chapter 3, *Rebasing* và *The Perils of Rebasing*: replay commit, lịch sử mới và rủi ro với lịch sử đã chia sẻ; PDF 164–174.
- Chapter 7, *Reset Demystified*: quan hệ giữa `HEAD`, index, working tree và các mode của reset; PDF 422–434.
- Chapter 10, *Git Objects* và *Git References*: blob, tree, commit, tag, refs và symbolic `HEAD`; PDF 762–790.

## Giới hạn

- Sách xuất bản năm 2014; tên nhánh mặc định và một số output/command cũ không được xem là chuẩn hiện hành.
- Mô hình object và graph ổn định hơn cú pháp giao diện. Lab phải ghi phiên bản Git thực tế và dùng `git switch`/`git restore` khi phù hợp.
- Ví dụ trong sách dùng SHA-1. Git hiện đại có thể dùng object format khác; note chỉ dựa vào tính chất content-addressed và identity thay đổi khi nội dung commit thay đổi.

## Note dẫn xuất

- [[Git as a content-addressed object database]]
- [[Branching merge rebase and commit identity]]
