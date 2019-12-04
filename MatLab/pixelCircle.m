function newPic = pixelCircle(centerX,centerY,radius,pic,layer,newValue,thickness)
  % Draws a circle on pic, returns new pic
  % x, y are center of circle on pic
  % radius of circle on pic
  % pic is 3D RGB matrix of uint8 
  % layer 1, 2, or 3 for RGB
  % newValue is RGB color value that will be written in circle pixels
  % thickness is the line thickness
  newPic = pic;
  for y = 1:row(newPic)
    for x = 1:col(newPic)
      if isWithinTolerance((x - centerX).^2 + (y - centerY).^2, radius, thickness/4)
        newPic(x, y, layer) = newValue;
      endif
    endfor
  endfor
endfunction