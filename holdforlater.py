# url = "https://the-cocktail-db.p.rapidapi.com/popular.php"
# KEY = '1f4b3e251bmshb1df2538c036ddfp1c6675jsn19129a6f9614'
# headers = {
# 	"X-RapidAPI-Key": "1f4b3e251bmshb1df2538c036ddfp1c6675jsn19129a6f9614",
# 	"X-RapidAPI-Host": "the-cocktail-db.p.rapidapi.com"
#     }

# response = requests.get(url, headers=headers)
# data = response.json()
# for drink in data['drinks']:
#     print(drink)


<!-- {% for drink in returnDrink %}
        <h1 name="drinkname">{{drink.strDrink}}</h1>
        <p name="alcoholic">{{drink.strAlcoholic}}</p>
        <p name="glass">{{drink.strGlass}}</p>
        <ul>
            <li>{{drink.strIngredient1}} x {{drink.strMeasure1}}</li>
            <li>{{drink.strIngredient2}} x {{drink.strMeasure2}}</li>
            <li>{{drink.strIngredient3}} x {{drink.strMeasure3}}</li>
            <li>{{drink.strIngredient4}} x {{drink.strMeasure4}}</li>
            <li>{{drink.strIngredient5}} x {{drink.strMeasure5}}</li>
            <li>{{drink.strIngredient6}} x {{drink.strMeasure6}}</li>
            <li>{{drink.strIngredient7}} x {{drink.strMeasure7}}</li>
            <li>{{drink.strIngredient8}} x {{drink.strMeasure8}}</li>
            <li>{{drink.strIngredient9}} x {{drink.strMeasure9}}</li>
        </ul>
        <p>{{drink.strInstructions}}</p>
        <form method="POST" action="/{{drink.strDrink}}">
            <button>FAVORITE THIS DRINK</button>
        </form>
        {% endfor %} -->