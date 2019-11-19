function result = sumOddInts(start,finish)
  sum = 0
  for num = start:finish
    if mod(num, 2) == 1
      sum = sum + num
    endif
  endfor
  result = sum
endfunction