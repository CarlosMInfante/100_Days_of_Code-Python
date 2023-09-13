# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades = {}


# for student in student_scores:
#     score = student_scores[student]
#     if score >= 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"


# print(student_grades)

#  Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a List in a Dictionary.
travel_log = {
    "Frace": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgrat"]
}

#Nesting a Dictionary in a Dictionary.
travel_log_2 = {
    "Frace": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgrat"], "total_visits": 5}
}

#Nesting a Dictionary in a List.
travel_log_3 = [
    {
        "country": "France",
        "total_visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    {
        "country" : "Germany",
        "total_visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgrat"]
    },
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log_3.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log_3)