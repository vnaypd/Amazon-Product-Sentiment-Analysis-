import pandas as pd
def main(x2):
    df = pd.read_csv('Reviews.csv')
    #x2="B0009XLVG0"
    df1 = df[df.ProductId == x2]
    if len(df1) > 0:
        data_dict = df1.to_dict()
         
        #print(data_dict)
        mscore=[]
        for data in data_dict:
            if data == "Score":
                val=data_dict[data]
                for v in val:
                    mscore.append(val[v])
                    
        #print(mscore)
        bad = 0
        avg = 0
        good = 0
        sales = "bad"
        
        for m in mscore:
            if m < 3:
                bad = bad+1
            elif m > 3:
                good = good+1
            else:
                avg = avg+1
        print("Bad Reviews Count: ",bad,"\nGood Reviews Count: ",good,"\nAvergae Reviews Count: ",avg)
        
        calc = 0
        if bad > (good or avg):
            sales="bad"
            calc =1
        elif avg > (good or bad):
            sales="avg"
            calc =1
        elif good >(bad or avg):
            sales="good"
            calc =1
        if calc == 0:
            if bad == avg:
                sales = "average"
            elif avg == good:
                sales = "good"
            elif bad == good:
                sales = "average"
        
        print("Predicted sale for",x2," is", sales,"for upcoming year")
        return "Predicted sale for Product ID: '"+x2+"' is "+sales+" for upcoming year"
    else:
        return "Product not found for sales prediction"
