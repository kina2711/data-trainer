#!/usr/bin/env python3
from promote_l051_l090_common import load_lesson, run
LESSONS = tuple(load_lesson(number) for number in range(71, 76))
if __name__ == "__main__": raise SystemExit(run(71, 75, "1.0.102", "2026-10-03T01:30:00+07:00"))
