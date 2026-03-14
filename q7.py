sizes = [
    "nano","micro","small","medium","large",
    "xlarge","2xlarge","4xlarge","8xlarge",
    "16xlarge","32xlarge"
]

latest_generation = {
    "t2": "t3",
    "t3": "t4g"
}

def print_table(rows):

    num_cols = len(rows[0])
    col_widths = [0] * num_cols

    for row in rows:
        for i in range(num_cols):
            col_widths[i] = max(col_widths[i], len(str(row[i])))

    def border():
        print("+", end="")
        for w in col_widths:
            print("-" * (w + 2) + "+", end="")
        print()

    def print_row(row):
        print("|", end="")
        for i, cell in enumerate(row):
            print(" " + str(cell).ljust(col_widths[i]) + " |", end="")
        print()

    border()
    print_row(rows[0])
    border()

    for row in rows[1:]:
        print_row(row)

    border()


current_instance = input("Current EC2 Instance (e.g. t2.large): ")
cpu = int(input("CPU Utilization (%): ").replace("%",""))

instance_type, instance_size = current_instance.split(".")

index = sizes.index(instance_size)


status = ""
recommended = current_instance

if cpu < 20:
    status = "Underutilized"
    if index > 0:
        recommended = instance_type + "." + sizes[index-1]
    else:
        recommended = "Already smallest size"

elif cpu > 80:
    status = "Overutilized"
    if index < len(sizes)-1:
        recommended = instance_type + "." + sizes[index+1]
    else:
        recommended = "Already largest size"

else:
    status = "Optimized"
    new_type = latest_generation.get(instance_type, instance_type)
    recommended = new_type + "." + instance_size


table = [
    ["Serial No.", "Current EC2", "Current CPU", "Status", "Recommended EC2"],
    ["1", current_instance, str(cpu)+"%", status, recommended]
]

print("\nRecommendation Table:\n")
print_table(table)