file_path = "emp.csv"

rows = []
with open(file_path, "r") as f:
    for line in f:
        rows.append(line.strip().split(","))

num_cols = len(rows[0])
col_widths = [0] * num_cols

for row in rows:
    for i in range(num_cols):
        col_widths[i] = max(col_widths[i], len(row[i]))

def print_border():
    print("+", end="")
    for w in col_widths:
        print("-" * (w + 2) + "+", end="")
    print()

def print_row(row):
    print("|", end="")
    for i, cell in enumerate(row):
        print(" " + cell.ljust(col_widths[i]) + " |", end="")
    print()

print_border()
print_row(rows[0])  
print_border()

for row in rows[1:]:
    print_row(row)

print_border()