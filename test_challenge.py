from code_challenge import fib

def test_fibonnaci():
	a1 = fib(1)
	a2 = fib(2)
	a3 = fib(3)
	assert a1 is 1
	assert a2 is 1
	assert a3 is 2

	