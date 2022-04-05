import pymongo


def client_connect():
    global client, db2, col1
    try:
        client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.lcwuv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db2 = client.test
        print(db2)
    except Exception as e:
        print(e)


def newTable():

    try:
        db2 = client['nesibe']
        col1 = db2['ineuron']
    except Exception as e:
        print(e)

def insertData():
    global rec
    try:
        record = {'companyName': 'iNeuron',
                  'product': 'Affordable AI',
                  'courseOffered': 'Deep Learning for Computer Vision',
                  'name': ["sudhan", "kumar", 5466],
                  "record_dict": {"name": "sudhanshu", "mail_id": "sudhanshu@fadfsaf.ai", "ph_number": 543535}}

        col1.insert_one(record)
        list_of_records = [{'companyName': 'iNeuron',
                            'product': 'Affordable AI',
                            'courseOffered': 'Machine Learning with Deployment'},

                           {'companyName': 'iNeuron',
                            'product': 'Affordable AI',
                            'courseOffered': 'Deep Learning for NLP and Computer vision'},

                           {'companyName': 'iNeuron',
                            'product': 'Master Program',
                            'courseOffered': 'Data Science Masters Program',
                            "test": "ffsdfsffsf",
                            "complex": [{"name": "sudhanshu", "list": [554, 545, 454, 54, 5, 4]},
                                        {"email_id": "sudhanshu@dffsf"}, {"phone_no": 345345345353},
                                        [4, 54, 534, 5, 45, 5, 45, 4]]

                            }]

        col1.insert_many(list_of_records)
    except Exception as e:
        print(e)

def data_fetch():
    data = []
    try:
        for i in col1.find_one():
            data.append(i)
            print(i)
        return data
    except Exception as e:
        print(e)





if __name__ == '__main__':
    client_connect()
    newTable()
    insertData()
    # data_fetch()
