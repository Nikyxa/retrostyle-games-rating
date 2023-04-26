# Data parser from Metacritic and Steam sites for TOP150 RTS Games
## Project description
This project is a data parser from two gaming sites: Metacritic and Steam. The parser retrieves information about games such as title, platform, date of release, genre, ratings, amount of ratings, etc. Then data is exported to CSV format.

## Installation and use instructions
1. If you are using PyCharm - it may propose you automatically create venv for your project 
    and install requirements in it, but if not:
    ```
    python -m venv venv
    venv\Scripts\activate (on Windows)
    pip install -r requirements.txt
    ```
2. Run the parser_metacritic.py file to launch the Metacritic parser. This will create a metacritic.csv file with all the necessary information about the games.
Run the parser_steam.py file to launch the parser for Steam. As a result, a steam.csv file will be created with all the necessary information about the games.

## CSV file format
Each CSV file contains the following game information:

- Title 
- Platform
- Date of release 
- Genre
- Ratings
- Amount of ratings

# Data parser from Wikipedia for 3 games
## Project description
This project is a data parser from three Wikipedia articles about games: Tinykin, Pikmin 2, Age of Empires. The parser retrieves information about games such as titles, info about producers, designers, and more detailed info about the games. The data is then exported to CSV format. To get data you also should run parsers with names of games.
