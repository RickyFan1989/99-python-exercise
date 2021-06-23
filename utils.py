from tornado import httpclient
import json 

from constants import LISTING_SERVICE_URL, USER_SERVICE_URL

def get_users(id=None, url_head=USER_SERVICE_URL):
    http_client = httpclient.HTTPClient()
    url = url_head + 'users'
    print("url: ", url)

    users = []
    if id is not None:
        url += "?id=" + str(id)
    try:
        response = http_client.fetch(url)
        print(response.body)
        data = json.loads(response.body)
        users = data["users"]

    except httpclient.HTTPError as e:
        # HTTPError is raised for non-200 responses; the response
        # can be found in e.response.
        print("Error: " + str(e))

    except Exception as e:
        # Other errors are possible, such as IOError.
        print("Error: " + str(e))
    
    http_client.close()

    return users



def create_user(name, url_head=USER_SERVICE_URL):
    http_client = httpclient.HTTPClient()
    # response = yield http_client.fetch("http://localhost:8889/variazione", method='POST', body=body)

    url = url_head + 'users' + '?name=' + str(name)
    print("url: ", url)

    user = dict()
    try:
        response = http_client.fetch(url, method='POST', allow_nonstandard_methods=True)
        print(response.body)
        data = json.loads(response.body)
        user = data["user"]
    except httpclient.HTTPError as e:
        # HTTPError is raised for non-200 responses; the response
        # can be found in e.response.
        print("Error: " + str(e))

    except Exception as e:
        # Other errors are possible, such as IOError.
        print("Error: " + str(e))
    
    http_client.close()

    return user

def get_listings(user_id=None, url_head=LISTING_SERVICE_URL):
    http_client = httpclient.HTTPClient()
    url = url_head + 'listings'
    print("url: ", url)

    # if user_id is not None:
    #     user = get_users(id=user_id)

    listings = []
    if user_id is not None:
        url += "?user_id=" + str(id)

    try:
        response = http_client.fetch(url)
        print(response.body)
        data = json.loads(response.body)
        listings = data["listings"]
        for listing in listings:
            user_id = listing["user_id"]
            listing["user"] = get_users(id=user_id)[0]
            del listing["user_id"]

    except httpclient.HTTPError as e:
        # HTTPError is raised for non-200 responses; the response
        # can be found in e.response.
        print("Error: " + str(e))

    except Exception as e:
        # Other errors are possible, such as IOError.
        print("Error: " + str(e))
    
    http_client.close()

    return listings



def create_listing(user_id, listing_type, price, url_head=LISTING_SERVICE_URL):
    http_client = httpclient.HTTPClient()
    # response = yield http_client.fetch("http://localhost:8889/variazione", method='POST', body=body)

    url = url_head + 'listings' + '?user_id=' + str(user_id) + '&listing_type=' + str(listing_type) + '&price=' + str(price) 
    print("url: ", url)
    
    listing = dict()
    try:
        response = http_client.fetch(url, method='POST', allow_nonstandard_methods=True)
        print(response.body)
        data = json.loads(response.body)
        listing = data["listing"]
    except httpclient.HTTPError as e:
        # HTTPError is raised for non-200 responses; the response
        # can be found in e.response.
        print("Error: " + str(e))

    except Exception as e:
        # Other errors are possible, such as IOError.
        print("Error: " + str(e))
    
    http_client.close()

    return listing



if __name__ == "__main__":
    print(get_users())
    print(get_users(id=1))
    print(get_users(id=2))

    print(create_user('Bob'))



