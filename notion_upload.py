import requests, json

def createPage(databaseId, headers, place_name, place_add, place_type, place_url):

    createUrl = 'https://api.notion.com/v1/pages'

    newPageData = {
        "parent": { "database_id": databaseId },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": place_name
                        }
                    }
                ]
            },
            "Address": {
                "rich_text": [
                    {
                        "text": {
                            "content": place_add
                        }
                    }
                ]
            },
            "Status": {
                "select": 
                    {
                        "name": "Anticipated"
                    }
            },
            "Type": {
                "select": 
                    {
                        "name": place_type
                    }
            },
            "url": {
                        "url": place_url
            }
        }
    }
    
    data = json.dumps(newPageData)
    # print(str(uploadData))

    res = requests.request("POST", createUrl, headers=headers, data=data)

    # print(res.status_code)
    # print(res.text)