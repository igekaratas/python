#
# Name: Mehmet Karatas
# SSID: 1640957
# Assignment #: 6
# Submission Date: 12/9/18 
# Description of program:
# This program draws a pie chart for countries 
# which are exceeded the UN’s threshold pm2 values.
#


import tkinter
import uuid


class  Top5Data:
  def  __init__(self):
    self.__population_percentage = {"China":36.17 ,"India":33.62, "Pakistan":5.37 ,"Nigeria":5.00 , "Bangladesh": 4.12}
    self.__pm25 = {"China":52.05 ,"India":58.54 , "Pakistan":88.00 , "Nigeria":36.42 ,"Bangladesh":78.00}
    self.__countries  =["China","India","Pakistan","Nigeria","Bangladesh"]

  def get_percent_population(self):
    return  self.__population_percentage

  def get_pm25(self):
    return  self.__pm25

  def get_countries(self):
    return  self.__countries;

class ChartTop5:
  def __init__(self):
    self.__CANVAS_WIDTH = 320   # Canvas  width
    self.__CANVAS_HEIGHT = 240 # Canvas  height
    self.__top5 = Top5Data()
    self.__pop_percentage = self.__top5.get_percent_population()
    self.__pm25 = self.__top5.get_percent_population()
    self.__country_list = self.__top5.get_countries()
    # I added these two lines to draw the pie for others.
    self.__second_pie_start = 303
    self.__second_pie_width = 57


    # Create  the  main  window.
    self.main_window = None
    self.canvas = None

  def draw_piechart(self):
    self.main_window = tkinter.Tk()  # Create  the  Canvas  widget.
    self.canvas = tkinter.Canvas(self.main_window ,
                                 width=self.__CANVAS_WIDTH ,
                                 height=self.__CANVAS_HEIGHT)


    self.canvas.create_arc(10,10,220,220, start=self.__second_pie_start, extent=self.__second_pie_width, fill='black')
    
    # This code prints the countries and their values on the canvas.
    i = 0
    for k,v in self.__pop_percentage.items():
      self.canvas.create_text(270,(10 + i), text="{:<9} {:<2}".format(k,v))
      i += 12

    # Some text for other countries.
    otherPop = float(15.70)
    self.canvas.create_text(258, 70, text=f"Others: {otherPop}")

    arc_start = 0
    # I added this code to generate the random colors for the pie chart.
    # So for each compile the chart will be in different colors.
    for v in self.__pop_percentage.values():
      def my_random_string(string_length=10):
      # Returns a random string of length string_length.
        random = str(uuid.uuid4()) # Convert UUID format to a Python string.
        random = random.upper() # Make all characters uppercase.
        random = random.replace("-","") # Remove the UUID '-'.
        return random[0:string_length] # Return the random string.
      # '#' is for the program read as a color code.
      rand_color_codes ="#" + my_random_string(6)

      arc_width = int(v*360/100)
      # After generating 6 digit letters and numbers in here
      # I use them as a color codes.
      self.canvas.create_arc(10, 10, 220, 220, start=arc_start, extent=arc_width, fill=rand_color_codes)
      arc_start += arc_width
          
    self.canvas.pack()
    tkinter.mainloop()

# Create  an  instance  of the  ChartTop5  class.
ui = ChartTop5()
ui.draw_piechart()


# 36*360/100
# 
# 




