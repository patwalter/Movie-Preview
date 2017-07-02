import fresh_tomatoes
import media

"""Below are 6 of my favorite movies and attributes for the website code builtinto fresh tomatoes."""
"""the class Movie is in the file media all in the same folder"""
#The movies instances below have the attributes of title storyline poster and youtune trailer

nightmare_christmas = media.Movie("The Nightmare Before Christmas",
                                "The mayor of Halloween Town, tired of \
                                 his job, decides to take a try at Chrsitmas.",
                                "http://www.impawards.com/1993/posters/nightmare_before_christmas_ver1.jpg",
                                "https://www.youtube.com/watch?v=wr6N_hZyBCk")
the_avengers = media.Movie("The Avengers",
                           "5 heros must team up to defeat a bigger threat \
                            none of them could face alone.",
                            "https://images-na.ssl-images-amazon.com/images/I/61bINjWK62L.jpg",
                             "https://www.youtube.com/watch?v=eOrNdBpGMv8")
spirtied_away = media.Movie("Spirted Away",
                            "A young girl must work foran evil witch who has \
                             turned her parentsinto pigs.",
                            "https://images-na.ssl-images-amazon.com/images/I/41jOy%2BrrcHL._AC_UL320_SR216,320_.jpg",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

final_fantasy = media.Movie("Final Fantast VII: Advent Children",
                            "Cloud Strife and his companions must face the \
                             children of an evil entity and the return of an \
                             old foe.",
                            "https://fanart.tv/fanart/movies/647/movieposter/final-fantasy-vii-advent-children-53bd247d24cfd.jpg",
                            "https://www.youtube.com/watch?v=wut2am39z-c")

the_incredibles= media.Movie("The Incredibles",
                             " A retired hero is called back to acion, \
                               and this time, accompanied by his family.",
                             "https://images-na.ssl-images-amazon.com/images/I/71kod5t-q9L._AC_UL320_SR214,320_.jpg",
                             "https://www.youtube.com/watch?v=eZbzbC9285I")

last_holiday = media.Movie("Last Holiday",
                           "A woman thinks she is dying, so she spends all \
                            her savings to take a luxury vacation",
                            "http://static.rogerebert.com/uploads/movie/movie_poster/last-holiday-2006/large_dp51drDOZ5xMt2Qi8JxQeKKzHPV.jpg",
                            "https://www.youtube.com/watch?v=fBUcxMNInL8")

#the list was needed to import into the website found in the fresh_tomatoes file

movies = [nightmare_christmas, the_avengers, spirtied_away, final_fantasy, the_incredibles, last_holiday]

fresh_tomatoes.open_movies_page(movies)

#finally, the foile calls on the open property to open that page

                
                
              
        

             
