
import time

def sleep(n_secs):
    time.sleep(n_secs)


def get_timestamp():
    now_time=time.strftime('%Y_%m_%d_%H_%M_%S')
    return now_time
    #return str(int(time.time()*1000))

def print_documentId(doc_id):
    print("documentId = {}".format(doc_id))

def get_base_url(env_type= "prod"):
    if env_type=="prod":
        return "https://mubu.com"

    else:
        return "https://test.mubu.com"