## Football data analysis

Compute 10 years + 5 leagues of football to build statistical prediction

## Retrieving data
Data can be found on repositories like : https://datahub.io/collections/football
The script BulkDownload generate CSV file for the 5 big championship of the 25 last seasons

## Setup and exectution

Install Python

## Set up venv and install dependencies

```shell
python3 -m venv venv
```

```shell
.\venv\Script\activate
pip install -r requirements.txt
```
## Setup WebApp
I used Next.js to create React App. It’s versatile and lets you create React apps of any size—from a mostly static blog to a complex dynamic application.
To launch it, type :
```shell
cd webapp
npm install
npm run dev
```
WebApp is starting on localhost:3000


## Objectives 

### Tab with the ranking of all the leagues availables and seasons
### Compute streaks and display the main opportunities

-0.5 HT Goals
-1.5 HT Goals
+1.5 FT Goals
-3.5 FT Goals
Lay the draw
