
print('---------------------------------------------------------------------------')
print('\t\tNear East University Facial Recognation System ')
print('---------------------------------------------------------------------------')
print('\t\t\t     Author:Hamza_Ezzat')
print('---------------------------------------------------------------------------')
print(" \n\n")
print("MENU\n(1)CREATING NEW STUDENT\n(2)TRAINING IMAGES\n(3)DETECTING STUDENT\n(4)STUDENTS LIST\n(5)GENERATING REPORT\n(6)QUIT")
choice=input(">>>")
ch=1
while ch!=0 and choice !=6:
    if choice==1: #Student List
        import dataset as ds
        ds.dataset()
        choice=input("\nMENU\n(1)CREATING NEW STUDENT\n(2)TRAINING IMAGES\n(3)DETECTING STUDENT\n(4)STUDENTS LIST\n(5)GENERATING REPORT\n(6)QUIT\n\n>>>")

        continue
    elif choice==2: #Create new Student
        import trainner
        print ("Trained Images successfully")
        choice=input("\nMENU\n(1)CREATING NEW STUDENT\n(2)TRAINING IMAGES\n(3)DETECTING STUDENT\n(4)STUDENTS LIST\n(5)GENERATING REPORT\n(6)QUIT\n\n>>>")
        continue
    elif choice==3: #Training Images
        import detector
        choice=input("\nMENU\n(1)CREATING NEW STUDENT\n(2)TRAINING IMAGES\n(3)DETECTING STUDENT\n(4)STUDENTS LIST\n(5)GENERATING REPORT\n(6)QUIT\n\n>>>")
        continue

    elif choice==4: #Detecting Student
        import sqlpy as dis
        dis.displayDatabase()
        choice=input("\nMENU\n(1)CREATING NEW STUDENT\n(2)TRAINING IMAGES\n(3)DETECTING STUDENT\n(4)STUDENTS LIST\n(5)GENERATING REPORT\n(6)QUIT\n\n>>>")
        continue

    elif choice==5: #Reporting Student
    	import report as rep
        rep.rep()
        print ("\nReport generated successfully")
        choice=input("\nMENU\n(1)CREATING NEW STUDENT\n(2)TRAINING IMAGES\n(3)DETECTING STUDENT\n(4)STUDENTS LIST\n(5)GENERATING REPORT\n(6)QUIT\n\n>>>")
        continue
    else:
        print("Invalid choice, please choose again")
        print("\n")
print("")
print(".")
