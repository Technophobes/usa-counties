Install: `pip3 install rq redis`

To start Redis install docker desktop and run `docker run -p6379:6379 redis`.


To start the worker: `rq worker counties`

The worker runs the function `station_queue.add_station_from_queue` on every item that gets put in the queue.

The api "stations" POST endpoint puts the request data on the queue.