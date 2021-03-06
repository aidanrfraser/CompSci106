function newPic = drawRect(pic, startX, startY, endX, endY, layer, newValue)
  % DRAWRECT draws a filled rectangle of pixels in one rgb layer
  % start values are less than end values
  newPic = pic;
  newPic = ones(newPic, newPic, 3);
  newPic = uint8(newPic);
  newPic(startX:endX, startY:endY, layer) = newValue;
imshow(newPic);
endfunction