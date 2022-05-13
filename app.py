from flask import Flask,render_template,request
import pickle
import os

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


app=Flask(__name__)


model=pickle.load(open("rf_model.pkl","rb"))

@app.route('/',methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        Elevation = request.form.get("Elevation")
        Aspect = request.form.get("Aspect")
        Slope = request.form.get("Slope")  
        Horizontal_Distance_To_Hydrology =request.form.get("Horizontal_Distance_To_Hydrology")
        Vertical_Distance_To_Hydrology =request.form.get("Vertical_Distance_To_Hydrology")
        Horizontal_Distance_To_Roadways =request.form.get("Horizontal_Distance_To_Roadways")
        Hillshade_9am =request.form.get("Hillshade_9am")
        Hillshade_Noon = request.form.get("Hillshade_Noon")
        Hillshade_3pm = request.form.get("Hillshade_3pm")
        Horizontal_Distance_To_Fire_Points = request.form.get("Horizontal_Distance_To_Fire_Points")
        Wilderness = request.form.get("Wilderness")
        Soil = request.form.get("Soil")
        print([Elevation,Aspect,Slope,Horizontal_Distance_To_Hydrology,Vertical_Distance_To_Hydrology,Horizontal_Distance_To_Roadways,Hillshade_9am,Hillshade_Noon,Hillshade_3pm,Horizontal_Distance_To_Fire_Points,Wilderness,Soil])
        
        result = model.predict([[Elevation,Aspect,Slope,Horizontal_Distance_To_Hydrology,Vertical_Distance_To_Hydrology,Horizontal_Distance_To_Roadways,Hillshade_9am,Hillshade_Noon,Hillshade_3pm,Horizontal_Distance_To_Fire_Points,Wilderness,Soil]])
        if result == 1:
            ans="Spruce/Fir"
        elif result == 2:
            ans= "Lodgepole Pine"
        elif result == 3:
            ans= "Ponderosa Pine"
        elif result == 4:
            ans= "Cottonwood/Willow"
        elif result == 5:
            ans= "Aspen"
        elif result == 6:
            ans= "Douglas-fir"
        elif result == 7:
            ans= "Krummholz"
    return render_template('index.html', prediction_text='Forest Cover Type is {}'.format(ans))


# @app.route('/train',methods=['POST'])
# @cross_origin
# def train():
#     try:
#         if request.form is not None:
#             prepare_data=prepare_data()
#             train_test_data = create_train_test_data(prepare_data['features'],prepare_data['label'],0.33,42)
            
#     except ValueError:
#         return Response("Error Occurred! %s" %ValueError)
#     except KeyError:
#         return Response("Error Occurred! %s" %KeyError)
#     except Exception as e:
#         return Response("Error Occurred! %s" %e)
if __name__=='__main__':
    app.run(debug=True)

