function within = isWithinTolerance(num1,num2,tolerance)
  if abs(num1 - num2) < tolerance
    within = true
  else
    within = false
  endif
endfunction
