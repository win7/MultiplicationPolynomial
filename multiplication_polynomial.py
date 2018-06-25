"""
Multiplication of polynomials using FFT
Cormen edtion 2
"""
from numpy import *

def FormatPolynomial(a):
	# a is array of polinomy coefficient, example: [1, -5, 0, 2] (1 - 5x +0x^2 + 2x^3)
	r = ""
	for k in range(len(a)):
		r += "{:+0.2f}x^{:d} ".format(round(a[k], 2), (k))
	return r

def PrintMatrix(m):
	print("-" * 10 * len(m[0]))
	for i in m:
		for j in i:
			print "| " + str(j).ljust(7, " "),
		print "|"
	print("-" * 10 * len(m[0]))

def MatrixVandermodeR(n):
	mvr = []
	for i in range(0, n):
		aux = [1]
		for j in range(1 , n):
			aux.append(pow(i, j))
		mvr.append(aux)
	return array(mvr)

### FFT ALGORITMH
def MatrixVandermodeI(n):
	mvr = []
	mvr.append([1] * (n))
	for i in range(1, n):
		aux = [1]
		for j in range(1 , n):
			aux.append(EulerNumber(i * j, n))
		mvr.append(aux)
	return array(mvr)

def EulerNumber(k, n):
	u = (2 * pi * k) / n
	return round(cos(u), 2) + 1j * round(sin(u), 2)
	# return (cos(u)) + 1j * (sin(u))

def GetEvenIndex(a):
	a_even = []
	for k in range(0, len(a), 2):
		a_even.append(a[k])
	return a_even

def GetOddIndex(a):
	a_odd = []
	for k in range(1, len(a), 2):
		a_odd.append(a[k])
	return a_odd

def RecursiveFFT(a):
	# a is array of polinomy coefficient, example: [1, -5, 0, 2] (1 - 5x +0x^2 + 2x^3)
	n = len(a)
	if n == 1:
		return a
	Wn = EulerNumber(1, n)
	W = 1
	a_even = GetEvenIndex(a)
	a_odd = GetOddIndex(a)
	y_even = RecursiveFFT(a_even)
	y_odd = RecursiveFFT(a_odd)
	y = []
	for k in range(0, n / 2):
		t = W * y_odd[k]
		y.insert(k, y_even[k] + t)
		y.insert(k + (n / 2), y_even[k] - t)
		W = W * Wn
	return array(y)

def BitReverse(a):
	A = []
	n = len(a)
	for k in range(n):
		A.insert(int(bin(k)[-1:1:-1], 2), a[k])
	return A

def IterativeFFT(a):
	# a is array of polinomy coefficient, example: [1, -5, 0, 2] (1 - 5x +0x^2 + 2x^3)
	A = BitReverse(a)
	n = len(a)
	for s in range(1, int(log2(n)) + 1):
		m = pow(2, s)
		Wm = EulerNumber(1, m)
		for k in range(0, n, m):
			W = 1
			for j in range(0, m / 2):
				t = W * A[k + j + m / 2]
				u = A[k + j]
				A[k + j] = u + t
				A[k + j + m / 2] = u - t
				W = W * Wm
	return array(A)
	
import sys
if __name__ == "__main__":
	a = [1, 2, 0, 0]
	print(RecursiveFFT(a))
	print(IterativeFFT(a))
	print "Pass file name ..."