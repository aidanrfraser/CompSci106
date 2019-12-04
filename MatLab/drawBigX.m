function newPic = drawBigX(pic, layer, newValue, thickness)
  % drawBigX draws diagonal lines from the top corners of a square picture
  % to the bottom corners.
  % Challenge: make it work for rectangular pics too, and only use one loop.
  newPic = (pic);
  newPic = ones(newPic, newPic, 3);
  newPic = uint8(newPic);
  [h w d] = size(newPic);
  height = 1;
  height2 = h;
  for row  = 1:h;
    newPic(row, height:height + thickness, layer) = newValue;
    height = height + 1;
    newPic(row, height2:height2 + thickness, layer) = newValue;
    height2 = height2 - 1;
  endfor
imshow(newPic);
endfunction