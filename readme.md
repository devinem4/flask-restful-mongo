# flask-restful-mongo
`pip install -r requirements.txt`  
`source venv/bin/activate`  

`sudo docker-compose build`  
`sudo docker-compose up`  
`sudo docker-compose down`  

### urls
`ip a` look for eth0  
mongo express: http://100.115.92.206:8081  
mongo uri: mongo:27017  
api endpoint w/o mongo: http://100.115.92.206:5000/hello  
api endpoint post to mongo: http://100.115.92.206:5000/user  

### notes for next time
add `host="0.0.0.0"` to `app.run(debug=True, host="0.0.0.0", port=8080)` so that server is publicly available