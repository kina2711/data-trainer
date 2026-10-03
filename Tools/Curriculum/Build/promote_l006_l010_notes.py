#!/usr/bin/env python3
from promote_l006_l050_common import load_lesson, run

LESSONS = tuple(load_lesson(number) for number in range(6, 11))

if __name__ == "__main__":
    raise SystemExit(run(6, 10, "1.0.89", "2026-10-03T00:25:00+07:00"))
