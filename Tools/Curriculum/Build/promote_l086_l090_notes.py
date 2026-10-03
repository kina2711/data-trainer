#!/usr/bin/env python3
from promote_l051_l090_common import load_lesson, run
LESSONS = tuple(load_lesson(number) for number in range(86, 91))
if __name__ == "__main__": raise SystemExit(run(86, 90, "1.0.105", "2026-10-03T01:45:00+07:00"))
