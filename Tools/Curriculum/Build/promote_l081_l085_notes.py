#!/usr/bin/env python3
from promote_l051_l090_common import load_lesson, run
LESSONS = tuple(load_lesson(number) for number in range(81, 86))
if __name__ == "__main__": raise SystemExit(run(81, 85, "1.0.104", "2026-10-03T01:40:00+07:00"))
