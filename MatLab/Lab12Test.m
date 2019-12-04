m1 = ones(40,60,3);
pic = uint8(m1);
pic(1:40,30:60,1) = 255;
imshow(pic)