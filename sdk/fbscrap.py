# para que se haga efectivo el retorno de los datos se debe desplegar un aplicativo web
import facebook

token = "EAABrJSeWa0ABAFZBCZC7beeFnjlTusWNmZAPS0GkwWXxTIZB115S6nyeQf6RGAMTdEnAn7xqIEsoHjvrZAomA9xVxsTfu1nxReLvXulZCVcK4PDoj0Rx3YijalLaCdOKZC5RLaz47OL8yWyZAaudtXTM4qwIvDii236dwbsgRz0NgpbNjePfVS5EtT0IZB2YZApUIZD"

graph = facebook.GraphAPI(access_token=token, version='2.6')

profile = graph.get_object("me")
print(profile)
friends = graph.get_connections(id='me', connection_name='friends')
print(friends)
friend_list = [friend['name'] for friend in friends['data']]
print(friend_list)

query_string = 'posts?limit={0}'.format(1)
posts = graph.get_connections(profile['id'], query_string)
print(posts)
