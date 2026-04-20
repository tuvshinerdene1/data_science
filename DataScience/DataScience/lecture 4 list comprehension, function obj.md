## List comprehension
Жагсаалтын бүх элемэнтэд үйлдэл гүйцэтгэж, шинэ жагсаалт үүсгэдэг

```
[*expression* for *elem* in *iterable* if *test*]
```

```
def f(L):
	Lnew = []
	for e in L:
		Lnew.append(a**2)
	return Lnew
	
	
Lnew = [e**2 for e in L]
Lnew = [e**2 for e in L if e%2 == 0]
[[e,e**2] for e in range(4) if e%2 != 0]  => [[1,1], [3,9]]
```

## Function default parameter
used when user didnt provide any argument

