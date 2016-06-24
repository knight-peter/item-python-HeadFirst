def save_transaction(price,credit_card,description):
    file=open("transactions.txt","a")# 这儿的“a”意味着你总是把记录添加在文件的尾部
    new_record="%07d%16s%s\n"%(price*100,credit_card,description)
    file.write(new_record)
    print(new_record)
    file.close()