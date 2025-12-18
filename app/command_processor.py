from config.constants import COURSES


class CommandProcessor:
    def __init__(self, purchase_service):
        self.service = purchase_service

    def process(self, line):
        parts = line.split()
        cmd = parts[0]

        if cmd == "ADD_PROGRAMME":
            course_name = parts[1]
            quantity = int(parts[2])
            unit_price = COURSES.get(course_name)
            self.service.add_item(course_name, unit_price, quantity)
        elif cmd == "APPLY_PRO_MEMBERSHIP":
            self.service.apply_pro_membership()
        elif cmd == "APPLY_COUPON":
            self.service.apply_discount_coupon(parts[1])
        elif cmd == "PRINT_BILL":
            self.service.print_bill()
    
