import subprocess

# Retrieve the raw output of saved Wi-Fi profiles
profiles = subprocess.check_output("netsh wlan show profiles", shell=True).decode("utf-8", errors="ignore")

# Parse the output to extract profile names
names = [line.split(":")[1].strip() 
         for line in profiles.split("\n") if "All User Profile" in line]

# Enumerate and display the list to the user
for i, n in enumerate(names, 1):
    print(f"[{i}] {n}")

# Prompt user for selection
ch = int(input("\nChoose WiFi number: "))
wifi = names[ch - 1]

# Fetch the specific profile details including the cleartext password
result = subprocess.check_output(
    f'netsh wlan show profile "{wifi}" key=clear', 
    shell=True
).decode("utf-8", errors="ignore")

print("\n" + result)