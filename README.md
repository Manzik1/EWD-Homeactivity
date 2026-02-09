I added  time complexity which is this  'O(n)' and path_t__graph
 I also Created another end point called save_analysis (POST)

To test do this:

curl -X POST http://localhost:8888/api/lead/convertToClient/$\(curl -s -H "Authorization: Bearer $(curl -s -X POST http://localhost:8888/api/login -H "Content-Type: application/json" -d '{
