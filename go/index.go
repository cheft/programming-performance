package main

import (
  "fmt"
  "net/http"
)

func helo(w http.ResponseWriter, r *http.Request){
  fmt.Fprintf(w, "Hello World")
}

func main() {
  http.HandleFunc("/", helo)
  http.ListenAndServe(":8080", nil)
}
