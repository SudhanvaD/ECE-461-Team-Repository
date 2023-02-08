package main

func main() {

}
func rampUpScore(contributors int, linesOfCode int) float64 {
	return float64(contributors) / float64(linesOfCode)
}
func license(license string) float64 {
	if license == "MIT License" {
		return 1.0
	} else {
		return 0.0
	}
}
func busFactorScore(developers int) float64 {
	score := float64(developers) / 100
	if score > 1 {
		return 1
	}
	return score
}
func correctnessScore(openIssues int, closedIssues int, communityMetric float64) float64 {
	totalIssues := openIssues + closedIssues
	openIssuesRatio := float64(openIssues) / float64(totalIssues)
	score := (1 - openIssuesRatio) + communityMetric
	if score > 1 {
		return 1
	}
	return score
}
