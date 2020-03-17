import pyperclip
import webbrowser

dayType = input('Good morning, Josh! \nIs today a Schoolday, Workday, or Weekend?').lower()

workdayTasks = {
    'Prosser': '7:55am-10:35am',
    'Chick-Fil-A': '12:00pm-8:00pm'
    }
schooldayTasks = {
    'Prosser': '7:55am-10:35am',
    'Psychology 101': '1:00pm-2:15pm',
    'English 111': '2:30pm-3:45pm'
    }
weekendTasks = {}
adding = True
while adding:
    print('Your current tasks include: \n')

    if dayType == 'workday':
        for task, time in workdayTasks.items():
            print(task, time)
    elif dayType == 'schoolday':
        for task, time in schooldayTasks.items():
            print(task, time)
    elif dayType == 'weekend':
        for task, time in weekendTasks.items():
            print(task, time)

    cont = input('\nAre there any other tasks you would like to add?').lower()
        
    if cont == 'yes' or cont == 'y':
        newTask = input('Which task would you like to add?')
        newTime = input('What time period will ' + newTask + ' occupy?')

        if dayType == 'workday':
            workdayTasks[newTask] = newTime
        elif dayType == 'schoolday':
            schooldayTasks[newTask] = newTime
        elif dayType == 'weekend':
            weekendTasks[newTask] = newTime


    elif cont == 'no' or cont == 'n':
        adding = False

        copy = input('Do you want to copy your schedule to your clipboard?').lower()
        if copy == 'yes' or copy == 'y':
            if dayType == 'workday':
                clipboard = str(workdayTasks)
            elif dayType == 'schoolday':
                clipboard = str(schooldayTasks)
            elif dayType == 'weekend':
                clipboard = str(weekdayTasks)

            censor = '{\'}'
            for char in censor:
                clipboard = clipboard.replace(char, '')
                clipboard = clipboard.replace(',', '\r\n')
                pyperclip.copy(clipboard)

        keep = input('Would you like to open Google Keep to Export your schedule?').lower()
        if keep == 'yes' or keep == 'y':
            print('Done. Have a nice day!')
            webbrowser.open('https://keep.google.com/')
            
        elif keep == 'no' or keep == 'n':
            print('Have a nice day!')
            
        else:
            print('Please respond with \'Yes\' or \'No.\'')
