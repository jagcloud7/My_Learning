#List of 5 batch jobs

Jobs = ["PAYROLL", "DAILY-REPORT", "DATA-EXTRACT", "BACKUP", "MONTH-END"]

sequence_number = 1

for job_name in Jobs:
    print(f"Job {sequence_number}: {job_name}")
    sequence_number += 1