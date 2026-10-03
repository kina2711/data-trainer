#!/usr/bin/env python3
from promote_l006_l050_common import load_lesson, run

LESSONS = tuple(load_lesson(number) for number in range(11, 16))

if __name__ == "__main__":
    raise SystemExit(run(11, 15, "1.0.90", "2026-10-03T00:30:00+07:00"))
