package main

// Showcasing how to import a package and use it

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(math.Floor(2.5))
	fmt.Println(math.Ceil(2.5))
	fmt.Println(math.Sqrt(25))
	fmt.Println(strutil("25"))
}
