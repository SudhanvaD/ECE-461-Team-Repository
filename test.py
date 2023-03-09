try:
    with open('out.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found.")
    exit()
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    exit()

# Split the data into lines
lines = data.split("\n")

#if len(lines) != 10:
#    print("File format is incorrect.")
#    exit()

# Assign values to variables
try:
    url = lines[0]
    number_of_events = int(lines[1])
    number_of_starred = int(lines[2])
    number_of_subscribers = int(lines[3])
    number_of_commits = int(lines[4])
    number_of_open_issues = int(lines[5])
    number_of_closed_issues = int(lines[6])
    license = lines[7]
    community_metric = float(lines[8])
    pull_requests = int(lines[9])
except ValueError:
    print("File format is incorrect. Some values are not available")
    exit()
except Exception as e:
    print(f"An error occurred while assigning values to variables: {e}")
    exit()

cases_passed = 0
for i in range(len(lines)):
    try:
        assert lines[i] != '0'
        cases_passed += 1
    except:
        pass

if len(lines) != cases_passed:
    print("File format is incorrect. Not all lines are correct")
    exit()

coverage = (cases_passed / len(lines)) * 100
print(f"Total: {len(lines)}")
print(f"Passed: {cases_passed}")
print(f"Coverage: {coverage:.2f}%")
print(f"{cases_passed}/{len(lines)} passed")
