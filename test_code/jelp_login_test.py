from getpass import getpass

passphrase = "jasper"

attempts = int(0)
max_tries = int(3)

while attempts <= max_tries:
	
	attempts += 1
	left = max_tries-attempts

	login = getpass("Please enter the passphrase (attempt %d of %d): " % (attempts, max_tries))

	if login == passphrase:
		print("Correct! Please continue.")
		break
	elif attempts == 3:
		print("Too many attempts - locked out for 15 minutes.")
		quit()
	else:
		print("Incorrect - %r attempts left now." % left)
