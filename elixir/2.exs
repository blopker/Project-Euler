require Integer

defmodule Fib do
	def fib(n) do fib(1, 1, n) end
	defp fib(a, _, 0) do a end
	defp fib(a, b, n) do fib(b, a + b, n-1) end
end

ans = 1..32 |> Stream.map(&Fib.fib/1) |> Stream.filter(&Integer.is_even/1) |> Enum.sum

IO.puts ans
