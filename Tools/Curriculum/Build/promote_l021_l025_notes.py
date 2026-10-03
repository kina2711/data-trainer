#!/usr/bin/env python3
from promote_l006_l050_common import load_lesson, run

LESSONS = tuple(load_lesson(number) for number in range(21, 26))

if __name__ == "__main__":
    raise SystemExit(run(21, 25, "1.0.92", "2026-10-03T00:40:00+07:00"))
