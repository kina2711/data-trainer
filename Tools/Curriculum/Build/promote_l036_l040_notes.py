#!/usr/bin/env python3
from promote_l006_l050_common import load_lesson, run

LESSONS = tuple(load_lesson(number) for number in range(36, 41))

if __name__ == "__main__":
    raise SystemExit(run(36, 40, "1.0.95", "2026-10-03T00:55:00+07:00"))
