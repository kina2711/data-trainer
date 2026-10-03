#!/usr/bin/env python3
from promote_l051_l090_common import load_lesson, run
LESSONS = tuple(load_lesson(number) for number in range(51, 56))
if __name__ == "__main__": raise SystemExit(run(51, 55, "1.0.98", "2026-10-03T01:10:00+07:00"))
