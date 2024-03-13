import numpy as np
import sys

# just here as a reminder
COCAPTAIN = '2023-06'
# Use to calculate other projects
current_project = COCAPTAIN

starting = np.datetime64(current_project)
print('Which month do you want to calculate?')
target_month = input().lower()

try:
    if target_month.startswith('m'):
        target_month = target_month[1:]
    target_month = int(target_month)
except ValueError:
    print('The script expects an the input to be a integer or a interger prefixed by M (e.g., M9, m9 or 9)')
    sys.exit(1)

delta = np.timedelta64(target_month-1, 'M')
print(f'M{target_month} correspond to {starting+delta}')
