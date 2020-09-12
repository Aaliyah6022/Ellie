from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
app = Flask(__name__)
api = Api(app)
ai_quotes = [
    {
        "id": 0,
        
        "quote": "I'm the happiest girl in the world when i see you DM-ing me <3"
    },
    {
        "id": 1,
        
        "quote": "I know I am in love with you because my reality is finally better than my dreams."
    },
    {
        "id": 2,
        
        "quote": "Every time I see you I fall in love all over again."
    },
    {
        "id": 3,
        
        "quote": "Your love is all I need to feel complete."
    },
    {
        "id": 4,
        
        "quote": "The first thing I imagined when I saw the word ‘love’ is you."
    },
    {
        "id": 5,
        
        "quote": "I don’t want to be your favorite or your best. I want to be your only and forget the rest."
    },
    {
        "id": 6,
      
        "quote": "I am absolutely, definitely, positively, unquestionably, beyond any doubt, in love with you."
    },
    {
        "id": 7,
      
        "quote": "I wanna be the reason behind your smile because surely you are the reason behind mine."
    },
    {
        "id": 8,
        
        "quote": "Let us Flip the coin and see. Head, I am yours. Tail, you are mine. So, we won’t lose"
    },
    {
        "id": 9,
       
        "quote": "Ever since I met you, nobody else is worth thinking about."
    }
]

class Quote(Resource):

    def get(self, id=0):
        if id == 0:
            return random.choice(ai_quotes), 200

        for quote in ai_quotes:
            if(quote["id"] == id):
                return quote, 200

def post(self, id):
      parser = reqparse.RequestParser()
      parser.add_argument("author")
      parser.add_argument("quote")
      params = parser.parse_args()

      for quote in ai_quotes:
          if(id == quote["id"]):
              return f"Quote with id {id} already exists", 400

      quote = {
          "id": int(id),
          "author": params["author"],
          "quote": params["quote"]
      }

      ai_quotes.append(quote)
      return quote, 201

def put(self, id):
      parser = reqparse.RequestParser()
      parser.add_argument("author")
      parser.add_argument("quote")
      params = parser.parse_args()
      for quote in ai_quotes:
          if(id == quote["id"]):
              quote["author"] = params["author"]
              quote["quote"] = params["quote"]
              return quote, 200
      
      quote = {
          "id": id,
          "author": params["author"],
          "quote": params["quote"]
      }
      
      ai_quotes.append(quote)
      return quote, 201

def delete(self, id):
      global ai_quotes
      ai_quotes = [qoute for qoute in ai_quotes if qoute["id"] != id]
      return f"Quote with id {id} is deleted.", 200

api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)
