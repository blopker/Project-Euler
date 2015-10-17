check = fn n -> rem(n, 3) == 0 || rem(n, 5) == 0 end
ans = 1..999 |> Stream.filter(check) |> Enum.sum
IO.puts ans
