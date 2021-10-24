import grpc
import location_pb2
import location_pb2_grpc

channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

user1_location = location_pb2.LocationMessage(
    person_id=1,
    latitude=100,
    longitude=200
)

user2_location = location_pb2.LocationMessage(
    person_id=2,
    latitude=300,
    longitude=400
)

response1 = stub.Create(user1_location)
response2 = stub.Create(user2_location)