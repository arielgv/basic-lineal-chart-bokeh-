#This codes requires to install bokeh to work.
#once you got it installed, you got to call these methods:
from bokeh.plotting import output_file,figure,show

#And then you can start making the graphic:
if __name__=="__main__":
    #the output html file
    output_file('graphic2.html')
    #how many data will be entered
    datanumber= int(input("How many "))
    TheGraphic=figure()
    x_value=[]
    y_value=[]
    for i in range(datanumber):
        #each value is entered by the user using the y_value variable
        print('Enter the value number ',i,': ')
        yvalue = int(input(''))
        x_value.append(i)
        y_value.append(yvalue)
    TheGraphic.line(x_value,y_value)


    show(TheGraphic)