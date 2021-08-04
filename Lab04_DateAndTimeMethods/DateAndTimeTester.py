class DateAndTimeTester():

    def run(self):
        while (True):
            usr_inp = (input("Enter a date and time (MM/DD hh:mm) and I will determine if it is valid\n")).strip()
            
            print("User entered: ", usr_inp)

            if self.isValid(usr_inp):
                print("The date and time is valid!")
            else:
                print("The date and time is not valid!")

            leave_cond = input("Would you like to exit? Type \"quit\" to exit or press [ENTER] to continue\n")

            if leave_cond is None or len(leave_cond) == 0:
                continue
            elif leave_cond.lower() == "quit":
                break
            else:
                print("\"" + leave_cond + "\"" + " was not a valid input, EXITING")
                break


    def isValid(self, usr_inp: str) -> bool:
        date_parts = usr_inp.split()
        return (self.isValidDate(date_parts[0]) and self.isValidTime(date_parts[1]))
        

    def isValidDate(self, usr_date: str) -> bool:
        ret_values = self.getDateParts(usr_date) 
        ret_month = int(ret_values[0])
        ret_day = int(ret_values[1])

        if (ret_month == 1 or
            ret_month == 3 or
            ret_month == 5 or
			ret_month == 7 or
			ret_month == 8 or
			ret_month == 10 or
			ret_month == 12):
            if ret_day > 31 or	ret_day < 1:
                return False
                
        elif ret_month == 2:
            if ret_day > 28 or ret_day < 1:
                return False
                
        elif (ret_month == 4 or
              ret_month == 6 or
              ret_month == 9 or
              ret_month ==11):
            if ret_day > 30 or ret_day < 1:
                return False
                
        elif ret_month < 1 or ret_month > 12:
            return False
            
        return True

    def isValidTime(self, usr_time: str) -> bool:
        ret_values = self.getTimeParts(usr_time)
        ret_hour = int(ret_values[0])
        ret_min = int(ret_values[1])

        if ret_hour > 12 or ret_hour < 1:
            return False
        if ret_min > 59 or ret_min < 0:
            return False
        return True

    def getDateParts(self, usr_date: str):
        return usr_date.split('/')

    def getTimeParts(self, usr_time: str):
        return usr_time.split(':')