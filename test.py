file = "out.txt"
try:
    with open(file, 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found.")
except:
    print("An error occurred while reading the file.")

# Split the data into lines
lines = data.split("\n")

# Assign values to variables
url = lines[0]
number_of_events = (lines[1])
number_of_starred = (lines[2])
number_of_subscribers = (lines[3])
number_of_commits = (lines[4])
number_of_open_issues = (lines[5])
number_of_closed_issues =(lines[6])
license = lines[7]
community_metric = (lines[8])
pull_requests = (lines[9])

casses_passed = 0
for i in range(len(lines)):
    try:
        assert lines[i] != '0'
        casses_passed = casses_passed + 1
    except:
        pass

coverage = (casses_passed / len(lines)) * 100
print(f"Total: {len(lines)}")
print(f"Passed: {casses_passed}")
print(f"Coverage: {coverage:.2f}%")
print(f"{casses_passed}/{len(lines)} passed")
