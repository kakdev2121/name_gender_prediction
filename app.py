from flask import Flask
from flask_restful import Resource,Api,reqparse
#from flask_cors import CORS
import gender_pred_resource




## Adding Request parameters
parser = reqparse.RequestParser()
parser.add_argument('name',type =str, help = 'This field cannot be blank', required = True)

                                                    

app =Flask(__name__)
#CORS(app)
api = Api(app)

# @app.route("/")
class gender_prediction_model(Resource):
    def post(self):
        try:
            data = parser.parse_args()
            print(data)

            name = data["name"].strip()
            if not name:
                return ({"status" : 400,
                      "message" : "API failed do check the name field"})
            else:
                gender_prediction_response = {
                    "status" : 200,
                    "message" : "success",
                    "data" : gender_pred_resource.gender_prediction(name)
                                         }  
                return(gender_prediction_response)
        except Exception as e:
            return(f'Check the name feild {e}')

                  
                  
api.add_resource(gender_prediction_model,'/gender_prediction_model')

if __name__ == '__main__':
    app.run(debug = True)
