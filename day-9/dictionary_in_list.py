travel_log=[
    {
        "country":"France",
        "visits":12,
        "cities":["Paris","lille","Dijon"]
    },
    {
        "country":"Germany",
        "visits":5,
        "cities":["Berlin","Hamburg","Stuttgart"]
    },
]


def add_new_country(country,visits,cities):
    new_country={
        "country":country,
        "visits" :visits,
        "cities"  :cities
    }
    travel_log.append(new_country)
   


add_new_country("Russia",2,["Moscow","Pittsburg","Cremea"])

print(travel_log)

