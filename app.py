from flask import Flask
from flask import request
import numpy as np
from copy import deepcopy
from scipy.spatial.distance import squareform, pdist
from haversine import haversine
from vrp import nsgaAlgo


app = Flask(__name__)

@app.route("/calc", methods=["POST"])
def calculate_routes():
    if request.method == 'POST':
        data = request.json
        drone_params = data["drone_params"]
        depot_coords = data["depot_coords"] # Form: {"lat": lat, "long": long}
        
        # Orders are of the form {"order_id": {"coordinates": {"lat": lat, "long": long}, "demand": w}}
        orders = data["orders"]

        input_data = {
            "Number_of_customers": data["num_of_customers"],
            "max_vehicle_number": data["max_drone_num"],
            "vehicle_capacity": data["drone_capacity"],
            "depot": {
                "coordinates": depot_coords,
                "demand": 0,
            },

        }

        all_points = np.array([[depot_coords["lat"],depot_coords["long"]]])
        for order_id in orders:
            coords=orders[order_id]["coordinates"]
            all_points = np.append(all_points,[[coords["lat"], coords["long"]]],axis=0)
            input_data[f"customer_{order_id}"]=orders[order_id]

        input_data["distance_matrix"] = squareform(pdist(all_points, metric=haversine))
        input_data["instance_name"] = "Test"
        nsgaObj = nsgaAlgo(input_data,drone_params)

        nsgaObj.runMain()
        route = nsgaObj.get_solution()
        colorset=["#000000","#0066ff","#cc0000","#009900","#6600cc","#cc00cc","#009999"]
        route_with_color = list(zip(route,colorset))
        context ={
            "route": route,
            "num_of_drones": len(route),
            "route_with_color": route_with_color,
        }

        return context






