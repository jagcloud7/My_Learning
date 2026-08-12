# Program to find the failure rate
print("*****BATCH SUMMARY*****")

# Use a single '=' for assignment and convert inputs to integers
total_jobs = int(input('total_jobs > '))
total_completion = int(input('total_completion > '))
total_abend = int(input('total_abend > '))

# Perform the calculation using the saved variables
failure_rate = (total_abend / total_jobs) * 100

# Print the final calculated result
print(f"Failure_rate: {failure_rate}%")