SHELL := /bin/bash
VALIDATOR := Tools/Curriculum/Validators/validate_structure.py

.PHONY: help test inventory objectives reference-inventory source-plan source-acquisition roadmap-diagrams web artifact

help: ## Hiển thị lệnh hiện có
	@grep -hE '^[a-z-]+:.*##' $(MAKEFILE_LIST) | sed 's/:.*## /\t/' | expand -t22

test: ## Kiểm tra cấu trúc Material sau migration
	@python3 $(VALIDATOR)

inventory: ## Thống kê phase, module, lesson, roadmap và reference
	@python3 $(VALIDATOR) --inventory

objectives: ## Dựng và kiểm định registry objective cho DA và DE
	@python3 Tools/Curriculum/Build/build_academic_objectives.py
	@python3 Tools/Curriculum/Validators/validate_objectives.py

reference-inventory: ## Kiểm kê tên, kích thước và hash của kho nguồn cục bộ
	@python3 Tools/Curriculum/Build/build_reference_inventory.py

source-plan: objectives reference-inventory ## Dựng và kiểm định kế hoạch nguồn cho toàn bộ objective
	@python3 Tools/Curriculum/Build/build_source_plan.py
	@python3 Tools/Curriculum/Validators/validate_source_plan.py

source-acquisition: source-plan ## Đối soát sách owner đã cung cấp với kế hoạch nguồn
	@python3 Tools/Curriculum/Build/reconcile_source_acquisition.py

roadmap-diagrams: ## Render Mermaid trong 56 roadmap thành ảnh SVG
	@python3 Tools/Curriculum/Build/render_roadmap_diagrams.py

artifact: ## Mở điểm vào của Artifact Rabbit Data
	@echo "Artifact: Artifact/Rabbit-Data/index.html"

web: ## Web chỉ được xây sau khi Artifact được duyệt
	@echo "Web đang bị khóa bởi cổng duyệt Artifact." >&2
	@exit 1
