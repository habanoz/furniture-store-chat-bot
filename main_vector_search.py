from index import Index as idx
from index import Index as idxl

def start_search_loop():
    index = idx()
    index_local = idxl()
    message = input("Merhaba:\n")
    context = index.find_context(message)
    print(context)
    print("---")
    context = index_local.find_context(message)
    print(context)


if __name__ == '__main__':
    start_search_loop()