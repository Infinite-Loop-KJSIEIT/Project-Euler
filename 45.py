def compute():
    i = 286
    j = 166
    k = 144
    while True:
        t= i* (i + 1) // 2
        p = j * (j * 3 - 1) // 2
        h = k * (k * 2 - 1)
        m = min(t, p, h)
        if m == max(t, p, h):
            return str(t)
        if m == t: i += 1
        if m == p: j += 1
        if m == h : k += 1


if __name__ == "__main__":
	print(compute())
