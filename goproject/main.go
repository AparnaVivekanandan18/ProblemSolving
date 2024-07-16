// Implement a producer-consumer problem using goroutines and channels.

package main

import (
	"fmt"
	"sync"
)

// Here do the add of 2 num
func producer(numbers chan int, wg *sync.WaitGroup) {
	// First goroutine to send a number to the channel
	go func() {
		defer wg.Done()
		numbers <- 3
	}()

	// Second goroutine to send another number to the channel
	go func() {
		defer wg.Done()
		numbers <- 4
	}()
}

// Here display the sum of 2 numbers
func consumer(numbers chan int, done chan bool) {
	var sum int
	for number := range numbers {
		sum = sum + number
	}
	fmt.Println("The sum is:", sum)
	done <- true

}

func main() {
	ch1 := make(chan int, 2)
	done := make(chan bool)
	var wg sync.WaitGroup

	wg.Add(2)
	// Always do "Call By Reference for Synchronization primitives like sync.WaitGroup / sync.Mutex"
	go producer(ch1, &wg)

	// Always do "Call By Reference for Synchronization primitives like sync.WaitGroup / sync.Mutex"
	go consumer(ch1, done)

	// Wait for the producers to finish
	wg.Wait()
	// Close the channel to signal to the consumer that no more data will be sent
	close(ch1)
	// Wait for the consumer to finish
	<-done
}
