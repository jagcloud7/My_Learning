# Batch summary report

Jobs = ["PAYROLL", "DAILY-REPORT", "DATA-EXTRACT", "BACKUP", "MONTH-END", "DBA", "CICS", "FTPJOB"]
Duration = [45, 120, 30, 95, 60, 200, 15, 80]  #Time in minutes

within_sla = 0
sla_breach = 0

# zip() lets us pair each Jobname with its corresponding time
for name, time in zip(Jobs, Duration):
    print(f"{name} job completed in: {time} minutes")
    
    # Use 'time' (the individual integer) instead of 'Duration' (the list)
    if time <= 60:
        within_sla += 1
    else:
        sla_breach += 1

print("\nFinal batch summary")
print(f"Total jobs: {len(Jobs)}")
print(f"Within SLA: {within_sla}")
print(f"SLA Breach: {sla_breach}")