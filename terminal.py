import os
import easygui as eg
import subprocess

while True:
    subprocess.run(["clear"])
    print(""""Select you want to do:
    0. Exit
    1. İnstall ADB & Fastboot
    2. İnstall Recovery
    3. İnstall Fastboot Rom
    4. Show Fastboot Devices
    5. Show ADB Devices
    6. Send File to Phone
    7. Fastboot Things""")

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
            subprocess.run(["clear"])

        elif os == "2":
            subprocess.run(["sudo", "apt", "install", "android-tools-adb", "android-tools-fastboot"])
            subprocess.run(["clear"])

        elif os == "3":
            subprocess.run(["sudo", "pacman", "-S", "android-tools"])
            subprocess.run(["clear"])

        elif os == "4":
            subprocess.run(["sudo", "dnf", "install", "android-tools"])
            subprocess.run(["clear"])

        elif os == "5":
            subprocess.run(["sudo", "zypper", "install", "android-tools"])
            subprocess.run(["clear"])

        elif os == "6":
            subprocess.run(["sudo", "yum", "install", "android-tools"])
            subprocess.run(["clear"])

        elif os == "7":
            subprocess.run(["sudo", "yum", "install", "android-tools"])
            subprocess.run(["clear"])

        elif os == "8":
            subprocess.run(["sudo", "emerge", "android-tools"])
            subprocess.run(["clear"])

        elif os == "9":
            subprocess.run(["sudo", "xbps-install", "android-tools"])
            subprocess.run(["clear"])

        elif os == "10":
            subprocess.run(["sudo", "eopkg", "install", "android-tools"])
            subprocess.run(["clear"])

        elif os == "11":
            subprocess.run(["sudo", "slackpkg", "install", "android-tools"])
            subprocess.run(["clear"])

        elif os == "12":
            subprocess.run(["sudo", "apk", "add", "android-tools"])
            subprocess.run(["clear"])

    elif select == "2":
        recovery = eg.fileopenbox(msg='Select Recovery .img file',
                                  title='Specify File', default='/home/*.img',
                                  filetypes='*.img')
        subprocess.run(["sudo", "fastboot", "flash", "recovery", recovery])
        subprocess.run(["clear"])

    elif select == "3":
        rom = eg.fileopenbox(msg='Select flash_all.sh file',
                             title='Specify File', default='/home/*.sh',
                             filetypes='*.sh')
        subprocess.run(["sudo", "sh", rom])
        subprocess.run(["clear"])

    elif select == "4":
        subprocess.run(["sudo", "fastboot", "devices"])
        subprocess.run(["clear"])

    elif select == "5":
        subprocess.run(["sudo", "adb", "devices"])
        subprocess.run(["clear"])

    elif select == "6":
        file = eg.fileopenbox(msg='Select File to Send',
                              title='Specify File', default='/home/*.*',
                              filetypes='*.*')
        subprocess.run(["sudo", "adb", "push", file, "/sdcard/"])
        subprocess.run(["clear"])

    elif select == "7":
        print(""" Fastboot Things:
        1. fastboot devices [-l] (with the path of the device/s)
        2. Find Device Information
        3. Reboot Your Device
        4. Reboot Your Device into Recovery Mode
        5. Reboot Your Device into Bootloader/Fastboot Mode
        6. Fastboot Commands to Flash TWRP and System Image""")

    fastbootthings = input("Select: ")

    if fastbootthings == "1":
        subprocess.run(["sudo", "fastboot", "devices", "-l"])
        subprocess.run(["clear"])

    elif fastbootthings == "2":
        subprocess.run(["sudo", "fastboot", "getvar", "all"])

    elif fastbootthings == "3":
        subprocess.run(["sudo", "fastboot", "reboot"])

    elif fastbootthings == "4":
        subprocess.run(["sudo", "fastboot", "reboot", "recovery"])

    elif fastbootthings == "5":
        subprocess.run(["sudo", "fastboot", "reboot", "bootloader"])

    elif fastbootthings == "6":
        print("""Fastboot Commands to Flash TWRP and System Image:
        1.fastboot flash boot boot.img
        2.fastboot flash system system.img
        3. fastboot flash recovery recovery.img
        4. fastboot flash cache cache.img
        5. fastboot flash modem NON-HLOS.bin
        6. fastboot flash sbl1 sbl1.mbn
        7. fastboot flash dbi sdi.mbn
        8. fastboot flash aboot emmc_appsboot.mbn
        9. fastboot flash rpm rpm.mbn
        10. fastboot flash tz tz.mbn
        11. fastboot flash LOGO logo.bin""")
        flash = input("Select: ")

        if flash == "1":
            boot = eg.fileopenbox(msg='Select boot.img file',
                                  title='Specify File', default='/home/*.img',
                                  filetypes='*.img')
            subprocess.run(["sudo", "fastboot", "flash", "boot", boot])
            subprocess.run(["clear"])

        elif flash == "2":
            system = eg.fileopenbox(msg='Select system.img file',
                                    title='Specify File', default='/home/*.img',
                                    filetypes='*.img')
            subprocess.run(["sudo", "fastboot", "flash", "system", system])
            subprocess.run(["clear"])

        elif flash == "3":
            recovery = eg.fileopenbox(msg='Select recovery.img file',
                                      title='Specify File', default='/home/*.img',
                                      filetypes='*.img')
            subprocess.run(["sudo", "fastboot", "flash", "recovery", recovery])
            subprocess.run(["clear"])

        elif flash == "4":
            cache = eg.fileopenbox(msg='Select cache.img file',
                                   title='Specify File', default='/home/*.img',
                                   filetypes='*.img')
            subprocess.run(["sudo", "fastboot", "flash", "cache", cache])
            subprocess.run(["clear"])

        elif flash == "5":
            modem = eg.fileopenbox(msg='Select NON-HLOS.bin file',
                                   title='Specify File', default='/home/*.bin',
                                   filetypes='*.bin')
            subprocess.run(["sudo", "fastboot", "flash", "modem", modem])
            subprocess.run(["clear"])

        elif flash == "6":
            sbl1 = eg.fileopenbox(msg='Select sbl1.mbn file',
                                  title='Specify File', default='/home/*.mbn',
                                  filetypes='*.mbn')
            subprocess.run(["sudo", "fastboot", "flash", "sbl1", sbl1])
            subprocess.run(["clear"])

        elif flash == "7":
            dbi = eg.fileopenbox(msg='Select sdi.mbn file',
                                 title='Specify File', default='/home/*.mbn',
                                 filetypes='*.mbn')
            subprocess.run(["sudo", "fastboot", "flash", "dbi", dbi])
            subprocess.run(["clear"])

        elif flash == "8":
            aboot = eg.fileopenbox(msg='Select emmc_appsboot.mbn file',
                                   title='Specify File', default='/home/*.mbn',
                                   filetypes='*.mbn')
            subprocess.run(["sudo", "fastboot", "flash", "aboot", aboot])
            subprocess.run(["clear"])

        elif flash == "9":
            rpm = eg.fileopenbox(msg='Select rpm.mbn file',
                                 title='Specify File', default='/home/*.mbn',
                                 filetypes='*.mbn')
            subprocess.run(["sudo", "fastboot", "flash", "rpm", rpm])
            subprocess.run(["clear"])

        elif flash == "10":
            tz = eg.fileopenbox(msg='Select tz.mbn file',
                                title='Specify File', default='/home/*.mbn',
                                filetypes='*.mbn')
            subprocess.run(["sudo", "fastboot", "flash", "tz", tz])
            subprocess.run(["clear"])

        elif flash == "11":
            logo = eg.fileopenbox(msg='Select logo.bin file',
                                  title='Specify File', default='/home/*.bin',
                                  filetypes='*.bin')
            subprocess.run(["sudo", "fastboot", "flash", "logo", logo])
            subprocess.run(["clear"])
