bluesync
magic = 0xb5b5
Fields:
type - 1 = request bluetooth connection
       2 = bluetooth connection failed
       3 = bluetooth connection eliminated
       0 = bluetooth connection successful
       4 = ask for current owner

flow:
bob wants to connect.
a. bob will try to connect to server
b. server will check current owner - "alice"
c. server will ask alice to release
d. alice will release, will notify server "i release"
e. server will set isfree to true, send "im free" to bob.
f. bob will try to connect to server
g. server replies "success" - sets current owner to bob, isFree to false

