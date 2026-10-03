#!/usr/bin/env python3
from promote_l006_l050_common import load_lesson, run

LESSONS = tuple(load_lesson(number) for number in range(31, 36))

if __name__ == "__main__":
    raise SystemExit(run(31, 35, "1.0.94", "2026-10-03T00:50:00+07:00"))
