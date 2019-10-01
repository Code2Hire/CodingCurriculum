package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"net/http"
	"os"

	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux"
)

type Disc struct {
	ID    int64  `json:"id"`
	Brand string `json:"brand"`
	Model string `json:"model"`
	Style string `json:"style"`
	Price string `json:"price"`
	Color string `json:"color"`
	Img   string `json:"img"`
	Img2  string `json:"img2"`
	Descr string `json:"descr"`
}

var db *sql.DB
var err error

func main() {
	//open db connection
	db, err = sql.Open("mysql", os.Getenv("MYSQL_USER")+":"+os.Getenv("MYSQL_PASSWORD")+"@tcp(db:3306)/"+os.Getenv("MYSQL_DATABASE"))
	if err != nil {
		panic(err.Error())
	}
	defer db.Close()

	//set up endpoints with mux router
	router := mux.NewRouter()
	router.HandleFunc("/discs/", getAll).Methods("GET")
	router.HandleFunc("/discs/style/{style}", getStyle).Methods("GET")
	router.HandleFunc("/discs/{id}", getDisc).Methods("GET")
	router.HandleFunc("/discs/{id}", deleteDisc).Methods("DELETE")
	router.HandleFunc("/discs/", addDisc).Methods("POST")

	http.ListenAndServe(":8080", router)

}

func getAll(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	var discs []Disc
	enableCors(&w)
	result, err := db.Query("SELECT id, brand, model, style, price, color, img, img2, descr from discs")
	if err != nil {
		panic(err.Error())
	}
	defer result.Close()
	//store returned values into disc struct and add disc structs to discs slice
	for result.Next() {
		var disc Disc

		err := result.Scan(&disc.ID, &disc.Brand, &disc.Model, &disc.Style, &disc.Price, &disc.Color, &disc.Img, &disc.Img2, &disc.Descr)
		if err != nil {
			panic(err.Error())
		}
		discs = append(discs, disc)
	}
	w.WriteHeader(http.StatusOK)
	//encode discs slice into json
	json.NewEncoder(w).Encode(discs)
}

//get all discs of a certain style
func getStyle(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	var discs []Disc
	params := mux.Vars(r)
	enableCors(&w)
	result, err := db.Query("SELECT id, brand, model, style, price, color, img, img2, descr from discs WHERE style = ?", params["style"])
	if err != nil {
		panic(err.Error())
	}
	defer result.Close()

	for result.Next() {
		var disc Disc
		err := result.Scan(&disc.ID, &disc.Brand, &disc.Model, &disc.Style, &disc.Price, &disc.Color, &disc.Img, &disc.Img2, &disc.Descr)
		if err != nil {
			panic(err.Error())
		}
		discs = append(discs, disc)
	}
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(discs)
}

//get a single disc entry
func getDisc(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	enableCors(&w)
	result, err := db.Query("SELECT id, brand, model, style, price, color, img, img2, descr from discs WHERE id = ?", params["id"])
	if err != nil {
		panic(err.Error())
	}
	defer result.Close()
	var disc Disc
	for result.Next() {
		err := result.Scan(&disc.ID, &disc.Brand, &disc.Model, &disc.Style, &disc.Price, &disc.Color, &disc.Img, &disc.Img2, &disc.Descr)
		if err != nil {
			panic(err.Error())
		}
	}
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(disc)
}

func addDisc(w http.ResponseWriter, r *http.Request) {
	//create a disc to hold the incoming request
	var disc Disc
	//read the request body with a json decoder and store into the disc just created
	json.NewDecoder(r.Body).Decode(&disc)

	//insert query with `?` to parameterize values to protect from sql injection
	query := `INSERT INTO discs (id, brand, model, style, price, color, img, img2, descr) values (?,?,?,?,?,?,?,?,?)`
	//using db.Exec for inserts returns a Result, not a row. Give it a query plus the parameters that will replace each `?` in the query string
	res, err := db.Exec(query, disc.ID, disc.Brand, disc.Model, disc.Style, disc.Price, disc.Color, disc.Img, disc.Img2, disc.Descr)
	//for real though, catch those errors.
	if err != nil {
		fmt.Println(err)
		return
	}
	//if there wasn't an error, then there was no problem connecting to the database and running the query.
	// You can then use the Result, res, to find out what happened. LastInsertId returns the auto-incremented id for the item that you just saved.
	id, err := res.LastInsertId()
	//Catchin' those errors
	if err != nil {
		fmt.Println(err)
		return
	}
	// now that you have the last inserted ID, you can save it to the user that came in on the original request.
	disc.ID = id

	//Because we successfully saved the user, let the caller know the item was created with a HTTP status code 201 Created
	w.WriteHeader(http.StatusCreated)

	//Use the writer (w) to create a json encoder and encode the user that was saved and respond to the caller with json.
	json.NewEncoder(w).Encode(disc)
}
func deleteDisc(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	result, err := db.Query("DELETE FROM discs WHERE id = ?", params["id"])
	if err != nil {
		panic(err.Error())
	}
	defer result.Close()
	w.WriteHeader(http.StatusOK)
}
func enableCors(w *http.ResponseWriter) {
	(*w).Header().Set("Access-Control-Allow-Origin", "*")
}
