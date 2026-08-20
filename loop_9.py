#Program - kind of batch forecast

Jobs = ["PAYROLL", "DAILY-REPORT", "DATA-EXTRACT", "BACKUP", "MONTH-END", "ABENDED-JOB", "CICS", "FTPJOB"]
Schedule = [1,0,1,1,0,1,0,1]

Job_Schd = []

for Jobname, schd in zip(Jobs,Schedule):
    if schd == 1:
        print(f"{Jobname} is in today's schedule")
        Job_Schd.append(Jobname)
        continue
    elif schd == 0:
        print(f"{Jobname} is not in schedule today")

print(f'Total no of jobs that are in today schedule: {len(Job_Schd)}')
print("=======================================")
print("Scheduled Jobs List:", Job_Schd)
print("=======================================")