#Author: Sheneille Gayle
#Date Created: April 26, 2022 
#Course: ITT103
#Purpose: To calculate and print the commission received by a sales person.

#Importing the Wx Python package to implement GUI
import wx

#creating a class for my main frame
class MainFrame(wx.Frame):
    #Creating an object for the class and initializing its attributes
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        #Assigning the screen size of the device to a varible to be used later
        screenSize = wx.DisplaySize()

        #Defining the frame/window object for the application and setting its size to the size of the device screen
        wx.Frame.__init__(self, size=screenSize, *args, **kwds)

        #Setting the background colour for the window
        self.SetBackgroundColour(('SKY BLUE'))

        #Giving the window a title
        self.SetTitle("JamEx Limited Sales Commission Calculator ")

        #Defining a custom font to be used in the window and assigning it to a variable
        font = wx.Font(18, wx.ROMAN, wx.BOLD, wx.NORMAL) 

        #Creating a panel within the window to hold all the widgets
        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        #Setting the font of the panel and its contents to the font defined earlier
        self.panel_1.SetFont(font)

        #Creating sizers to place the widgets in to lay them out automatically
        verticalBox = wx.BoxSizer(wx.VERTICAL)        
        horizontalBox = wx.BoxSizer(wx.HORIZONTAL)

        #Creating the main label for the window, setting it in focus and adding it to the main vertical sizer
        self.mainLabel = wx.StaticText(self.panel_1, label="Welcome to JamEx Limited\'s sales commission calculator.\n \n \n Enter your information into the boxes below and press calculate when you are finished.\n \n \n (Please do not leave any field empty)\n \n \n")
        self.mainLabel.SetFocus()
        verticalBox.Add(self.mainLabel, 0, wx.ALL|wx.CENTER, 5)

        #Creating the label and the edit box for the first user input and adding them to the main vertical sizer
        self.label_1 = wx.StaticText(self.panel_1, id = -1, label = "Please enter the sales person number(This should be exactly 5 characters):")
        self.editBox1 = wx.TextCtrl(self.panel_1)
        verticalBox.Add(self.label_1, 0, wx.ALL , 5)
        verticalBox.Add(self.editBox1, 0, wx.ALL , 5)

        #Creating the label and the edit box for the second user input and adding them to the main vertical sizer
        self.label_2 = wx.StaticText(self.panel_1, id = -1, label = "Please enter the sales amount(This must be a number and cannot include any symbols except for a decimal point):")
        self.editBox2 = wx.TextCtrl(self.panel_1)
        verticalBox.Add(self.label_2, 0, wx.ALL , 5)
        verticalBox.Add(self.editBox2, 0, wx.ALL , 5)

        #Creating the label and the edit box for the third user input and adding them to the main vertical sizer
        self.label_3 = wx.StaticText(self.panel_1, id = -1, label = "Please enter either 1, 2 or 3 to indicate the class in which the sales person belongs:")
        self.editBox3 = wx.TextCtrl(self.panel_1)
        verticalBox.Add(self.label_3, 0, wx.ALL , 5)
        verticalBox.Add(self.editBox3, 0, wx.ALL , 5)

        #Adding the horizontal box that will layout the buttons to the main vertical box
        verticalBox.Add(horizontalBox, 0, wx.ALL , 5)

        #Creating a button to perform a calculation based on the user's input
        self.calculateButton = wx.Button(self.panel_1, -1, "&Calculate")
        self.calculateButton.SetToolTip("Calculate the sales commission!")
        #Binding an event to the button. When it is clicked the defined function will be carried out
        self.Bind(wx.EVT_BUTTON, self.OnCalculate, self.calculateButton)
        #Setting the colour of the text on the button
        self.calculateButton.SetForegroundColour(('WHITE'))
        #Setting the background colour of the button
        self.calculateButton.SetBackgroundColour(('DARK GREY'))
        #Adding the button to the horizontal box
        horizontalBox.Add(self.calculateButton, 0, wx.ALL , 1)

        #Creating a button that the user can use to exit the program
        self.exitButton = wx.Button(self.panel_1, -1, "&Exit")
        self.exitButton.SetToolTip("Exit the program")
        #Binding an event to the button. When it is clicked the defined function will be carried out
        self.Bind(wx.EVT_BUTTON, self.OnExit, self.exitButton)
        #Setting the colour of the text of the button
        self.exitButton.SetForegroundColour(('WHITE'))
        #Setting the background colour of the button
        self.exitButton.SetBackgroundColour(('DARK GREY'))
        #Adding the button to the horizontal box
        horizontalBox.Add(self.exitButton, 0, wx.ALL , 1)

        #Assigning the vertical sizer to the panel as the main sizer
        self.panel_1.SetSizerAndFit(verticalBox)
        self.Layout()
        
    #Creating a function to validate the user input when the calculate button is pressed
    def OnValidation(self):
        #Creating a tupple to hold the acceptable values for sales person class
        class_list = ('1', '2', '3')

        #Collecting the user input from the edit boxes and assigning them to variables
        sales_person_num = str(self.editBox1.GetValue())
        sales_amount = str(self.editBox2.GetValue())
        sales_class = str(self.editBox3.GetValue())
        
        #Using if statements to validate the user input for each field
        #Validation check to ensure that the user enters a 5 character input for the sales person number field
        if len(sales_person_num) != 5:
            #Display an error message to the user prompting them to enter a valid input if the input was invalid
            wx.MessageBox('Your input is invalid!\nPlease enter a valid sales person number with 5 characters', "JamEx Limited Sales Commission Calculator ",
            wx.OK | wx.ICON_INFORMATION)

            #Clearing the contents of the specified edit box and setting it in focus
            self.editBox1.ChangeValue("")
            self.editBox1.SetFocus()
            #Returning the value 0 for validation if the user input was invalid
            return 0
        
        #Validation check to ensure that the user enters either 1, 2 or 3 for the sales class
        elif sales_class not in class_list:
            #Display an error message prompting the user to enter one of the values specified if the input is invalid
            wx.MessageBox('That class is invalid!\nPlease enter 1, 2 or 3 to choose a sales class', "JamEx Limited Sales Commission Calculator ",
            wx.OK | wx.ICON_INFORMATION)

            #Clearing the content of the specified edit box and setting it in focus
            self.editBox3.ChangeValue("")
            self.editBox3.SetFocus()
            #Returning a value of 0 for the validation if the input was invalid
            return 0

        #Validation to ensure that the user enters a real number
        #If the conversion of the user input to float fails, an error message is displayed
        try:
            #Converting the string input to float
            #Continue with program if conversion is successful
            sales_amount = float(sales_amount)
        except ValueError:
            wx.MessageBox('Your input is invalid!\nPlease enter a valid number for the sales amount', "JamEx Limited Sales Commission Calculator ",
            wx.OK | wx.ICON_INFORMATION)

            #Clearing the content of the specified edit box and setting it in focus
            self.editBox2.ChangeValue("")
            self.editBox2.SetFocus()
            #Returning a value of 0 for the validation if the input was invalid
            return 0

    #Creating a function to be called when the calculate button is pressed
    def OnCalculate(self, event):
        #No calculation is done if the validation fails and returns to the main screen of the program
        if self.OnValidation() == 0:
            return
        else:
            #Collecting the input of the user from the edit boxes for calculation
            sales_person_num = str(self.editBox1.GetValue())
            sales_amount = float(self.editBox2.GetValue())
            sales_class = str(self.editBox3.GetValue())
        
            #Determining the commission rate and calculating the sales commission based on the sales amount and class
            if sales_class == '1':
                if sales_amount <= 1000:
                    com_rate = 0.06

                elif sales_amount >1000 and sales_amount <2000:
                    com_rate = 0.07
                    
                elif sales_amount >= 2000:
                    com_rate = 0.10
                    
            elif sales_class == '2':
                if sales_amount < 1000:
                    com_rate = 0.04
                elif sales_amount >= 1000:
                    com_rate = 0.06
                    
            elif sales_class == '3':
                com_rate = 0.045

        #Formula to calculate the commission
        commission = sales_amount * com_rate
        #Rounding the result to 2 decimal places
        commission = round(commission, 2)

        #Displaying the results of the calculation and prompting the user to either do another calculation or exit the program
        wx.MessageBox(f"The results for the sales person of number {sales_person_num}, and sales class {sales_class} is: ${commission}\n You can calculate the commission for another sales person or just press the exit button to exit the program", "JamEx Limited Sales Commission Calculator ",
        wx.OK | wx.ICON_INFORMATION)

        #Clearing the content of all the edit boxes
        self.editBox1.ChangeValue("")
        self.editBox2.ChangeValue("")
        self.editBox3.ChangeValue("")
        
    #Creating a function to be carried out when the exit button is pressed
    def OnExit(self, event):
        #Using the close method to close the window
        self.Close()

#Creating a class for the application object
class MyApp(wx.App):
    def OnInit(self):
        #Creating a wx python frame object based on the mainframe class and assigning it to the app
        self.frame = MainFrame(None, wx.ID_ANY, "")
        #Setting the main frame as the main top level window for the app
        self.SetTopWindow(self.frame)
        #Calling the show method on the frame to display it on the screen
        self.frame.Show()
        return True

#Running the app
if __name__ == '__main__':
    app = MyApp(0)
    #Executing the main GUI event loop
    app.MainLoop()
