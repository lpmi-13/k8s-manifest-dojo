package main

import (
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"os"
	"strconv"
	"time"
)

const DELAY = 1000
const NUMBER_OF_USERS = 26

func main() {

    webserver_domain := os.Args[1]
	concurrentExecutions, _ := strconv.Atoi(os.Args[2])

	ch := make(chan string)

	for i := 0; i < concurrentExecutions; i++ {
		go sendRequest(webserver_domain, ch)
	}

	for {
		go sendRequest(<-ch, ch)
	}
}

func randomURLPath() string {
  URL_PATHS := []string{
    "/all_users",
	fmt.Sprintf("/user/%v", randomUserId()),
	"/log-info",
  }

  indexToChoose := rand.Intn(3)
  return URL_PATHS[indexToChoose]
}

func randomUserId() int {
    min := 1
    max := NUMBER_OF_USERS
    return rand.Intn(max) + min
}

func sendRequest(url string, ch chan string) {
	time.Sleep(DELAY * time.Millisecond)
	fullPath := url + randomURLPath()
	log.Printf("calling: %s", fullPath)

	res, err := http.Get(fullPath)
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Println("got status code:", res.StatusCode)

	ch <- url
}