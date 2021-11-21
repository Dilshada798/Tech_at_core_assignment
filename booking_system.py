from datetime import datetime
print("0900 1700")
employe = int(input("Enter the number of employee: "))
array=[]
for i in range(employe):
    
    submission_time_of_employee=str(input("enter date(yyyy-mm-dd hh:mm:ss): "))
    employee_id=int(input("enter the id:"))
    print(submission_time_of_employee,"EMP0"+str(employee_id))
    meeting_start_time = str(input("enter date(yyyy-mm-dd hh:mm :"))
    meeting_duration=str(input("Enter the duration of the time (hh:mm): "))
    duration=datetime.strptime(meeting_duration,"%H:%M")
    my_date=datetime.strptime(meeting_start_time, "%Y-%m-%d %H:%M")
    final_time=(int("%s"%(my_date.hour))+int("%s"%(duration.hour)))
    final_min=(int("%s"%(my_date.minute))+int("%s"%(duration.minute)))
    if (final_time>=9 and final_time<=17) and (final_min>=00 and final_min<=59):
        array.append(meeting_start_time)
        print(array)
        if meeting_start_time in array:
            print("not overlap")
        else:
            print("overlap")
        
    else:
        print("out of office time")
    











