from celery import shared_task
import time
from BusinessManagement.models import OrderFormStatus,OrderForm

# 这里不再使用@app.task,而是用@shared_task，是指定可以在其他APP中也可以调用这个任务
@shared_task
def add(x,y):
    print('########## running add #####################')
    return x + y

@shared_task
def minus(x,y):
    time.sleep(30)
    print('########## running minus #####################')
    return x - y

@shared_task
def process_overtime_orders(id):
	print('===============跑着了===============')
	order = OrderForm.objects.get(id = id)
	#判断是否支付，已支付
	if order.status.code == '1':
		print('===============修改着===============')
		#更改订单状态为取消
		cancle_status =  OrderFormStatus.objects.get(code = '4')
		order.status = cancle_status
		order.save()
		#还原库存数量
		for item in order.product_list.all():
			item.specification.stock += item.purchase_quantity
			item.specification.save()
	#已取消或者支付
	else:
		pass
