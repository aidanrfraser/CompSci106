function newPic = pixelCircle(centerX,centerY,radius,pic,layer,newValue,thickness)
  % pixelCircle(centerX,centerY,radius,pic,layer,newValue,thickness)
  % Draws a circle on pic, returns new pic
  % x, y are center of circle on pic
  % radius of circle on pic
  % pic is 3D RGB matrix of uint8 
  % layer 1,2, or 3 for RGB
  % newValue is RGB color value that will be written in circle pixels
  % thickness is the line thickness
  newPic = pic;
  [h w d] = size(newPic); %this is multiple assignment in Matlab