n=int(input())
for guid in guides:
    if n==guid["pk"]:
        print (f'{guid["fields"]["full_name"]}, туров: {guid["fields"][ "tours_count"]}')
        print (guid["fields"]["bio"])