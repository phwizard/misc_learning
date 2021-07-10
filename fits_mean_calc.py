import numpy as np
from astropy.io import fits
# Write your mean_datasets function here

def mean_fits(fileNames):
  fileCounter=0
  #dic={}
  
  matrixSrc = [[0]*200 for i in range(200)];
  
  # open files
  for file in fileNames:
    rowCounter = 0;
    colCounter = 0;
    fitsFile = fits.open(file)
    #fitsData = fitsFile[0].data
    #fitsFile.close()
    #fitsData = fitsFile[fileCounter].data
    fitsData = fitsFile[0].data
    
    # read source data
#    csvFile = csv.reader(open(file, 'rt', encoding='utf-16le'))
#    csvFile = csv.reader(open(file, 'rt', encoding="ISO8859"))
    for row in fitsData:
      for column in row:
        # update sum for each cell
        matrixSrc[rowCounter][colCounter] += float(column);
        ## UNCOMMENT FOR DEBUG MODE
        #print("Value [" + str(rowCounter) + "," + str(colCounter) + "]: " + str(column));
        #print("Sum: " + str(matrixSrc[rowCounter][colCounter]));
        colCounter += 1;
      rowCounter += 1;
      maxCol = colCounter; 
      colCounter = 0;
    maxRow = rowCounter;
    fileCounter += 1;
 
  ## UNCOMMENT FOR DEBUG MODE
  #print("maxCol: " + str(maxCol));
  #print("maxRow: " + str(maxRow));
  #print("fileCounter: " + str(maxRow));
  
  # create and fill the resulting 2D array with mean values
  matrixRes = [[0]*maxCol for i in range(maxRow)];
    
  for i in range(len(matrixRes)):
          for j in range(len(matrixRes[i])):
            #print(matrixSrc[i][j]);
            meanCalc = matrixSrc[i][j]/fileCounter;
            #meanCalc = round(matrixSrc[i][j]/fileCounter,1);
            matrixRes[i][j]= meanCalc
 
  meanArr = np.array(matrixRes);
  #print(meanArr);

  return meanArr; 


if __name__ == '__main__':
  
  # Test your function with examples from the question
  #data  = mean_fits(['image0.fits'])
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
 


## more elegant solution:

## from astropy.io import fits
## import numpy as np

## def mean_fits(files):
##  n = len(files)
##  if n > 0:
    
##    hdulist = fits.open(files[0])
##    data = hdulist[0].data
##    hdulist.close()
    
##    for i in range(1, n):
##      hdulist = fits.open(files[i])
##      data += hdulist[0].data
##      hdulist.close()
    
##    mean = data / n
##    return mean
