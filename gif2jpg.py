from PIL import Image
import glob

i=3936-65
for j in range(37,40):

  fnames=glob.glob("/home/alireza/Documents/cv-final-project/CroppedYale/yaleB"+str(j)+"/file-*.pgm")
  fnames.sort()
  print(len(fnames))

  i=i+65

  for fname in fnames:
    print(fname[0:-3])
    im=Image.open(fname)
    im.convert('RGB')
    im.save("/home/alireza/Documents/cv-final-project/positiveSamples/"+str(i)+".jpg")
    i+=1
