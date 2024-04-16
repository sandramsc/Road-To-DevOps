package main

import "fmt"

func concat(s1 string, s2 string) string {
	return s1 + s2
}

// don't touch below this line

func main() {
	test("Lane", " happy bday!")
	test("Elon", " hope that SpaceX works out great")
	test("Zack", " is great")
}

func test(s1 string, s2 string) {
	fmt.Println(concat(s1, s2))
}
