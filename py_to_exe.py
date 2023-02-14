# Developed by: Fabrício de Lima | string.

# Dependências: "pyinstaller"
# pip install pyinstaller

# Recomendo que execute o programa atráves do Terminal (cmd), não através de IDE.

from os import getcwd, system, popen, path
from time import sleep

#

checkPyinstaller = system("pyinstaller --version")

if (checkPyinstaller == 1):
	system("pip install pyinstaller")
	system("pip install pyinstaller --upgrade")

#

logo = """
 ██████╗ ██╗   ██╗    ████████╗ ██████╗        ███████╗██╗  ██╗███████╗
 ██╔══██╗╚██╗ ██╔╝    ╚══██╔══╝██╔═══██╗       ██╔════╝╚██╗██╔╝██╔════╝
 ██████╔╝ ╚████╔╝        ██║   ██║   ██║       █████╗   ╚███╔╝ █████╗  
 ██╔═══╝   ╚██╔╝         ██║   ██║   ██║       ██╔══╝   ██╔██╗ ██╔══╝  
 ██║        ██║          ██║   ╚██████╔╝    ██╗███████╗██╔╝ ██╗███████╗
 ╚═╝        ╚═╝          ╚═╝    ╚═════╝     ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝"""
# [1m[33mA
colors = {"red":"[1m[31m", "yellow":"[1m[33m","green":"[1m[32m", "magenta":"[1m[35m", "cyan":"[1m[36m"}

def error():
	print(f"{colors['red']}\n Comando inválido ou desconhecido. \n")
	sleep(2)

def option(x, a, b):
	adds[x] = a
	options[x] = b

#

system("cls")
folderExtract = str(input(f"{colors['green']}{logo}{colors['cyan']}\n\n Arraste aqui a pasta onde será criado o arquivo executável e pressione a tecla enter:\n\n {colors['yellow']}-> "))
system("cls")
filePy = str(input(f"""{colors['green']}{logo}{colors['cyan']}\n\n Arraste aqui o arquivo ".py" que será convertido para ".exe" e pressione a tecla enter:\n\n {colors['yellow']}-> """))

folderExtract = folderExtract.replace('"', "")
command = ["pyinstaller "]
command_f = ""
includeFiles = []
includeFilesF = ""
options = {1:f"+", 2:"+", 3:"+", 4:"+", 5:"+"}
adds = {1:0, 2:0, 3:0, 4:0, 5:0}

while True:
	system("cls")

	for c in range(0, len(command)):
		command_f += command[c]

	try:
		user = int(input(f"""{colors['green']}{logo}\n\n {colors['cyan']}[1] {options[1]} Gerar apenas um arquivo executável\n [2] {options[2]} Acesso de Administrador\n [3] {options[3]} Inserir ícone\n [4] {options[4]} Sem terminal\n [5] {options[5]} Incluir arquivos \n\n [0] → Salvar e compilar\n\n {colors['yellow']}{command_f}{filePy}{includeFilesF}\n\n {colors['red']}-> """))
	except:
		user = 000;
	command_f = ""

	if (user == 1):
		if (adds[1] == 0):
			command.append("--onefile ");
			option(1, 1, "-")
		else:
			command.remove("--onefile ");
			option(1, 0, "+")

	elif (user == 2):
		if (adds[2] == 0):
			command.append("--uac-admin ");
			option(2, 1, "-")
		else:
			command.remove("--uac-admin ");
			option(2, 0, "+")

	elif (user == 3):
		if (adds[3] == 0):
			system("cls")
			fileIcon = str(input(f"""{colors['green']}{logo}{colors['cyan']}\n\n Arraste aqui o arquivo do ícone (.ico) e pressione a tecla enter:\n\n {colors['yellow']}-> """))
			command.append(f"""--icon="{fileIcon}" """);
			option(3, 1, "-")
		else:
			command.remove(f"""--icon="{fileIcon}" """);
			option(3, 0, "+")

	elif (user == 4):
		if (adds[4] == 0):
			command.append("--noconsole ");
			option(4, 1, "-")
		else:
			command.remove("--noconsole ");
			option(4, 0, "+")

	elif (user == 5):
		if (adds[5] == 0):
			system("cls")

			try:
				qntArq = int(input(f"""{colors['green']}{logo}{colors['cyan']}\n\n Insira a quantidade de arquivos que será incluídos e pressione a tecla enter:\n\n {colors['yellow']}-> """))
			except:
				error()
				qntArq = ""
				continue

			system("cls")
			print(f"{colors['green']}{logo}")

			for c in range(0, qntArq):
				user = str(input(f"{colors['yellow']}\n Arquivo ({c+1}) - {colors['cyan']}Arraste aqui o arquivo que será incluso e pressione a tecla enter:\n\n {colors['red']}-> """))
				includeFiles.append(user)

			includeFilesF = f"""\n\n Include Files: {includeFiles}"""
			option(5, 1, "-")
		else:
			includeFiles = []
			includeFilesF = ""
			option(5, 0, "+")

	elif (user == 0):
		if (len(command) == 1):
			command_f = f"pyinstaller "
		else:
			for c in range(0, len(command)):
				command_f += command[c]

		system("cls")
		print(f"{colors['green']}{logo}{colors['cyan']}\n\n Pasta onde será extraído: {folderExtract}\n\n Arquivo que será compilado: {filePy}\n\n{colors['red']} {command_f}{filePy} {includeFilesF}\n\n{colors['yellow']} Compilando para executável...\n\n {colors['magenta']}↓\n")
		system(f"cd {folderExtract} && {command_f}{filePy} {includeFilesF}")

		if (len(includeFiles) > 0):
			print("\n Copiando arquivos para pasta...\n")
			for c in range(0, len(includeFiles)):
				try:
					if ("--onefile" in command_f):
						popen(f'copy "{includeFiles[c]}" "{folderExtract}"\\dist')
					else:
						nameFolder = path.basename(filePy).replace(".py", "")
						popen(f'copy "{includeFiles[c]}" "{folderExtract}\\dist\\{nameFolder}"')
						
					print(includeFiles[c], "copiado com sucesso.")
				except Exception as e:
					print(e)

		input(f"\n {colors['magenta']}↑\n{colors['red']}\n Pressione a tecla enter para sair: ")
		quit();

	elif (user == 000):
		error()

	else:
		error()