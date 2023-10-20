import tkinter as tk
import predict_sales
import test1

root= tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=400, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Review Sentiment Analysis &\n Sales Prediction')
label1.config(font=('helvetica', 14),fg='blue')
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter your Review:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 80, window=label2)

entry1 = tk.Entry(root) 
canvas1.create_window(200, 120, window=entry1)

label3 = tk.Label(root, text='Enter your Product:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 160, window=label3)

entry2 = tk.Entry(root) 
canvas1.create_window(200, 200, window=entry2)

def get_sentiment():
    x1 = entry1.get()
    x2= entry2.get()
    
   # label3 = tk.Label(root, text='The Review ' + x1 + ' is:', font=('helvetica', 10))
    #canvas1.create_window(200, 210, window=label3)
    sentiment = test1.predict_review(x1)
    res = predict_sales.main(x2)
    fres= sentiment+ "\n\n"+ res
    label4 = tk.Label(root, text=fres, font=('helvetica', 8, 'bold'),wraplength=400, fg="green")
    canvas1.create_window(200, 300, window=label4)
    
button1 = tk.Button(text='Analyse Sentiment', command=get_sentiment, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 240, window=button1)

root.mainloop()
