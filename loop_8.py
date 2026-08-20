#Scanning a list of jobs and stop it when it finds the ABEND_JOB

Jobs=["PAYROLL", "DAILY-REPORT", "DATA-EXTRACT", "BACKUP", "MONTH-END", "ABENDED-JOB", "CICS", "FTPJOB"]

last_ok_job = "None"

for jobname in Jobs:
    if jobname == "ABENDED-JOB":
        print("ALERT! Abended job found: ABENDED-JOB")
        print("Stopping scan! Fix this first!")
        break
    print(f"Job scanned & completed: {jobname} job" )
    last_ok_job = jobname
    
print(f"\nJob was ok till: {last_ok_job} job")