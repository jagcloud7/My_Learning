### Batch Monitor Window
print("Hello!!! Welcome to Batch monitoring window")
print("===========================================")

# 1. Track the counters
total_processed = 0
total_completed = 0
total_skipped = 0
abended = False  # Flag to check if a critical failure happened

# 2. Loop exactly 5 times for the 5 jobs
for job_num in range(1, 6):
    # Prompt for job name and take actual input
    job_name = input(f"Please enter the name for Job {job_num}: ")
    
    # Prompt for status and convert to uppercase to prevent casing errors
    status = input(f"Please enter the status for {job_name} (COMPLETED / ABENDED / SKIPPED): ").upper()
    
    # Increment total processed jobs
    total_processed += 1
    
    # 3. Check statuses using strings
    if status == "COMPLETED":
        print("Success!\n")
        total_completed += 1
        
    elif status == "SKIPPED":
        print("Skipping this job...\n")
        total_skipped += 1
        continue
        
    elif status == "ABENDED":
        print("Alert!!! Job got abended, STOP everything!\n")
        abended = True
        break
    else:
        print("Invalid status entered. Counting as processed but uncompleted.\n")

# 4. Print Batch Summary
print("\nBatch Summary")
print("-------------")
print(f"Total jobs processed: {total_processed}")
print(f"Total completed: {total_completed}")
print(f"Total skipped: {total_skipped}\n")

# 5. Final Status Check
if abended:
    print("BATCH INCOMPLETE - Escalate!")
else:
    print("ALL JOBS COMPLETED SUCCESSFULLY!")