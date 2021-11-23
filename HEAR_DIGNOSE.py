from tkinter import*
root = Tk()
root.title("Heart_Dignose_Report")
root.geometry("600x600")
root.configure(bg="cyan")

question1_radioButton = StringVar(value = "0")
Question1 = Label(root, text = "Do you experience shortness of breath during toutine activities?",bg = "cyan")
Question1.pack()
question1_r1 = Radiobutton(root, text = "yes", variable = question1_radioButton, value = "yes", bg = "cyan")
question1_r1.pack()
question1_r2 = Radiobutton(root, text = "no", variable = question1_radioButton, value = "no",bg = "cyan")
question1_r2.pack()

question2_radioButton = StringVar(value = "0")
Question2 = Label(root, text = "Do you have swelling in the feet/ ankles/ legs (shoes feel tighter) or abdomen?",bg = "cyan")
Question2.pack()
question2_r1 = Radiobutton(root, text = "yes", variable = question2_radioButton, value = "yes", bg = "cyan")
question2_r1.pack()
question2_r2 = Radiobutton(root, text = "no", variable = question2_radioButton, value = "no", bg = "cyan")
question2_r2.pack()

question3_radioButton = StringVar(value = "0")
Question3  = Label(root, text = "Do you feel any of these symptoms - confusion, disorientation, or loss of memory?",bg = "cyan")
Question3.pack()
question3_r1 = Radiobutton(root, text = "yes", variable = question3_radioButton, value = "yes",bg = "cyan")
question3_r1.pack()
question3_r2 = Radiobutton(root, text = "no", variable = question3_radioButton, value = "no",bg = "cyan")
question3_r2.pack()

question4_radioButton = StringVar(value = "0")
Question4  = Label(root, text = "Do you experience shortness of breath while running down?",bg = "cyan")
Question4.pack()
question4_r1 = Radiobutton(root, text = "yes", variable = question4_radioButton, value = "yes",bg = "cyan")
question4_r1.pack()
question4_r2 = Radiobutton(root, text = "no", variable = question4_radioButton, value = "no",bg = "cyan")
question4_r2.pack()

question5_radioButton = StringVar(value = "0")
Question5  = Label(root, text = "Do you experience persistant wheezing / coughting that produces white or pink blood tinged mucus?",bg = "cyan")
Question5.pack()
question5_r1 = Radiobutton(root, text = "yes", variable = question5_radioButton, value = "yes",bg = "cyan")
question5_r1.pack()
question5_r2 = Radiobutton(root, text = "no", variable = question5_radioButton, value = "no",bg = "cyan")
question5_r2.pack()


def fever_score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score + 10
        print(score)
    if question2_radioButton.get()=="yes":
        score = score + 10
        print(score)
    if question3_radioButton.get()=="yes":
        score = score + 10
        print(score)
    if question4_radioButton.get()=="yes":
        score = score + 10
        print(score)
    if question5_radioButton.get()=="yes":
        score = score + 10
        print(score)
        
        
    if score <= 10:
        messagebox.showinfo("Report","You don't need to visit a doctor.")
    elif score > 10 and score <= 30:
        messagebox.showinfo("Reprot","You might perhaps have to visit a doctor")
    else:
        messagebox.showinfo("Report","I strongly advise you to visit a doctor")
btn = Button(root, text = "click me", command = fever_score)
btn.pack()

root.mainloop()