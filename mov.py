import fresh_tomatoes
import media

avengers = media.Movie(" Avengers ", 
                        " The Avengers and their allies must be willing to sacrifice lifes to save the world ", 
                        " https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg ",
                        " https://www.youtube.com/watch?v=_xBziiJI3DU")

rampage = media.Movie("Rampage ", 
                        " Rampage is a 2018 American science fiction monster film ", 
                        " https://upload.wikimedia.org/wikipedia/en/6/6b/Rampage_teaser_film_poster.jpg",
                        " https://www.youtube.com/watch?v=-43MBOJnVks")

deadpool = media.Movie("Deadpool 2 ",
                        "Deadpool 2 is a 2018 American superhero film based on the Marvel Comics character Deadpool, distributed by 20th Century Fox",
                        "https://upload.wikimedia.org/wikipedia/en/c/cf/Deadpool_2_poster.jpg ",
                        " https://www.youtube.com/watch?v=D86RtevtfrA")

annihilation = media.Movie("Annihilation ",
                        "Annihilation is a 2018 science fiction psychological horror film",
                        "https://upload.wikimedia.org/wikipedia/en/f/f6/Annihilation_%28film%29.png ",
                        " https://www.youtube.com/watch?v=DILhOWzJkGE")

red_sparrow = media.Movie("Red Sparrow",
                          "Red Sparrow is a 2018 American spy thriller film directed by Francis Lawrence and written by Justin Haythe",
                          "https://upload.wikimedia.org/wikipedia/en/5/5a/Red_Sparrow.png",
                          "https://www.youtube.com/watch?v=PmUL6wMpMWw")

black_panther = media.Movie("Black Panther",
                            "Black Panther is a 2018 American superhero film based on the Marvel Comics character of the same name",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

movies = [avengers,  rampage,  deadpool,  annihilation,  red_sparrow, black_panther ]
                          
fresh_tomatoes.open_movies_page(movies)
                            









