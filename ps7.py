# Copyright 2025 Vanzel Essien

import sys
import re
from datetime import datetime

# check if command line arguments are correct
if len(sys.argv) != 2:
    print("Usage: python ps7.py <filename>")
    sys.exit(1)

# save filename from command line
filename = sys.argv[1]
output_filename = filename + ".rpt"

# regex patterns
START_PATTERN = re.compile(r'\(log\.c\.166\) server started')
END_PATTERN = re.compile(r'oejs\.AbstractConnector:Started SelectChannelConnector@')
START_TIME_PATTERN = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}):')
END_TIME_PATTERN = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3})')

# open file and read lines
with open(filename, 'r') as file:
    lines = file.readlines()
print("Log file: ", filename)  # debug check
print("Total lines: ", len(lines))  # debug check

# create empty variables for boot process
output = []
boot_active = False

# check each line for start and end
for i, line in enumerate(lines):
    # check for the start of the boot process
    if START_PATTERN.search(line):
        if boot_active:
            output.append(("**** Incomplete boot ****",))
        match = START_TIME_PATTERN.search(line)
        if match:
            start_time_str = match.group(1)
            output.append(("=== Device boot ===", i + 1, start_time_str))
            boot_active = True

    # check for the end of the boot process
    elif boot_active and END_PATTERN.search(line):
        match = END_TIME_PATTERN.search(line)
        if match:
            end_time_str = match.group(1)
            # find last start in output
            for j in reversed(output):
                if isinstance(j, tuple) and j[0] == "=== Device boot ===":
                    start_time_str = j[2]
                    break
            # parse start and end times
            start_dt = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
            end_dt = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S.%f")
            end_dt = end_dt.replace(microsecond=0)
            duration_ms = int((end_dt - start_dt).total_seconds() * 1000)

            output.append((i + 1, end_dt.strftime("%Y-%m-%d %H:%M:%S"), "Boot Completed"))
            output.append((f"\tBoot Time: {duration_ms}ms",))
            boot_active = False

# write output to .rpt file
with open(output_filename, "w") as f:
    for entry in output:
        label = entry[0]

        # boot start
        if label == "=== Device boot ===":
            line_num, timestamp = entry[1], entry[2]
            f.write(f"{label}\n")
            f.write(f"{line_num}({filename}): {timestamp} Boot Start\n")

        # incomplete
        elif label == "**** Incomplete boot ****":
            f.write(f"{label}\n\n")

        # boot end
        elif len(entry) == 3 and label != "=== Device boot ===":
            line_num, timestamp, status = entry
            f.write(f"{line_num}({filename}): {timestamp} {status}\n")

        # duration
        elif len(entry) == 1 and label.startswith("\tBoot Time:"):
            f.write(f"{label}\n")
