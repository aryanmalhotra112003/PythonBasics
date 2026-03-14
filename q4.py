import subprocess

def check_updates():
    print("Checking for available updates...\n")

    subprocess.run(["sudo", "apt", "update"])

    result = subprocess.run(
        ["apt", "list", "--upgradable"],
        capture_output=True,
        text=True
    )

    packages = result.stdout.split("\n")[1:] 

    update_list = []

    for i, pkg in enumerate(packages):
        if pkg.strip() != "":
            print(f"{i}. {pkg}")
            update_list.append(pkg.split("/")[0])

    return update_list

def install_updates(packages):

    choice = input("\nUpdate all packages? (yes/no): ")

    try:
        if choice.lower() == "yes":
            print("\nUpdating all packages...\n")
            subprocess.run(["sudo", "apt", "upgrade", "-y"])

        else:
            index = int(input("Enter package index number to update: "))
            pkg_name = packages[index]

            print(f"\nUpdating {pkg_name}...\n")

            subprocess.run(["sudo", "apt", "install", pkg_name, "-y"])

    except Exception as e:
        print("ERROR: Update failed")
        print(e)

packages = check_updates()

if len(packages) == 0:
    print("No updates available.")
else:
    install_updates(packages)