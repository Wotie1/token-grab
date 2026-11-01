
import os
import re

print("--- SCANNER ---")

local = os.getenv("LOCALAPPDATA")
roaming = os.getenv("APPDATA")

paths = {}

if roaming:
    paths["Discord"] = os.path.join(roaming, "Discord")

if local:
    paths["Chrome"] = os.path.join(
        local,
        "Google",
        "Chrome",
        "User Data",
        "Default"
    )

# Token benzeri verileri yalnızca tespit etmek için desenler
patterns = [
    re.compile(r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}"),
    re.compile(r"mfa\.[\w-]{84}")
]

def find_indicators(base_path):
    storage_path = os.path.join(
        base_path,
        "Local Storage",
        "leveldb"
    )

    if not os.path.isdir(storage_path):
        return 0

    matches = set()

    try:
        for file_name in os.listdir(storage_path):

            if not file_name.endswith((".ldb", ".log")):
                continue

            file_path = os.path.join(
                storage_path,
                file_name
            )

            try:
                with open(
                    file_path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as file:

                    for line in file:
                        for pattern in patterns:
                            if pattern.search(line):
                                matches.add(file_name)

            except OSError as error:
                print(f"Dosya erişim hatası: {error}")

    except OSError as error:
        print(f"Klasör erişim hatası: {error}")

    return len(matches)


print("\nTarama başlatılıyor...\n")

total = 0

for source, path in paths.items():

    count = find_indicators(path)
    total += count

    print(f"{source}: {count} dosyada eşleşme")

print("\n" + "-" * 40)
print(f"Toplam eşleşme bulunan dosya: {total}")
print("Tarama tamamlandı.")
