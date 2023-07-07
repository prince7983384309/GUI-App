import os
from tkinter import *
from  tkinter import ttk
from PIL import Image,ImageTk
import random
from tkinter import messagebox
import tempfile  # for print bill
from time import strftime



# making a classs======================================================
class bill_app:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x900")
        self.root.title(" PRINCE MALL")

# some important variable after price selection automatically
        self.customername = StringVar()
        self.customerphone = StringVar()
        self.billno        = StringVar()
        b_no = random.randint(1,10000)
        self.billno.set(b_no)
        self.mail      = StringVar()
        # self.searchbill    = StringVar()
        self.subprocategory = StringVar()
        self.mainprocategory  = StringVar()
        self.pronamecategory  = StringVar()
        self.price         = IntVar()
        self.quantity      = IntVar()
        self.subtotal      = StringVar()
        self.textfield     = StringVar()
        self.tax           =StringVar()
        self.total         = StringVar()



        ## now we will write  product list eliments after completing all products+++++++++++
        self.category = ["select option","mobile","clothes","food"]
        self.subcategorymobile =["apple","samsung","mi"]
        #yha mobiles ke name and unke price variable---------------
        self.apple =["iphone-11","iphone-12","iphone-13"]
        self.ip11_price = 60000
        self.ip12_price = 90000
        self.ip13_price = 100000


        self.samsung =["galaxy-10","galaxy-11","galaxy-12"]
        self.gx10_price = 20000
        self.gx11_price = 30000
        self.gx12_price = 50000

        self.mi =["mi-6","mi-7","mi-8"]
        self.mi6_price = 7000
        self.mi7_price = 10000
        self.mi8_price = 15000


        # yha colthes ki category-----------------------------
        self.subcategoryclothes = ["t-shirt","pant","kurta"]
        self.tshirt =["levis","flue","oswal"]
        self.levis_price = 5000
        self.flue_price = 4000
        self.oswal_price = 3000

        self.pant =["jeans","trouser","capry"]
        self.jeans_price = 3000
        self.trouser_price = 2000
        self.capry_price = 1000

        self.kurta = ["cotton","hojri","saneel"]
        self.cotton_price = 800
        self.hojri_price = 700
        self.saneel_price = 600




        # yha food category----------------------------------------
        self.subcategoryfood = ["indian","chianeez","fastfood"]
        self.indian=["dal-chawal","chiken","vegetables"]
        self.dalchawal_price = 500
        self.chiken_price = 1000
        self.veg_price = 600

        self.china = ["springroll","noodle","chaumeen"]
        self.springroll_price = 400
        self.noodle_price = 800
        self.chaumeen_price = 500

        self.fastfood =["pizza","burger","maggi"]
        self.pizza_price = 500
        self.burger_price = 200
        self.maggi_price = 250

        # importing images
        #image = 1======================================================
        img1 = Image.open("images\\mall.jpg")
        img1 = img1.resize((280,130),Image.ANTIALIAS)
        self.photoimage_1 = ImageTk.PhotoImage(img1)
         # making lable for img1
        lbl_img1 = Label(self.root,image=self.photoimage_1)
        lbl_img1.place(x=0,y=0,width=280,height=130)

        # image = 2======================================================
        img2 = Image.open("images\\food.jpg")
        img2 = img2.resize((280, 130), Image.ANTIALIAS)
        self.photoimage_2 = ImageTk.PhotoImage(img2)

        # making lable for img2
        lbl_img2 = Label(self.root, image=self.photoimage_2)
        lbl_img2.place(x=280 , y=0, width=280, height=130)

        # image = 3=========================================================
        img3 = Image.open("images\\mobile.jpg")
        img3 = img3.resize((280, 130), Image.ANTIALIAS)
        self.photoimage_3 = ImageTk.PhotoImage(img3)

        # making lable for img3
        lbl_img3 = Label(self.root, image=self.photoimage_3)
        lbl_img3.place(x=560, y=0, width=280, height=130)

        # image = 4=========================================================
        img4 = Image.open("images\\clothes.jpg")
        img4 = img4.resize((280, 130), Image.ANTIALIAS)
        self.photoimage_4 = ImageTk.PhotoImage(img4)

        # making lable for img4
        lbl_img4 = Label(self.root, image=self.photoimage_4)
        lbl_img4.place(x=840, y=0, width=280, height=130)

        # maing label for mall title=========================================
        lbl_title = Label(self.root,text="* * * * * * Welcome to PRINCE MALL * * * * * *",
                          bg="white",fg="orangered",font=("times 25 bold italic underline"))
        lbl_title.place(x=0,y=130,width=1200)

        # making frame 1
        main_frm = Frame(self.root,bd=5,relief=GROOVE,bg="yellowgreen")
        main_frm.place(x=0,y=175,width=1530,height=500)

        # making customer form into mainframe+++++++++++++++++++++++++++++++++++++++
        cus_frame =LabelFrame(main_frm,text="fill and press 'customer detail'",bg="white",fg="red",
                              font=("times 10 bold italic"))
        cus_frame.place(x=4 ,y=1,width=300,height=110)

        # labels and entries in frame =========================================

        # label for customer name
        self.cus_lbl=Label(cus_frame,text="Name  :",bg="white",fg="black",
                             font=("times 12 bold italic"))
        self.cus_lbl.grid(row=0,column=0)
        #entry for customer name
        self.entry_cname=ttk.Entry(cus_frame,textvariable=self.customername,
                                   font=("times 12 "),width= 27)
        self.entry_cname.grid(row=0,column=1)

        #label for mobile no
        self.mob_lbl = Label(cus_frame, text="Mobile :", bg="white", fg="black",
                             font=("times 13 bold italic"))
        self.mob_lbl.grid(row=1, column=0)
        #entry for mobile no
        self.entry_mobile = ttk.Entry(cus_frame, font=("times 10 "),
                                      textvariable=self.customerphone, width=36)
        self.entry_mobile.grid(row=1, column=1)

        # label for email
        self.mail_lbl = Label(cus_frame, text="Mail :", bg="white", fg="black",
                             font=("times 13 bold italic"))
        self.mail_lbl.grid(row=3, column=0)
        # entry for email
        self.entry_mail = ttk.Entry(cus_frame, font=("times 12 "),
                            textvariable=self.mail  ,      width=27)
        self.entry_mail.grid(row=3, column=1)

        # making product frame 2 into main frame++++++++++++++++++++++++++++++++++++
        product_frame = LabelFrame(main_frm, text=" selct Product and press 'add cart'", bg="white", fg="red",
                               font=("times 10 bold italic"))
        product_frame.place(x=306, y=1, width=405, height=110)

        #making label for product category

        self.category_lbl = Label(product_frame, text="Category :", bg="white", fg="black",
                             font=("times 13 bold italic"))
        self.category_lbl.grid(row=0, column=0)
        # make combobox to select product category
        self.combo_category = ttk.Combobox(product_frame,state="readonly",
                           values=self.category ,font=("times 10 bold italic"),
                            textvariable=self.mainprocategory, width=15)
        self.combo_category.current(0)
        self.combo_category.bind("<<ComboboxSelected>>", self.categori)

        self.combo_category.grid(row=0,column=1)



        # making label for product sub category

        self.subcat_lbl = Label(product_frame, text="Sub Cate :", bg="white", fg="black",
                                  font=("times 13 bold italic"))
        self.subcat_lbl.grid(row=1, column=0)

        # make combobox to select product subcategory
        self.combo_subcat = ttk.Combobox(product_frame, state="readonly",
                            values= self.subcategorymobile,
              textvariable= self.subprocategory  ,font=("times 10 bold italic"), width=15)
        self.combo_subcat.bind("<<ComboboxSelected>>",self.product_name)

        self.combo_subcat.grid(row=1, column=1)



        # making label for product name

        self.proname_lbl = Label(product_frame, text="Pro Name :", bg="white", fg="black",
                                font=("times 13 bold italic"))
        self.proname_lbl.grid(row=3, column=0)

        # make combobox to select product name
        self.combo_proname = ttk.Combobox(product_frame, state="readonly",
                values=self.apple  ,font=("times 10 bold italic"),
                         textvariable=self.pronamecategory,       width=15)
        self.combo_proname.bind("<<ComboboxSelected>>",self.price_product)
        self.combo_proname.grid(row=3, column=1)

        # making label for price
        self.price_lbl = Label(product_frame, text="Price :", bg="white", fg="black",
                                 font=("times 13 bold italic"))
        self.price_lbl.grid(row=0, column=3)

        # make combobox to select product category
        self.combo_price = ttk.Combobox(product_frame, state="readonly", width=15,
                         textvariable=self.price ,font=("times 10"))
        self.combo_price.grid(row=0, column=4)

        # making label for product quantity
        self.quantity_lbl = Label(product_frame, text="quant:", bg="white", fg="black",
                               font=("times 13 bold italic"))
        self.quantity_lbl.grid(row=1, column=3)
        # making entry for product quantity
        self.entry_quantity = ttk.Entry(product_frame, font=("times 10 "),
                         textvariable=self.quantity, width=15)
        self.entry_quantity.grid(row=1, column=4)

        # making imagesframe in main frame under product frame========================
        image_frame=Frame(main_frm,bd=0)
        image_frame.place(x=7,y=115,width=705,height=143)

        # importing images
        # image = 1======================================================
        img5 = Image.open("images\\anim6.jpg")
        img5 = img5.resize((356, 143), Image.ANTIALIAS)
        self.photoimage_5 = ImageTk.PhotoImage(img5)
        # making lable for img1
        lbl_img5 = Label(image_frame, image=self.photoimage_5,bd=0)
        lbl_img5.place(x=0, y=0 )

        # import image 2
        img6 = Image.open("images\\anim2.jpg")
        img6 = img6.resize((349, 143), Image.ANTIALIAS)
        self.photoimage_6 = ImageTk.PhotoImage(img6)
        # making lable for img1
        lbl_img6 = Label(image_frame, image=self.photoimage_6, bd=0)
        lbl_img6.place(x=356, y=0)






        # # making search frame in main frame====================================
        # search_frame=LabelFrame(main_frm, text="search",fg="red",bg="white",
        #                                 font = ("times 10 bold italic"))
        # search_frame.place(x=720,y=0,width=365,height=45)
        #
        # #making label for bill no
        # self.bill_lbl=Label(search_frame,text="Bill no.  :    ",bg="white",fg="black",
        #                        font="times 12 bold italic")
        # self.bill_lbl.place(x=30,y=0)
        # #make entry for bill no
        # self.entry_bill =Entry(search_frame, font=("times 9"),
        #                       textvariable=self.billno, width=22,bd=2)
        # self.entry_bill.place(x=115,y=0)
        #
        # # make search button
        # self.search_btn = Button(search_frame, text="Search", bg="orangered", fg="blue",
        #                           cursor="hand2", width=13, bd=3, font=("times 7 bold italic"))
        # self.search_btn.place(x=260,y=0)
        #



        # making frame  3 in right side for total buying==============================
        billing_frame = LabelFrame(main_frm, text="Total Billing", bg="white", fg="red",
                                   font=("times 10 bold italic"))
        billing_frame.place(x=720, y=0, width=365, height=259)

        # making scroll in y position
        scroll_y=Scrollbar(billing_frame,orient=VERTICAL)
        self.textarea=Text(billing_frame,yscrollcommand=scroll_y.set,bg="pink",
                           fg="blue",font="times 12")
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        self.text_area()
        # making frame for bill counter in bottom =====================================

        billcounter_frame = LabelFrame(main_frm, text="Bill Counter", bg="white", fg="red",
                                   font=("times 10 bold italic"))
        billcounter_frame.place(x=0, y=265, width=1530, height=100)


        # making label for sub total and entry------------------------------------
        self.subtotal_lbl = Label(billcounter_frame, text="Sub total :", bg="white",
                                  fg="black",font=("times 13 bold italic"))
        self.subtotal_lbl.grid(row=0, column=0)
        # making entry for product quantity
        self.entry_subtotal = ttk.Entry(billcounter_frame, font=("times 10"),
                            textvariable=self.subtotal, width=25)
        self.entry_subtotal.grid(row=0, column=1)

        # making govt text label and entry
        self.govtax_lbl = Label(billcounter_frame, text=" Tax :", bg="white", fg="black",
                                  font=("times 13 bold italic"))
        self.govtax_lbl.grid(row=1, column=0)
        # making entry for product quantity
        self.entry_tax = ttk.Entry(billcounter_frame, font=("times 10"),
                                      textvariable=self.tax , width=25)
        self.entry_tax.grid(row=1, column=1)

        # label for total billing
        self.total_lbl = Label(billcounter_frame, text="Total :", bg="white", fg="black",
                                 font=("times 13 bold italic"))
        self.total_lbl.grid(row=2, column=0)
        # making entry for product quantity
        self.entry_total = ttk.Entry(billcounter_frame,textvariable= self.total,
                                     font=("times 10"), width=25)
        self.entry_total.grid(row=2, column=1)

        # make anather buttonframe in billcounter frame================================
        btn_frame = LabelFrame(billcounter_frame, text="other option", bg="yellowgreen", fg="red",
                                   font=("times 10 bold italic"))
        btn_frame.place(x=250, y=0,width=775,height=70)


        #add button in button frame--------------
        #add to cart button
        self.cart_btn = Button(btn_frame, text="Add to cart", bg="orangered", fg="black",
                               cursor="hand2",bd=5,command=self.add_item,
                               font=("times 15 bold italic"))
        self.cart_btn.grid(row=0, column=1 ,padx=5)

        # genrate bill button
        self.bill_btn = Button(btn_frame, text="Bill Genrate", bg="orangered",
                               fg="black",command=self.bill_genrate,
                               cursor="hand2",bd=5,font=("times 15 bold italic"))
        self.bill_btn.grid(row=0, column=2 ,padx=5)

        #save bill button
        self.savebill_btn = Button(btn_frame, text="customer detail", bg="orangered", fg="black",
                                   cursor="hand2",bd=5,
                                   command=self.text_area,font=("times 15 bold italic"))
        self.savebill_btn.grid(row=0, column=0 ,padx=5)

        #print bill button
        self.printbill_btn = Button(btn_frame, text="save Bill", bg="orangered", fg="black",
                               cursor="hand2",bd=5,command= self.prnt_bill,
                               font=("times 15 bold italic"))
        self.printbill_btn.grid(row=0, column=3 ,padx=5)

        #clear bill button
        self.clearbill_btn = Button(btn_frame, text=" Clear Bill", bg="orangered", fg="black",
                               cursor="hand2",bd=5,
                                    command=self.clear_btn,font=("times 15 bold italic"))
        self.clearbill_btn.grid(row=0, column=4 ,padx=5)

        # exit button
        self.exitbill_btn = Button(btn_frame, text="Exit", bg="orangered", fg="black",
                                    cursor="hand2",width=8,bd=5,
                                   command=self.root.destroy,font=("times 15 bold italic"))
        self.exitbill_btn.grid(row=0, column=5, padx=5)





    # making functions for category and subcategory()()()()()()()()()()()()()()()()

    def categori(self,event=""):
        if self.combo_category.get() =="mobile":
            self.combo_subcat.config(value=self.subcategorymobile)
            self.combo_subcat.current(0)

        if self.combo_category.get() =="clothes":
            self.combo_subcat.config(value=self.subcategoryclothes)
            self.combo_subcat.current(0)

        if self.combo_category.get() == "food":
            self.combo_subcat.config(value=self.subcategoryfood)
            self.combo_subcat.current(0)


    # add product name =============================================================
    def product_name(self,event=""):
      if  self.combo_subcat.get() =="apple":
          self.combo_proname.config(value=self.apple)
          self.combo_proname.current(0)

      if self.combo_subcat.get() == "samsung":
          self.combo_proname.config(value=self.samsung)
          self.combo_proname.current(0)

      if self.combo_subcat.get() == "mi":
          self.combo_proname.config(value= self.mi)
          self.combo_proname.current(0)

      if self.combo_subcat.get() == "t-shirt":
          self.combo_proname.config(value= self.tshirt)
          self.combo_proname.current(0)

      if self.combo_subcat.get() == "pant":
          self.combo_proname.config(value= self.pant)
          self.combo_proname.current(0)

      if self.combo_subcat.get() == "kurta":
          self.combo_proname.config(value=self.kurta)
          self.combo_proname.current(0)

      if self.combo_subcat.get() == "indian":
          self.combo_proname.config(value=self.indian)
          self.combo_proname.current(0)

      if self.combo_subcat.get() == "chianeez":
          self.combo_proname.config(value=self.china)
          self.combo_proname.current(0)

      if self.combo_subcat.get() == "fastfood":
          self.combo_proname.config(value=self.fastfood)
          self.combo_proname.current(0)


      # set price automatically after chossing product===============================
    def price_product(self,event=""):

 # mobiles category=================================================
        # iphone mobiles
            if self.combo_proname.get() == "iphone-11":
                self.combo_price.config(values=self.ip11_price)
                self.combo_price.current(0)
                self.quantity.set(1)

            if self.combo_proname.get() == "iphone-12":
                self.combo_price.config(values=self.ip12_price)
                self.combo_price.current(0)
                self.quantity.set(1)

            if self.combo_proname.get() == "iphone-13":
                self.combo_price.config(values=self.ip13_price)
                self.combo_price.current(0)
                self.quantity.set(1)
         #  samsung mobiles
            if self.combo_proname.get() == "galaxy-10":
                self.combo_price.config(values=self.gx10_price)
                self.combo_price.current(0)
                self.quantity.set(1)

            if self.combo_proname.get() == "galaxy-11":
                self.combo_price.config(values=self.gx11_price)
                self.combo_price.current(0)
                self.quantity.set(1)

            if self.combo_proname.get() == "galaxy-12":
                self.combo_price.config(values=self.gx12_price)
                self.combo_price.current(0)
                self.quantity.set(1)

        # mi phones
            if self.combo_proname.get() == "mi-6":
                self.combo_price.config(values= self.mi6_price)
                self.combo_price.current(0)
                self.quantity.set(1)

            if self.combo_proname.get() == "mi-7":
                self.combo_price.config(values= self.mi7_price)
                self.combo_price.current(0)
                self.quantity.set(1)

            if self.combo_proname.get() == "mi-8":
                self.combo_price.config(values= self.mi8_price)
                self.combo_price.current(0)
                self.quantity.set(1)

