function result = biggestNumber(alist)
  largest = alist(1);
  result = 1;
  for num = [1:length(alist)]
    if (alist(num)>largest)
      largest = alist(num);
      result = num
    endif
  endfor
endfunction