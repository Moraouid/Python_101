import sys

args = sys.argv

def get_input():
	if len(sys.argv) == 1:
		print("What is the text to count?")
		return input()
	if len(sys.argv) > 2:
		print ("AssertionError: more than one argument is provided")
		return None
	return sys.argv[1]

def main():
	txt = get_input()
	if txt is None:
		exit(0)
	l = len(txt)
	i = 0
	upper = 0
	lower = 0
	pun = 0
	dig = 0
	esp = 0
	while i < l:
		if txt[i].isupper():
			upper += 1
		elif txt[i].islower():
			lower += 1
		elif txt[i].isdigit():
			dig += 1
		elif txt[i] == " ":
			esp += 1
		else:
			pun += 1
		i += 1
	print ("The text contains", i, "characters:")
	print(upper, "upper letters")
	print(lower, "lower letters")
	print(pun, "punctuation marks")
	print(esp, "spaces")
	print(dig, "digits")


if __name__ == "__main__":
	main()