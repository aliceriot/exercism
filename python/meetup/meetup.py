from datetime import date

def meetup_day(year, month, weekday, desc):
    if (desc == '1st'):
        try_dates = range(1,8)
    elif (desc == '2nd'):
        try_dates = range(8,15)
    elif (desc == 'teenth'):
        try_dates = range(13, 20)
    elif (desc == '3rd'):
        try_dates = range(15, 22)
    elif (desc == '4th'):
        try_dates = range(22,29)
    else:
        try_dates = range(29,32)

    for i in try_dates:
        trialdate = date(year, month, i)
        if trialdate.strftime("%A") == weekday:
            return trialdate


