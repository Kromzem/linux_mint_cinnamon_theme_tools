import subprocess

schemas = subprocess.check_output("gsettings list-schemas", shell=True, universal_newlines=True).splitlines()
for schema in schemas:
    keys = subprocess.check_output(f"gsettings list-keys {schema}", shell=True, universal_newlines=True).splitlines()

    for key in keys:
        value = subprocess.check_output(f"gsettings get {schema} {key}", shell=True, universal_newlines=True).splitlines()[0]

        if value == "'Mint-Y-Dark'":
            print(value)
            print(f"Found: {schema} {key}")
            exit(0)
