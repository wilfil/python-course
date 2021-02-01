#!/usr/bin/env python3.9

import os


stage = os.getenv("STAGE", default="dev").upper()


output = f"We're running in {stage}"


if stage.startswith("prod"):
    output = "DANGER!!! - " + output

print(output)
