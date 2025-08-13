def make_shirt(size= 'l', message= 'I love Python'):
    print("\nSummarizing the size of the shirt and the message")
    print("=" * 50)
    print("Size: " + size.upper())
    print("Messaeg: " + message)
make_shirt()
make_shirt(size= 'm')
make_shirt(size= 'xl', message= 'Hello world!')