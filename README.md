# Drone-Delivery-Planning API

This is a hobby project that uses the core algorithmic log from the Drone delivery route planning repository, and converts it into a simple Flask API with a single POST request endpoint.

## POST /calc

### Example request (in curl)
```
curl --location '127.0.0.1:5000/calc' \
--header 'Content-Type: application/json' \
--data '{
    "num_of_customers": 3,
    "max_drone_num": 2,
    "drone_capacity": 10,
    "depot_coords": {
        "lat": 33.40968118765043,
        "long": -111.916380996181
    },
    "orders": {
        "1": {
            "coordinates": {
                "lat": 33.41355484357154,
                "long": -111.92650756558604
            },
            "demand": 2
        },
        "2": {
            "coordinates": {
                "lat": 33.415723373415126,
                "long": -111.92102201007762
            },
            "demand": 5
        },
        "3": {
            "coordinates": {
                "lat": 33.40755824948113,
                "long": -111.90806792010417
            },
            "demand": 2
        }
    },
    "drone_params": {
        "weight": 1,
        "capacity": 50,
        "number": 2,
        "bat_consum_perkm_perkg": 0.05,
        "takeoff_landing": 0
    }
}'
```

### Example response
```
{
    "num_of_drones": 2,
    "route": [
        [
            [
                33.40968118765043,
                -111.916380996181
            ],
            [
                33.415723373415126,
                -111.92102201007762
            ],
            [
                33.41355484357154,
                -111.92650756558604
            ],
            [
                33.40968118765043,
                -111.916380996181
            ]
        ],
        [
            [
                33.40968118765043,
                -111.916380996181
            ],
            [
                33.40755824948113,
                -111.90806792010417
            ],
            [
                33.40968118765043,
                -111.916380996181
            ]
        ]
    ],
    "route_with_color": [
        [
            [
                [
                    33.40968118765043,
                    -111.916380996181
                ],
                [
                    33.415723373415126,
                    -111.92102201007762
                ],
                [
                    33.41355484357154,
                    -111.92650756558604
                ],
                [
                    33.40968118765043,
                    -111.916380996181
                ]
            ],
            "#000000"
        ],
        [
            [
                [
                    33.40968118765043,
                    -111.916380996181
                ],
                [
                    33.40755824948113,
                    -111.90806792010417
                ],
                [
                    33.40968118765043,
                    -111.916380996181
                ]
            ],
            "#0066ff"
        ]
    ]
}
```