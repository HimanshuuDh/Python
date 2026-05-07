def item_finder(item):
    groceries=["milk","bread","juice","chicken"]

    if item in groceries:
        print("Item found")
    else:
        print("Item not found")

def main():
    item_finder("salmon")

main()