# clothes category -======================================================
 #  t shirt ["levis","flue","oswal"]===========================================================
            if self.combo_proname.get() == "levis":
                self.combo_price.config(values= self.levis_price)
                self.combo_price.current(0)
                self.quantity.set(1)

            if self.combo_proname.get() == "flue":
                self.combo_price.config(values= self.flue_price)
                self.combo_price.current(0)
                self.quantity.set(1)

            if self.combo_proname.get() == "oswal":
                self.combo_price.config(values= self.oswal_price)
                self.combo_price.current(0)
                self.quantity.set(1)

  #  pant-   ["jeans","trouser","capry"]

            if self.combo_proname.get() == "jeans":
                self.combo_price.config(values= self.jeans_price)
                self.combo_price.current(0)
                self.quantity.set(1)

            if self.combo_proname.get() == "trouser":
                self.combo_price.config(values= self.trouser_price)
                self.combo_price.current(0)
                self.quantity.set(1)

            if self.combo_proname.get() == "capry":
                self.combo_price.config(values= self.capry_price)
                self.combo_price.current(0)
                self.quantity.set(1)

  # kurta - ["cotton","hojri","saneel"]===========================

            if self.combo_proname.get() == "cotton":
                self.combo_price.config(values=self.cotton_price)
                self.combo_price.current(0)
                self.quantity.set(1)


            if self.combo_proname.get() == "hojri":
                self.combo_price.config(values=self.hojri_price)
                self.combo_price.current(0)
                self.quantity.set(1)


            if self.combo_proname.get() == "saneel":
                self.combo_price.config(values=self.saneel_price)
                self.combo_price.current(0)
                self.quantity.set(1)

  # food=============================================================
  #indian food -["dal-chawal","chiken","vegetables"]
            if self.combo_proname.get() == "dal-chawal":
                self.combo_price.config(values=self.dalchawal_price)
                self.combo_price.current(0)
                self.quantity.set(1)


            if self.combo_proname.get() == "chiken":
                self.combo_price.config(value=self.chiken_price)
                self.combo_price.current(0)
                self.quantity.set(1)


            if self.combo_proname.get() == "vegetables":
                self.combo_price.config(value=self.veg_price)
                self.combo_price.current(0)
                self.quantity.set(1)

 # chaineez food-  ["springroll","noodle","chaumeen"]
            if self.combo_proname.get() == "springroll":
                self.combo_price.config(value=self.springroll_price)
                self.combo_price.current(0)
                self.quantity.set(1)


            if self.combo_proname.get() == "noodle":
                self.combo_price.config(value=self.noodle_price)
                self.combo_price.current(0)
                self.quantity.set(1)

            if self.combo_proname.get() == "chaumeen":
                self.combo_price.config(value=self.chaumeen_price)
                self.combo_price.current(0)
                self.quantity.set(1)

  # fast food ["pizza","burger","maggi"] =======================

            if self.combo_proname.get() == "pizza":
                self.combo_price.config(value=self.pizza_price)
                self.combo_price.current(0)
                self.quantity.set(1)

            if self.combo_proname.get() == "burger":
                self.combo_price.config(value=self.burger_price)
                self.combo_price.current(0)
                self.quantity.set(1)

            if self.combo_proname.get() == "maggi":
                self.combo_price.config(value=self.maggi_price)
                self.combo_price.current(0)
                self.quantity.set(1)


