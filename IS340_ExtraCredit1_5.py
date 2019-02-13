#Ch 5. Functions Problem 5
#
def main():
	reqs = False
	match = False
	pw1 = ""
	pw2 = ""
	while reqs == False:
		pw1 = input("Enter your password:")
		reqs = isValidPassword(pw1)
	while match == False:
		pw2 = input("Enter your password:")
		if pw1 == pw2:
			match = True
		else:
			match = False
			
def isValidPassword(password):
	pw = password
	if len(pw) >= 8:
		if any(ch.isupper() for ch in pw) and any(ch.islower() for ch in pw):
			if any(ch.isdigit() for ch in pw):
					return True
			else:
				print("must have at least one digit")
				return False
		else:
			print("must have at least one uppercase and one lowercase")
			return False
	else:
		print("must be at least 8 characters long")
		return False
main()
