def fib(N: int) -> int:
  if N <= 1:
      return N
  else:
      return fib(N-1) + fib(N-2)

print(fib(4))