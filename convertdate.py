#Working with Adam Staveski and Leah Nakaima

from datetime import datetime

#Set a variable birthday = "1-May-12".
birthday = "1-May-12"

#Parse the date using datetime.datetime.strptime.
date_format = "%d-%B-%y"

parsed_date = datetime.strptime(birthday, date_format)


#Use strftime to output a date that looks like "5/1/2012".
date_str = parsed_date.strftime("%-m/%-d/%Y")

print(date_str)

