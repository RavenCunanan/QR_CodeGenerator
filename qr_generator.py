import qrcode
import validators

count=0
def generate_qr():
    global count  
    print()
    print("Website QR Code Generator")
    print()

    while True:
        website_link = input("Enter the website link: ")
        if validators.url(website_link):
            break
        else:
            print("Invalid URL! Please enter a valid website link!")

    qr = qrcode.QRCode(version=1, box_size=5, border=5)
    qr.add_data(website_link)
    qr.make()

    print()
    user_input = input("Enter 1 for a black QR code or enter 2 for a white QR code: ")
    print()

    while True:
        if user_input == "1":
            img = qr.make_image(fill_color='black', back_color='white')
            break
        elif user_input == "2":
            img = qr.make_image(fill_color='white', back_color='black')
            break
        else:
            print("Invalid input! Please enter either 1 or 2.")

    #Create unique file names
    
    count+=1
    filename=website_link.split('//')[1].split('.')[1]+str(count)+'_qr.png'
    img.save(filename)

    print()
    print("QR code saved as:", filename)
    print()

while True:
    generate_qr()
    answer = input("Would you like to generate another QR code? (yes/no): ").lower()
    if answer != 'yes':
        print("Exiting.")
        break