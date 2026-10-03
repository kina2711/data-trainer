#!/usr/bin/env python3
from promote_l051_l090_common import load_lesson, run
LESSONS = tuple(load_lesson(number) for number in range(56, 61))
if __name__ == "__main__": raise SystemExit(run(56, 60, "1.0.99", "2026-10-03T01:15:00+07:00"))
