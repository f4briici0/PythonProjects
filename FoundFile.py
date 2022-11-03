from os import walk, system
from colorama import Fore

system("cls")

#userfiles - ! - save

output = int(input(f"\n {Fore.GREEN}0 -{Fore.CYAN} Without show output folder and paths. {Fore.GREEN}(fast)\n {Fore.GREEN}1 -{Fore.CYAN} Show output folder and paths. {Fore.RED}(slow)\n\n {Fore.WHITE}->{Fore.YELLOW} "))
path = str(input(f"\n {Fore.CYAN}Enter a {Fore.RED}path{Fore.CYAN}:\n\n {Fore.WHITE}->{Fore.YELLOW} "));
file = str(input(f"\n {Fore.CYAN}Enter a {Fore.RED}file{Fore.CYAN}:\n\n {Fore.WHITE}->{Fore.YELLOW} "));

if (path == "userfiles"):
	path = r"C:\Users"

system("cls")
print(f"\n{Fore.WHITE} [===]\n\n {Fore.CYAN}{path}\n\n {Fore.YELLOW}Looking for: {Fore.CYAN}{file}")

found_files = []

if (output == 1):
	print()

if (file[0] == "!"):
	file = file[1:]
	for c in walk(path):
		if (file in c[2]):
			for i in range(0, len(c[2])):
				if (file in c[2][i]):
					found_files.append(c[0] + "\\" + c[2][i])
		if (output == 1): # try / except
			for i in range(0, len(c[2])):
				print(f" {Fore.YELLOW}{c[0]}{Fore.RED}\\{c[2][i]}")

else:
	for c in walk(path):
		for p in range(0, len(c[2])):
			if (file.lower() in c[2][p].lower()):
				found_files.append(c[0] + "\\" + c[2][p])

		if (output == 1): # try / except
			for i in range(0, len(c[2])):
				print(f" {Fore.YELLOW}{c[0]}{Fore.RED}\\{c[2][i]}")

print(f"\n {Fore.WHITE}[===]\n\n {Fore.CYAN}Found paths:{Fore.GREEN} ({len(found_files)})\n")

if (len(found_files) > 0):
	for c in found_files:
		print(" ", c)
else:
	print(f"{Fore.RED}  nothing")

save = str(input((f"\n {Fore.WHITE}->{Fore.YELLOW} ")))

if (save == "save"):
	with open("paths.txt", "w") as esc:
		for c in range(0, len(found_files)):
			if (c == len(found_files)):
				esc.write(found_files[c])
			else:
				esc.write(found_files[c] + "\n")
		esc.close();
