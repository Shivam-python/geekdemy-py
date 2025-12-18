from config.constants import *


class Purchase:
    def __init__(self):
        self.items = 0
        self.items_list = []
        self.pro_member = False
        self.discount_coupon = None

    def add_item(self, item_name, unit_price, quantity):
        self.items += quantity
        self.items_list.append({'name': item_name, 'unit_price': unit_price, 'price': unit_price * quantity, 'quantity': quantity})
        self.items_list.sort(key=lambda x: x['unit_price'])

    def apply_pro_membership(self):
        self.pro_member = True
        
    def apply_discount_coupon(self, coupon_code):
        selected_coupon = self.evaluate_coupon_hierarchy(coupon_code)
        self.discount_coupon = selected_coupon

    def evaluate_coupon_hierarchy(self, coupon_code):
        if self.items>=4:
            return "B4G1"
        else:
            if self.discount_coupon:
                return COUPON_HIERARCHY[max(COUPON_HIERARCHY.index(coupon_code), COUPON_HIERARCHY.index(self.discount_coupon))]
            return coupon_code
        
    def fetch_enrollment_fee(self, amount):
        if amount < 6666:
            return 500
        return 0

    def generate_bill(self):
        freebie = False
        sub_total = sum(item['price'] for item in self.items_list)
        total = sub_total
        pro_membership_discount = 0
        coupon_discount = 0
        if self.discount_coupon == "B4G1":
            coupon_discount = self.items_list[0]['unit_price']
            freebie = True
        else:
            coupon_discount = total*DISOUNT_PRICE.get(self.discount_coupon)            
        
        total -= coupon_discount

        enrollment = self.fetch_enrollment_fee(total)
        total+=enrollment
        sub_total+=enrollment

        if self.pro_member:
            
            start = 0
            if freebie:
                start = 1
            
            for item in self.items_list[start:]:
                discount = self.get_item_discount_for_pro(item)
                pro_membership_discount += discount
                total -= discount
                item["price"] -= discount
            
            sub_total += PRO_MEMBERSHIP_FEES
            total += PRO_MEMBERSHIP_FEES

        bill = {"SUB_TOTAL": round(sub_total,2), "COUPON_DISCOUNT": round(coupon_discount,2), "TOTAL_PRO_DISCOUNT": round(pro_membership_discount,2), "TOTAL": round(total,2),"ENROLLMENT_FEE": round(enrollment,2)}
        if self.pro_member:
            bill["PRO_MEMBERSHIP_FEE"] = PRO_MEMBERSHIP_FEES
        return bill
    
    def get_item_discount_for_pro(self, item):
        return item['price'] * PRO_DISCOUNT.get(item['name'], 0)
    
    def print_bill(self):
        bill = self.generate_bill()
        print("SUB_TOTAL {:.2f}".format(bill["SUB_TOTAL"]))
        print("COUPON_DISCOUNT {} {:.2f}".format(self.discount_coupon, bill.get("COUPON_DISCOUNT", 0)))
        print("TOTAL_PRO_DISCOUNT {:.2f}".format(bill.get("TOTAL_PRO_DISCOUNT", 0)))
        print("PRO_MEMBERSHIP_FEE {:.2f}".format(bill.get("PRO_MEMBERSHIP_FEE", 0)))
        print("ENROLLMENT_FEE {:.2f}".format(bill.get("ENROLLMENT_FEE", 0)))
        print("TOTAL {:.2f}".format(bill["TOTAL"]))