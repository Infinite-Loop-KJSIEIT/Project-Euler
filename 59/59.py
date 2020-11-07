f=open('p059_cipher.txt','r')
s=f.readline()
CIPHERTEXT=list(map(int,s.split(',')))
def compute():
	bestkey = max(((x, y, z)
		for x in range(97, 123)  # ASCII lowercase 'a' to 'z'
		for y in range(97, 123)
		for z in range(97, 123)),
		key=lambda key: get_score(decrypt(CIPHERTEXT, key)))
	ans = sum(decrypt(CIPHERTEXT, bestkey))
	return str(ans)


# Heuristical function that returns a penalty score, where lower is better.
def get_score(plaintext):
	result = 0
	for c in plaintext:
		if 65 <= c <= 90:  # ASCII uppercase 'A' to 'Z', good
			result += 1
		elif 97 <= c <= 122:  # ASCII lowercase 'a' to 'z', excellent
			result += 2
		elif c < 0x20 or c == 0x7F:  # ASCII control characters, very bad
			result -= 10
	return result


def decrypt(ciphertext, key):
	return [(c ^ key[i % len(key)]) for (i, c) in enumerate(ciphertext)]

if __name__ == "__main__":
	print(compute())
	

