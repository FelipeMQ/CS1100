import pafy

myvid = pafy.new("https://www.youtube.com/watch?v=kJQP7kiw5Fk")
print(myvid.videostreams)