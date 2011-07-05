import pickle
"""f=open("pickling_text","wb")
shop_list=["mango","apple","banana"]
pickle.dump(shop_list,f)
del shop_list
f.close()"""
shop_list=[]
print shop_list
f=open("pickling_text","rb")
shop_list=pickle.load(f)
print shop_list