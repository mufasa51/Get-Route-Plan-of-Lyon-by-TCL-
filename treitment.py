import pandas as pd
import numpy

def del_negative(Matrix_1):
    list=[]
    for m in range(1,147):
        if type(Matrix_1[m,1])==int and Matrix[m,1] < 0 :
            list.append(m)
    Matrix_1 = numpy.delete(Matrix_1,list,axis=0)
    list=[]
    for n in range(1,147):
        if type(Matrix_1[1,n])== int and Matrix[1,n] < 0:
            list.append(n)
    Matrix_2 = numpy.delete(Matrix_1,list,axis=1)
    return Matrix_2

def del_repeat(Matrix_2):
    Num= len(Matrix_2[1, ])
    list_repeat_column = []
    list_repeat_row = []
    for n in range(2,Num-1):
        if Matrix_2[1,n] == Matrix_2[1,n+1]:
            list_repeat_column.append(n)
            list_repeat_row.append(n-1)
    Matrix_3 = numpy.delete(Matrix_2,list_repeat_column,axis=1)
    Matrix_3 = numpy.delete(Matrix_3,list_repeat_row,axis=0)
    return Matrix_3

if __name__ == '__main__':
    Date_original=pd.read_excel('traitment.xlsx','Feuil1')
    Matrix = Date_original.as_matrix()
    Matrix_1 = Matrix
    Matrix_2 = del_negative(Matrix_1)
    Matrix_3 = del_repeat(Matrix_2)
    #Matrix[行，列]
    Result = pd.DataFrame(Matrix_3)
    print(type(Result))
    Result.to_excel('traitment2.xlsx')


