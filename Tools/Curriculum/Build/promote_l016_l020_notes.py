#!/usr/bin/env python3
from promote_l006_l050_common import load_lesson, run

LESSONS = tuple(load_lesson(number) for number in range(16, 21))

if __name__ == "__main__":
    raise SystemExit(run(16, 20, "1.0.91", "2026-10-03T00:35:00+07:00"))
