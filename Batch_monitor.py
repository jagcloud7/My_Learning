# Good for: Real monitoring tool

def check_job_status(job_name, status, sla_minutes, actual_minutes):
    print(f"===== JOB: {job_name} =====")
    
    if status == "COMPLETED" and actual_minutes <= sla_minutes:
        print(f"Status: SUCCESS")
        print(f"Completed within SLA: {actual_minutes} mins")
    elif status == "COMPLETED" and actual_minutes > sla_minutes:
        print(f"Status: SLA BREACH!")
        print(f"Expected: {sla_minutes} mins | Actual: {actual_minutes} mins")
    elif status == "ABENDED":
        print(f"Status: ABENDED!")
        print(f"Action: Notify on-call team immediately!")
    elif status == "RUNNING" and actual_minutes > sla_minutes:
        print(f"Status: LATE RUNNING!")
        print(f"SLA: {sla_minutes} mins | Running: {actual_minutes} mins")
    else:
        print(f"Status: RUNNING - Within SLA")
    
    print("=" * 30)

# Get input FROM USER
job_name       = input("Enter job name: ")
status         = input("Enter status (COMPLETED/ABENDED/RUNNING): ")
sla_minutes    = int(input("Enter SLA in minutes: "))
actual_minutes = int(input("Enter actual run time in minutes: "))

# Pass user input TO function
check_job_status(job_name, status, sla_minutes, actual_minutes)