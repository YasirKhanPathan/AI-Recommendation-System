import openpyxl
from collections import Counter, defaultdict


def load_dataset(path):
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb["Sheet1"]
    records = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        records.append(
            {
                "order_id": row[0],
                "date": row[1],
                "customer_id": row[2],
                "product": row[3],
                "quantity": row[4],
                "unit_price": row[5],
                "shipping_address": row[6],
                "payment_method": row[7],
                "order_status": row[8],
                "tracking_number": row[9],
                "items_in_cart": row[10],
                "coupon_code": row[11],
                "referral_source": row[12],
                "total_price": row[13],
            }
        )
    return records
