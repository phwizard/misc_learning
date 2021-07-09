import csv
# Write your mean_datasets function here

def mean_datasets(fileNames):
  fileCounter=0
  #dic={}
  
  # matrix = [[0 for x in 20] for y in 20] 
  matrixSrc = [[0]*20 for i in range(20)];
  
  for file in fileNames:
    rowCounter = 0;
    colCounter = 0;
    csvFile = csv.reader(open(file, 'rt'))
    for row in csvFile:
      for column in row:
        matrixSrc[rowCounter][colCounter] += float(column);
        #print("Value [" + str(rowCounter) + "," + str(colCounter) + "]: " + column);
        #print("Sum: " + str(matrixSrc[rowCounter][colCounter]));
        colCounter += 1;
      rowCounter += 1;
      maxCol = colCounter; 
      colCounter = 0;
        #dic(row,column)=dic(row,column)+column[0] 
        #print(row[0]);
        #print(column[0]);
    maxRow = rowCounter;
    fileCounter += 1;
    
  
  ## UNCOMMENT FOR DEBUG MODE
  #print("maxCol: " + str(maxCol));
  #print("maxRow: " + str(maxRow));
  #print("fileCounter: " + str(maxRow));

  
  matrixRes = [[0]*maxCol for i in range(maxRow)];
    
  meanArr = [];
    
  for i in range(len(matrixRes)):
          for j in range(len(matrixRes[i])):
            meanCalc = round(matrixSrc[i][j]/fileCounter,1);
            matrixRes[i][j]= meanCalc
            #meanArr[i][j]=meanCalc;
            #meanArr[i].append(meanCalc);
            #print(str(matrixRes[i][j]));
  
  return matrixRes;
  #return meanArr;
  
 


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

  # Run your function with the second example from the question:
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
