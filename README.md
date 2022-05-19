Deployment instructions:
- clone https://github.com/KhayrulloevDD/shop_visit.git repository;
- create virtual environment and activate it(optional);
- install dependencies from the requirements.txt file (pip install -r requirements.txt);
- install & run your postgres db (change default to sqlite in settings.py file if you want to use sqlite db)
- migrate migrate (python manage.py migrate);
- run the server (python manage.py runserver).

API's

- GET: http://127.0.0.1:8000/api/shop/trade_points?phone_number=phone_number
  
  example response:
        
        [
            {
        
                "id": 2,
                "name": "TP2",
                "employee": 1
            }
        ]
  
  
- POST: http://127.0.0.1:8000/api/shop/attend_tp?phone_number=phone_number
  
    example required body data:
  
      {
        "trade_point": 1,
        "latitude": "3",
        "longitude": "11"
      }
  example response:
  
      {
        "id": 7,
        "date": "2022-05-19T15:21:47.346280+05:00"
      }