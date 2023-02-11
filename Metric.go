package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"io/ioutil"
)

func readFromFile(file string) string {
	data := ""

	f, err := os.Open(file)
	if err != nil {
		// fmt.Println(err)
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
	lines := strings.Split(data, "https")
	lines = lines[1:]
	//fmt.Println(lines)
	var Number_of_Events int
	var Number_of_Starred int
	var Number_of_Subscribers int
	var Number_of_Commits int
	var Number_of_Open_Issues int
	var Number_of_Closed_Issues int
	var Community_Metric int
	var Pull_Requests int
	var Lines_of_Code int
	// scores := make(map[string]float64)
	
	for _, line := range lines {
		line1 := strings.Split(line,"\n")
		line1[0] = "https" + line1[0]
		dir := strings.Split(line1[0],"/")//[len(line1)-1]
		dir1 := dir[len(dir)-1]
		Lines_of_Code = numLines(dir1)
		fmt.Println(Lines_of_Code)
		for _, ind := range line1 {
			if strings.Contains(ind, "Number of Events") {
				fields := strings.Fields(ind)
				fmt.Sscanf(fields[3], "%d", &Number_of_Events)
			} else if strings.Contains(ind, "Number of Starred") {
				fields := strings.Fields(ind)
				fmt.Sscanf(fields[3], "%d", &Number_of_Starred)
			} else if strings.Contains(ind, "Number of Subscribers") {
				fields := strings.Fields(ind)
				fmt.Sscanf(fields[3], "%d", &Number_of_Subscribers)
			} else if strings.Contains(ind, "Number of Commits") {
				fields := strings.Fields(ind)
				fmt.Sscanf(fields[3], "%d", &Number_of_Commits)
			} else if strings.Contains(ind, "Number of Open_Issues") {
				fields := strings.Fields(ind)
				fmt.Sscanf(fields[3], "%d", &Number_of_Open_Issues)
			} else if strings.Contains(ind, "Number of Closed_Issues") {
				fields := strings.Fields(ind)
				fmt.Sscanf(fields[3], "%d", &Number_of_Closed_Issues)
			} else if strings.Contains(ind, "Community Metric") {
				fields := strings.Fields(ind)
				fmt.Sscanf(fields[2], "%d", &Community_Metric)
			} else if strings.Contains(ind, "Pull_Requests") {
				fields := strings.Fields(ind)
				fmt.Sscanf(fields[1], "%d", &Pull_Requests)
			}
		}
		// scores["RAMP_UP_SCORE"] = rampUpScore()
		// scores["CORRECTNESS_SCORE"] = correctnessScore()
		// scores["BUS_FACTOR_SCORE"] = busFactorScore()
		// scores["RESPONSIVE_MAINTAINER_SCORE"] = responsiveMaintainerScore()
		// scores["LICENSE_SCORE"] = license()

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

func numLines(dir string) int{
	files, err := ioutil.ReadDir(dir)
	if err != nil {
		fmt.Println("Error reading file:", err)
	}
	out := 0
	for _, f:= range files {
		//fmt.Println(f.Name())
		content, err := ioutil.ReadFile(dir + "/" + f.Name())
		content1 := string(content)
		if err != nil {
			//fmt.Println("Error reading file:", err)
			continue
		}
		lines := strings.Split(content1,"\n")
		nonEmpty := []string{}
		for _, str := range lines{
			ex := ([]rune(str))
			ex1 := 13
			if len(ex) != 0{
				ex1 = int(ex[0])
			}
			if ex1 != 13 || len(ex) != 1{
				nonEmpty = append(nonEmpty,str)
			}
		}
		out = out + len(nonEmpty)
		// fmt.Println(len(nonEmpty))
	}
	return out
}
