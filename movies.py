# Movie library - add, view and search through your movies.

movies =[ {'title': 'The Green Mile', 'year': '1999', 'director': 'Frank Darabont'},
   {'title': 'Forrest Gump', 'year': '1994', 'director': 'Robert Zemeckis'},
    {'title': 'Leon', 'year': '1994', 'director': 'Luc Besson'},
    {'title': 'Avatar', 'year': '2009', 'director': 'James Cameron'}]


def add_new_movie():

    title = input('Enter the title: ')
    year = input('Enter the year:')
    director = input('Enter the director')


    movies.append(
    {
        'title': title,
        'year' : year,
        'director' : director
    }
 )

def view_all():

    for movie in movies:
        title = movie['title']
        year = movie['year']
        director = movie['director']
        print(title, year, director)

def search():
    user_search = input('Enter name on the movie, director or year:')

    for movie in movies:
        if user_search == movie['title']:
            print(movie['director'], movie['year'])

        elif user_search == movie['director']:
            print(movie['director'], movie['year'])

        elif (user_search) == movie['year']:
            print(movie['director'], movie['title'])



while True:
    new = input("\n For adding new movie to collection please type 1:"
                " \n To view all type 2: "
                "\n To search through movie collection type 3: "
                "\n To finish type 4: \n")
    if new == '1':
        add_new_movie()
    elif new == '2':
        view_all()
    elif new == '3':
        search()
    elif new == '4':
        break
