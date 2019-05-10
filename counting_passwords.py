import argparse

def parsarg():
	parser = argparse.ArgumentParser(description='Утилита для подсчета повторяющихся паролей')
	parser.add_argument('ifile', type=str, help='Путь до файла с базой')
	parser.add_argument('ofile', type=str, help='Путь до выходного файла')
	parser.add_argument('--separator', type=str, default=';', help='Разделитель логина и пароля')
	return parser.parse_args()

if __name__ == "__main__":
	complites = []
	args = parsarg()

	with open(args.ifile, 'r') as accountsFile:
	    accounts = accountsFile.read().split('\n')

	# Вытаскиваем пароли из базы
	passwords = [account.split(args.separator)[1] for account in accounts]

	# Считаем их колличество и добавляем в список уже без повторов
	for password in passwords:
	    finishedLine = '{0} - {1}\n'.format(password, passwords.count(password))
	    if finishedLine not in complites:
	        complites.append(finishedLine)

	with open(args.ofile, 'w') as finishedFile:
	    for complite in complites:
	        finishedFile.write(complite)
