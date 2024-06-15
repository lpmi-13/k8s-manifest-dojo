package main

import (
	"fmt"
	"log"
	"math/rand"
	"net"
	"net/http"
	"os"
	"strconv"
	"syscall"
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
	    // Check for connection refused error
		if netErr, ok := err.(net.Error); ok && netErr.Timeout() {
			log.Printf("timeout error for URL %s: %v", fullPath, err)
		} else if opErr, ok := err.(*net.OpError); ok {
			if sysErr, ok := opErr.Err.(*os.SyscallError); ok && sysErr.Err == syscall.ECONNREFUSED {
				log.Printf("connection refused for URL %s: %v", fullPath, err)
			} else {
				log.Printf("network error for URL %s: %v", fullPath, err)
			}
		} else {
			log.Printf("HTTP error for URL %s: %v", fullPath, err)
		}
	} else {
		log.Printf("received response code %d for URL %s", res.StatusCode, fullPath)
	}

	ch <- url
}
