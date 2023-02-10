package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func readFromFile(file string) string {
	data := ""

	f, err := os.Open(file)
	if err != nil {
		fmt.Println(err)
		return data
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		data += scanner.Text() + "\n"
	}

	return data
}

func main() {
	file := "out.txt"

	data := readFromFile(file)
	lines := strings.Split(data, "\n")

	var Number_of_Events int
	var Number_of_Starred int
	var Number_of_Subscribers int
	var Number_of_Commits int
	var Number_of_Open_Issues int
	var Number_of_Closed_Issues int
	var Community_Metric int
	var Pull_Requests int

	for _, line := range lines {
		if strings.Contains(line, "Number of Events") {
			fields := strings.Fields(line)
			fmt.Sscanf(fields[3], "%d", &Number_of_Events)
		} else if strings.Contains(line, "Number of Starred") {
			fields := strings.Fields(line)
			fmt.Sscanf(fields[3], "%d", &Number_of_Starred)
		} else if strings.Contains(line, "Number of Subscribers") {
			fields := strings.Fields(line)
			fmt.Sscanf(fields[3], "%d", &Number_of_Subscribers)
		} else if strings.Contains(line, "Number of Commits") {
			fields := strings.Fields(line)
			fmt.Sscanf(fields[3], "%d", &Number_of_Commits)
		} else if strings.Contains(line, "Number of Open_Issues") {
			fields := strings.Fields(line)
			fmt.Sscanf(fields[3], "%d", &Number_of_Open_Issues)
		} else if strings.Contains(line, "Number of Closed_Issues") {
			fields := strings.Fields(line)
			fmt.Sscanf(fields[3], "%d", &Number_of_Closed_Issues)
		} else if strings.Contains(line, "Community Metric") {
			fields := strings.Fields(line)
			fmt.Sscanf(fields[2], "%d", &Community_Metric)
		} else if strings.Contains(line, "Pull_Requests") {
			fields := strings.Fields(line)
			fmt.Sscanf(fields[1], "%d", &Pull_Requests)
		}
	}
}

//export rampUpScore
func rampUpScore(contributors int, linesOfCode int) float64 {
	return float64(contributors) / float64(linesOfCode)
}

//export license
func license(license string) float64 {
	if license == "MIT License" {
		return 1.0
	} else {
		return 0.0
	}
}

//export busFactorScore
func busFactorScore(developers int) float64 {
	score := float64(developers) / 100
	if score > 1 {
		return 1
	}
	return score
}

//export correctnessScore
func correctnessScore(openIssues int, closedIssues int, communityMetric float64) float64 {
	totalIssues := openIssues + closedIssues
	openIssuesRatio := float64(openIssues) / float64(totalIssues)
	score := (1 - openIssuesRatio) + communityMetric
	if score > 1 {
		return 1
	}
	return score
}
func netScore(correctnessScore float64, busFactorScore float64, license float64, rampUpScore float64) float64 {
	final_score := (2*correctnessScore + 1.5*busFactorScore + 2*license + 2*rampUpScore) / 10.5
	return final_score
}
