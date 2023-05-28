import subprocess
from colorama import init, Fore
init()

# clear screen
subprocess.run(["clear"])

# mainmenu
mainmenu = Fore.LIGHTWHITE_EX + "Select your option:\n" + Fore.LIGHTRED_EX + "0. Exit\n" + Fore.LIGHTCYAN_EX + "2. ADB Commands:\n\t" + Fore.GREEN + "a. Show ADB devices\n\t" + Fore.MAGENTA + "b. Reboot device\n\t" + Fore.BLUE + "c. Reboot to Bootloader"
print(mainmenu)


# print OS menu
osmenu = Fore.WHITE + "Select your OS:\n" + Fore.RED + " 1. Ubuntu\n" + Fore.CYAN + " 2. Debian\n" + Fore.GREEN + " 3. Arch\n" + Fore.MAGENTA + " 4. Fedora\n" + Fore.BLUE + " 5. OpenSUSE\n" + Fore.RED + " 6. CentOS\n" + Fore.CYAN + " 7. RHEL\n" + Fore.GREEN + " 8. Gentoo\n" + Fore.MAGENTA + " 9. Void\n" + Fore.BLUE + "10. Solus\n" + Fore.RED + "11. Slackware\n" + Fore.CYAN + "12. Alpine\n" + Fore.LIGHTWHITE_EX + "Select:"
print(osmenu)
