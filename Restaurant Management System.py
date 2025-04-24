import tkinter as tk
from tkinter import ttk, messagebox

class RestraurantOrderManagement:
    def __init__(self,root):
        self.root = root
        self.root.title("Restraurant Management App")
        self.menu_items = {
             "FRIES MEAL": 2,
             "LUNCH MEAL": 2,
             "BURGER MEAL":3,
             "PIZZA MEAL":4,
             "CHEESE BURGER":2.5,
             "DRINKS":1
        }
        frame = ttk.Frame(master=root)
        frame.place(relx=0.5, rely=0.5,anchor=tk.CENTER)

        ttk.Label(frame,
                  text="Restaurant Order Management").grid(row=0,columnspan=3)
        self.menu_labels = {}
        self.menu_quantities = {}
         
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(frame,
                              text=f"{item} (${price}):")
            label.grid(row=1, column=0)
            self.menu_labels[item]=label

            quantity_entry =ttk.Entry(frame, width=5)
            quantity_entry.grid(row=1, column=1)
            self.menu_quantities[item] = quantity_entry
        order_button = ttk.Button(frame,
                                  text="Place Order",
                                  command=self.place_order)
        order_button.grid(row=len(self.menu_items) + 2,columnspan=3)

    def place_order(self):
        total_cost = 0
        order_summary= "Order Summary:\n"
        for item, entry  in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity= int(quantity)
                price = self.menu_items[item]
                cost  = quantity * price
                total_cost+= cost
                if quantity > 0:
                 order_summary += f"{item} : {quantity} x {price} = {cost}\n"
        if total_cost> 0:
            order_summary+= f"\nTotal Cost: {total_cost}"
            messagebox.showinfo(
                "Order Placed",
                order_summary
            )
        else:
            messagebox.showerror("Error", "Please order atleast one item.")
if __name__ == "__main":
    root = tk.Tk()
    app = RestraurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()

            
            