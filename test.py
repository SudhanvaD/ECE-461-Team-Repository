# Read from file
file = "out.txt"
with open(file, 'r') as f:
    data = f.read()

# Split the data into lines
lines = data.split("\n")

# Assign values to variables
Url = lines[0]
Number_of_Events = (lines[1])
Number_of_Starred = (lines[2])
Number_of_Subscribers = (lines[3])
Number_of_Commits = (lines[4])
Number_of_Open_Issues = (lines[5])
Number_of_Closed_Issues = (lines[6])
License = lines[7]
Community_Metric = (lines[8])
Pull_Requests = (lines[9])


file_expected = "out_expected.txt"
with open(file_expected, 'r') as f:
    data_expected = f.read()

# Split the data into lines
lines_expected = data_expected.split("\n")

# Assign values to variables
Url_expected = lines[0]
Number_of_Events_expected = (lines[1])
Number_of_Starred_expected = (lines[2])
Number_of_Subscribers_expected = (lines[3])
Number_of_Commits_expected = (lines[4])
Number_of_Open_Issues_expected = (lines[5])
Number_of_Closed_Issues_expected = (lines[6])
License_expected = lines[7]
Community_Metric_expected = (lines[8])
Pull_Requests_expected = (lines[9])

casses_passed = 0
for i in range(len(lines)):
    assert lines[i] == lines_expected[i]
    casses_passed = casses_passed + 1
print(f"Total: {len(lines)}")
print(f"Passed: {casses_passed}")
print(f"{casses_passed}/{len(lines)} passed")
