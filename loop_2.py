# Loop program - Batch retry logic
retry_count = 0

while retry_count < 3:
    status = input("Enter status (COMPLETED/FAILED): ")
    
    if status == "COMPLETED":
        print("Success! Job completed!")
        break
    elif status == "FAILED":
        retry_count += 1
        if retry_count < 3:
            print(f"Retry {retry_count} of 3...")
        
else:
    # This runs ONLY when while condition becomes False
    # (not when break is used)
    print("Job failed after 3 retries - Escalate to L2!")

print("Thank you!!!")