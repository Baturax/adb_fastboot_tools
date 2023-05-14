import os
import easygui as eg
import subprocess

subprocess.run(["clear"])
print(""""Select you want to do:
0. Exit
1. İnstall ADB & Fastboot""")

select = input("Select: ")


# Install ADB & Fastboot
if select == "1":
    print("""Select your OS:
    1. Ubuntu
    2. Debian
    3. Arch
    4. Fedora
    5. OpenSUSE
    6. CentOS
    7. RHEL
    8. Gentoo
    9. Void
    10. Solus
    11. Slackware
    12. Alpine""")
    os = input("Select: ")
    if os == "1":
        subprocess.run(["sudo", "apt", "install", "android-tools-adb", "android-tools-fastboot"])

    elif os == "2":
        subprocess.run(["sudo", "apt", "install", "android-tools-adb", "android-tools-fastboot"])

    elif os == "3":
        subprocess.run(["sudo", "pacman", "-S", "android-tools"])

    elif os == "4":
        subprocess.run(["sudo", "dnf", "install", "android-tools"])

    elif os == "5":
        subprocess.run(["sudo", "zypper", "install", "android-tools"])

    elif os == "6":
        subprocess.run(["sudo", "yum", "install", "android-tools"])

    elif os == "7":
        subprocess.run(["sudo", "yum", "install", "android-tools"])

    elif os == "8":
        subprocess.run(["sudo", "emerge", "android-tools"])

    elif os == "9":
        subprocess.run(["sudo", "xbps-install", "android-tools"])

    elif os == "10":
        subprocess.run(["sudo", "eopkg", "install", "android-tools"])

    elif os == "11":
        subprocess.run(["sudo", "slackpkg", "install", "android-tools"])

    elif os == "12":
        subprocess.run(["sudo", "apk", "add", "android-tools"])