# price and quantity ke bad text area me fill krenge==================================

    def text_area (self):

        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"                       Welcome to Prince Mall")
        self.textarea.insert(END,f"\n Bill No : {self.billno.get()}")
        self.textarea.insert(END,f"\n Customer name   :      {self.customername.get()}")
        self.textarea.insert(END, f"\n Customer phone  :     {self.customerphone.get()}")
        self.textarea.insert(END, f"\n Customer email   :    {self.mail.get()}")

        self.textarea.insert(END, "\n =====================================")
        self.textarea.insert(END, f"\n Product\t\tQty\t\tPrice")
        self.textarea.insert(END, "\n =====================================")


# quantity *prices ke liye function    add cart button to text area=============================================
        self.lst =[]

    def add_item(self):

      self.pr= self.price.get()
      self.qty=self.quantity.get()*self.pr
      self.lst.append(self.qty)
      if self.pronamecategory.get()=="":
          messagebox.showerror("product not fill","plz select the product name")
      else:
          self.textarea.insert(END,f"\n { self.pronamecategory.get()}"
                                   f"\t\t{self.quantity.get()}\t\t{self.qty}")

          #self.subtotal.set(str('Rs.%.2f'%(sum(self.lst))))
          # self.tax.set(str('Rs.%.2f'%((((sum(self.lst))-(self.price.get()))*self.tax)/100)))
          # self.total.set(str('Rs.%.2f'%(((sum(self.lst))+((((sum(self.lst))- (self.price.get()))*self.tax)/100)))))

          self.subtotal.set(sum(self.lst))
          self.tax.set(sum(self.lst)*8/100)
          self.total.set(sum(self.lst)+sum(self.lst)*8/100)




    #bill genrate ka button function bnayenge============================================
    def bill_genrate(self):

        if self.pronamecategory.get()=="":
          messagebox.showerror("product not fill","plz select the product to add cart")
        else:
            #text =self.textarea.get(len(self.lst))
            #self.text_area()
            #self.add_item() # fuction call
            #self.textarea.insert(END,text)
            self.textarea.insert(END,"\n ===================================== ")
            self.textarea.insert(END,f"\n sub amount :\t\t\t{ self.subtotal.get() }")
            self.textarea.insert(END, f"\n tax amount :\t\t\t{self.tax.get()}")
            self.textarea.insert(END, f"\n total amount :\t\t\t{self.total.get()}")

    # work on print button=========================================
    def prnt_bill(self):
        veriabl=self.textarea.get(1.0 ,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(veriabl)
        os.startfile(filename,"print")


# all data clear button============================================
    def clear_btn(self):
        self.textarea.delete(1.0,END)
        self.customername.set("")
        self.customerphone.set("")
        self.mail.set("")
        self.subprocategory.set("")
        self.mainprocategory.set("select option")
        self.pronamecategory.set("")
        self.price.set("0")

        self.quantity.set("0")

        self.subtotal.set("")
        self.textfield.set("")
        self.tax.set("")
        self.total.set("")

        self.text_area()


# working on exit button=================================
# direct commad hai exait button me































if __name__=='__main__':
    root = Tk()
    obj = bill_app(root)
    root.mainloop()




