function newPic = drawBigX(pic, layer, newValue, thickness)
  % drawBigX draws diagonal lines from the top corners of a square picture
  % to the bottom corners.
  % Challenge: make it work for rectangular pics too, and only use one loop.
  newPic = pic;
  [h w d] = size(newPic); %this is multiple assignment in Matlab