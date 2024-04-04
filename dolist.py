import datetime

#Current Assignments on my plate represented as a dictionary, where the key is the assignment and the value is the due date
assignments = {}

#Upcoming Exams represented as a dictionary, where the key is the exam and the value is the date
upcoming_exams = {"Algorithm Exam":"April 10th, Wednesday"}

#Current Projects that I am actively working on represented as a list
current_projects = ["LibreTunes", "Discord-Bot", "Improv"]

#Things I need to do to get smarter and better at my craft represented as a list
get_smarter = ["LeetCode", "AWS CCP Training"]

#Things I need to do represented as a list
what_to_do = [assignments, upcoming_exams, current_projects, get_smarter]

#All days
wake_up = "7:00am - Wake Up"
run = "7:10am - 8:00am - Run"
breakfast = "8:00am - 8:30am - Breakfast"
morning_hygiene = "8:30am - 9:00am - Brush Teeth, Shower"

#Monday, Thursday
awg_ccp_training = "9:00am - 9:30am - AWG CCP Training"
go_to_cogpsyc = "9:30am - 10:00am - Go to CogPsyC"
cogpysc = "!10:00am - 12:00am - CogPsyC"

#Monday
monday_work = "!12:00pm - 01:00pm - Work"
monday_lunch = "01:00pm - 02:00pm - Lunch"
monday_work2 = "!02:00pm - 04:00pm - Work"
monday_gym = "04:00pm - 05:30pm - Gym"

#Tuesday
tuesday_work_study = "!12:00pm - 02:00pm - Work Study"
tuesday_lunch = "02:00pm - 03:00pm - Lunch"
tuesday_work = "!03:00pm - 04:00pm - Work"
tuesday_gym = "04:00pm - 05:30pm - Gym"

#Wednesday
wednesday_work = "!9:00pm - 11:00pm - Work"
wednesday_work_study = "!12:00pm - 02:00pm - Work Study"
wednesday_lunch = "02:00pm - 03:00pm - Lunch"
wednesday_work = "!03:00pm - 05:00pm - Work"
wednesday_gym = "05:00pm - 06:30pm - Gym"

#Thursday
thursday_work = "!12:00pm - 01:00pm - Work"
thursday_lunch = "01:00pm - 02:00pm - Lunch"
thursday_work_study = "!02:00pm - 04:00pm - Work Study"
thursday_gym = "04:00pm - 05:30pm - Gym"

#Friday
friday_work = "!12:00pm - 01:00pm - Work"
friday_lunch = "01:00pm - 02:00pm - Lunch"
friday_work2 = "!02:00pm - 04:00pm - Work Study"
friday_gym = "04:00pm - 05:30pm - Gym"

#Tuesday, Friday
goto_psoft_algos = "9:00am - 9:20am - Go to Psoft/Algos"
psoft_algos = "!9:20am - 11:50pm - Psoft/Algos"

#Root to do list, where the key is the day and the value is a list of things to do during that day
todo_list = {
    "Monday": [wake_up, run, breakfast, morning_hygiene, awg_ccp_training, go_to_cogpsyc, cogpysc, monday_work, monday_lunch, monday_work2, monday_gym],
    "Tuesday": [wake_up, run, breakfast, morning_hygiene, goto_psoft_algos, psoft_algos, tuesday_work_study, tuesday_lunch, tuesday_work, tuesday_gym],
    "Wednesday": [wake_up, run, breakfast, morning_hygiene, wednesday_work, wednesday_work_study, wednesday_lunch, wednesday_work, wednesday_gym],
    "Thursday": [wake_up, run, breakfast, morning_hygiene, awg_ccp_training, go_to_cogpsyc, cogpysc, thursday_work, thursday_lunch, thursday_work_study, thursday_gym],
    "Friday": [wake_up, run, breakfast, morning_hygiene, goto_psoft_algos, psoft_algos, friday_work, friday_lunch, friday_work2, friday_gym],
    "Saturday": [],
    "Sunday": []
}
def get_todo_list():
    today = datetime.datetime.now().strftime("%A")
    return todo_list[today]

def get_what_to_do():
    return what_to_do   


