# mediatracker
This is a project I'll use to be able to track the various types of media i've consumed or want to.


Will consist of:
1. Database containing movies, tv shows and books I have either consumed or wish to.
2. Application layer handling receipt of new data/updating old data
3. Front end which will be searchable


##Front End
Will have options to display:
- lists such as top 10 (based on user input rating)
- Charts showing things such as genre preferences aggregated by media or broken down
- Things you want to read or watch or play
- Eventually maybe suggest things based on others preferences?

###Experience Design v0.1
 1. Upon entering URL the user will be taken to a login page.
    1. They can login, click forgot password or register a new account.
 2. Upon logging in they will be directed to the index page which will display a table of movies the has in their "wants to watch" list.
 3. There will also be a table of Movies the user has already watched.
 4. I'd like to pull from IMDB to provide data for popovers for each movie.
 5. Add a button to the "want to watch" table to move it to the watched which will prompt user for rating.
 6. 


###Ideas
- Store every users data on their own local machine, no need to host databases remotely.
- Use IMDB API for movies and tv shows where you can click on an actor in a movie in your list and it will automatically open a list of all their movies
- Social aspect of sharing and recommending media between users
- 


