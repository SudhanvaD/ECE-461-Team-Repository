package main
import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main(){
	files, err := ioutil.ReadDir("./")
	if err != nil {
		panic(err)
	}
	for _, f:= range files {
		fmt.Println(f.Name())
		content, err := ioutil.ReadFile(f.Name())
		content1 := string(content)
		if err != nil {
			fmt.Println("Error reading file:", err)
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
		fmt.Println(len(nonEmpty))
	}
}

