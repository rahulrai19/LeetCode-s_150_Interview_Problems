import os
import re

with open('leetcode_top_150.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    # pattern to match: - [88] Merge Sorted Array (Easy)
    match = re.search(r'- \[(\d+)\] (.*) \((Easy|Medium|Hard)\)', line)
    if match:
        num = match.group(1)
        name = match.group(2).strip()
        
        # Replace spaces and certain symbols for file name safety
        filename_base = name.replace(' ', '_')
        # Remove any other characters that might be invalid in Windows filenames like : * ? " < > |
        filename_base = re.sub(r'[:*?"<>|]', '', filename_base)
        
        filename = f"{num}_{filename_base}.md"
        filepath = os.path.join(r"D:\DSA\150_Interview_problem", filename)
        
        if not os.path.exists(filepath):
            with open(filepath, 'w', encoding='utf-8') as out_f:
                pass
            print(f"Created {filename}")
