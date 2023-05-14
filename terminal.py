import os
import easygui as eg
import subprocess

subprocess.run(["clear"])
print(""""Select you want to do:
0. Exit
1. İnstall ADB & Fastboot
2. İnstall Recovery
3. İnstall Fastboot Rom
4. Show Fastboot Devices
5. Show ADB Devices
6. Send File to Phone""")

select = input("Select: ")

if select == "0":
    os.system("exit")
    subprocess.run(["clear"])


# Install ADB & Fastboot
elif select == "1":
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

elif select == "2":
    recovery = eg.fileopenbox(msg='Select Recovery .img file',
                    title='Specify File', default='/home/*.img',
                    filetypes='*.img')
    subprocess.run(["sudo", "fastboot", "flash", "recovery", recovery])

elif select == "3":
    rom = eg.fileopenbox(msg='Select flash_all.sh file',
                    title='Specify File', default='/home/*.sh',
                    filetypes='*.sh')
    subprocess.run(["sudo", "sh", rom])

elif select == "4":
    subprocess.run(["sudo", "fastboot", "devices"])

elif select == "5":
    subprocess.run(["sudo", "adb", "devices"])

elif select == "6":
    file = eg.fileopenbox(msg='Select File to Send',
                    title='Specify File', default='/home/*.*',
                    filetypes='*.*')
    subprocess.run(["sudo", "adb", "push", file, "/sdcard/"])