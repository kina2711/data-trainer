#!/usr/bin/env python3
from promote_l006_l050_common import load_lesson, run

LESSONS = tuple(load_lesson(number) for number in range(26, 31))

if __name__ == "__main__":
    raise SystemExit(run(26, 30, "1.0.93", "2026-10-03T00:45:00+07:00"))
